import re
import numpy as np
from transformers import AutoModel
import json
import torch
import random


def load_data(load_path, only_input=False):
    f = open(load_path, "r")
    all_objs = json.load(f)
    opt = ["A. ", "B. ", "C. ", "D. "]
    all = []
    for example in all_objs["examples"]:
        inputs = example["input"].strip()
        if not only_input:
            cnt = 0
            temp_str = ""
            for key, val in example["target_scores"].items():
                temp_str += opt[cnt] + key + "\n "
                cnt += 1
            all.append(inputs + " " + temp_str)
        else:
            all.append(inputs)
    return all, all_objs


def filter_duplicate(path, s_thresold, direction):
    data, all_objs = load_data(path, only_input=True)
    # model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-code', trust_remote_code=True)
    model = AutoModel.from_pretrained(
        "jinaai/jina-embeddings-v2-base-en", trust_remote_code=True
    )
    en_data = model.encode(data, convert_to_tensor=True)

    removal_row = []
    for row in range(en_data.shape[0]):
        if row in removal_row:
            continue
        source_embeddings = en_data[row]
        compare_embeddings = en_data
        cosine_similarities = torch.nn.functional.cosine_similarity(
            source_embeddings, compare_embeddings
        ).tolist()
        idx = np.where(np.array(cosine_similarities) > s_thresold)[0].tolist()
        idx.remove(row)
        if len(idx) > 0:
            removal_row = list(set(removal_row + idx))
    cnt, new_all_objects = 0, {"examples": []}
    for example in all_objs["examples"]:
        d = {"input": "", "target_scores": {}}
        if cnt not in removal_row:
            d["input"] = example["input"].strip()
            d["target_scores"] = example["target_scores"]
            new_all_objects["examples"].append(d)
        cnt += 1

    dict_data = json.dumps(new_all_objects, indent=4)
    out_file = direction + "_post_sd_fd.json"
    with open(out_file, "w") as outfile:
        outfile.write(dict_data)


def random_dic(dicts):
    dict_key_ls = list(dicts.keys())
    random.shuffle(dict_key_ls)
    new_dic = {}
    for key in dict_key_ls:
        new_dic[key] = dicts.get(key)
    return new_dic


def remove_brace(option):
    update_option = option.strip()
    if len(update_option) >= 2 and update_option[1] == ")":
        new_option = update_option[2:].strip()
        return new_option
    else:
        return update_option


def post_process(direction, num, num_target_scores, customized_length_data):
    in_file = direction + "_synthetic_data.json"
    with open(in_file, "r") as openfile:
        json_object = json.load(openfile)

    examples_dict = {}
    examples_dict["examples"] = []
    for sub_dict in json_object["examples"]:
        if len(examples_dict["examples"]) > num:
            break
        if len(sub_dict["input"]) < customized_length_data:
            if len(sub_dict["target_scores"]) > num_target_scores:
                cnt, new_dict = 0, {}
                zeros, ones = [], []
                for key, val in sub_dict["target_scores"].items():
                    key = remove_brace(key)
                    if val == 0:
                        zeros.append(key)
                    else:
                        cnt += 1
                        ones.append(key)
                if cnt == 1:
                    new_dict[ones[0]] = 1
                    zero_sample = random.sample(zeros, num_target_scores - 1)
                    for s in zero_sample:
                        new_dict[s] = 0
                    update_dict = random_dic(new_dict)
                    sub_dict["target_scores"] = update_dict
                    examples_dict["examples"].append(sub_dict)

            elif len(sub_dict["target_scores"]) == num_target_scores:
                cnt, new_dict = 0, {}
                for key, val in sub_dict["target_scores"].items():
                    key = remove_brace(key)
                    new_dict[key] = val
                    if val == 1:
                        cnt += 1
                if cnt == 1:
                    update_dict = random_dic(new_dict)
                    sub_dict["target_scores"] = update_dict
                    examples_dict["examples"].append(sub_dict)
            else:
                print(f"less choices!")

    examples_dict_data = json.dumps(examples_dict, indent=4)
    out_file = direction + "_post_sd2.json"
    with open(out_file, "w") as outfile:
        outfile.write(examples_dict_data)


def post_process_implicatures(direction, num):
    in_file = direction + "_synthetic_data.json"
    with open(in_file, "r") as openfile:
        json_object = json.load(openfile)

    examples_dict = {}
    examples_dict["examples"] = []
    for sub_dict in json_object["examples"]:
        if len(examples_dict["examples"]) > num:
            break
        # preprocessing sub_dict['input']

        if (
            len(sub_dict["input"]) > len("Speaker 1:") + len("Speaker 2:")
            and len(sub_dict["input"]) < 350
        ):
            if len(sub_dict["target_scores"]) == 2:
                cnt = 0
                for key, val in sub_dict["target_scores"].items():
                    if val == 1:
                        cnt += 1
                if (
                    cnt == 1
                    and " Yes" in sub_dict["target_scores"].keys()
                    and " No" in sub_dict["target_scores"].keys()
                ):
                    new_dict = {
                        "Yes": sub_dict["target_scores"][" Yes"],
                        "No": sub_dict["target_scores"][" No"],
                    }
                    sub_dict["target_scores"] = new_dict
                    examples_dict["examples"].append(sub_dict)

    examples_dict_data = json.dumps(examples_dict, indent=4)
    out_file = direction + "_post_sd2.json"
    with open(out_file, "w") as outfile:
        outfile.write(examples_dict_data)


def merge_data(direction_list):
    total_list = []
    for d in direction_list:
        in_file = d + "_post_sd2.json"
        with open(in_file, "r") as openfile:
            json_object = json.load(openfile)
            for obj in json_object["examples"]:
                total_list.append(obj)

    examples_dict = {}
    examples_dict["examples"] = []
    for sub_dict in total_list:
        examples_dict["examples"].append(sub_dict)

    examples_dict_data = json.dumps(examples_dict, indent=4)
    out_file = "all_merge_post_sd.json"
    with open(out_file, "w") as outfile:
        outfile.write(examples_dict_data)


def count_data(path):
    with open(path, "r") as openfile:
        json_object = json.load(openfile)
        print(
            "size of all_path_data of path {}: {}".format(
                path, len(json_object["examples"])
            )
        )


def shuffle_options(path, dirs, num_target_scores):
    with open(path, "r") as openfile:
        json_object = json.load(openfile)
    # action = ["shuffle", "keep"]
    action = ["shuffle"]
    examples_dict = {}
    examples_dict["examples"] = []
    for sub_dict in json_object["examples"]:
        res = random.choice(action)
        if res == "shuffle":
            all_keys = random.sample(
                list(sub_dict["target_scores"].keys()), num_target_scores
            )
            d = {"input": sub_dict["input"], "target_scores": {}}
            for idx in range(num_target_scores):
                d["target_scores"][all_keys[idx]] = sub_dict["target_scores"][
                    all_keys[idx]
                ]
        else:
            d = sub_dict
        examples_dict["examples"].append(d)
    examples_dict_data = json.dumps(examples_dict, indent=4)
    if "fd" in path:
        out_file = dirs + "all_post_sd_fd_shuffle.json"
    else:
        out_file = dirs + "all_post_sd2_shuffle.json"
    with open(out_file, "w") as outfile:
        outfile.write(examples_dict_data)


if __name__ == "__main__":
    direction_list = ["all"]

    for d in direction_list:
        direction = "./synthesis_data_finance/" + d
        post_process(
            direction, num=40004, num_target_scores=3, customized_length_data=10000
        )

    # exk_all_path = "./synthesis_data_legal/all_post_sd2.json"
    # filter_duplicate(exk_all_path, 0.98, "./synthesis_data/all")

    exk_fd_all_path = "./synthesis_data_finance/all_post_sd2.json"

    count_data(exk_fd_all_path)

    shuffle_options(
        "./synthesis_data_finance/all_post_sd2.json",
        "./synthesis_data_finance/",
        num_target_scores=3,
    )
    # shuffle_options("./synthesis_data/all_post_sd_fd.json", "./synthesis_data/")
