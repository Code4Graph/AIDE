import json
import random
import re
import os
from datasets import load_dataset, DatasetDict, Dataset
import pandas as pd
from tqdm import tqdm
import string
from ftfy import fix_text

SYMBOLS = set(string.punctuation)
prefix_learned_hands_benefits = "Does the post discuss public benefits and social services that people can get from the government?"
prefix_jcrew_blocker = "The JCrew Blocker is a provision that typically includes (1) a prohibition on the borrower from transferring IP to an unrestricted subsidiary, and (2) a requirement that the borrower obtains the consent of its agent/lenders before transferring IP to any subsidiary. Do the following provisions contain JCrew Blockers?"
prefix_supply_chain_disclosure_disclosed_certification = "Does the disclosure meet the following criteria: Does the above statement disclose to what extent, if any, that the retail seller or manufacturer requires direct suppliers to certify that materials incorporated into the product comply with the laws regarding slavery and human trafficking of the country or countries in which they are doing business? Reply with either: Yes, No"
prefix_definition_classification = "Identify if the sentence defines a term."
task_name = {
    "learned_hands_benefits": prefix_learned_hands_benefits,
    "jcrew_blocker": prefix_jcrew_blocker,
    "supply_chain_disclosure_disclosed_certification": prefix_supply_chain_disclosure_disclosed_certification,
    "definition_classification": prefix_definition_classification,
}


def sample_inputs_CE(inputs, K):
    cause, effect = [], []
    sample_idx = random.sample(list(enumerate(inputs)), K)
    for idx, val in sample_idx:
        ce = val.split("\n")
        for c in ce:
            if "[cause]" not in c or "[effect]" not in c:
                continue
            cse = c.split("[cause]")[1].split("->")[0].strip()
            eff = c.split("[effect]")[1].strip()
            cause.append(cse)
            effect.append(eff)
    return cause, effect


def sample_inputs(inputs, K):
    inst, choices = [], []
    sample_idx = random.sample(list(enumerate(inputs)), K)
    for idx, val in sample_idx:
        inst.append(inputs[idx])
        choices.append("options")
    return inst, choices


def loading(file):
    f = open(file)
    data = json.load(f)
    inst = data["samples"]
    choices = []
    for _ in inst:
        choices.append("options")
    return inst, choices


def loading_ce(file):
    f = open(file)
    data = json.load(f)["samples"]
    cause = []
    effect = []
    for dict in data:
        cause.append(dict["cause"])
        effect.append(dict["effect"])
    return cause, effect


def make_triples(use_case, skills):
    triples = []
    for s in skills:
        l = []
        l.append(use_case)
        l.append("has")
        l.append(s)
        triples.append(l)
    return triples


def loading_implicature(file):
    f = open(file)
    data = json.load(f)["samples"]
    utterance = []
    response = []
    for dict in data:
        utterance.append(dict["utterance"])
        response.append(dict["response"])
    return utterance, response


def sample_implicature(inputs, K):
    utterance, response = [], []
    sample_idx = random.sample(list(enumerate(inputs)), K)
    for idx, val in sample_idx:
        ut = val.strip()
        utterance.append(ut)
        response.append("options")
    return utterance, response


def write_json_general(question, choices, file_name):
    question = question.strip()
    choices = choices.strip()
    choices += "\n"
    all_choices = re.findall("correct.(.*?)\n", choices)
    incorrects = re.findall("incorrect.(.*?)\n", choices)
    sub_dictionary = {}
    for c in all_choices:
        if c in incorrects:
            sub_dictionary[c] = 0
        else:
            sub_dictionary[c] = 1
    dictionary = {"input": question, "target_scores": sub_dictionary}
    with open(file_name, "a", encoding="utf-8") as outfile:
        json.dump(dictionary, outfile, ensure_ascii=False, indent=4)
        outfile.write("\n")


def write_json_ce(question, choices, file_name):
    cause = question.strip()
    effect = choices.strip()
    sub_dictionary = {}
    sub_dictionary[cause] = 1
    sub_dictionary[effect] = 0
    dictionary = {"input": "", "target_scores": sub_dictionary}
    with open(file_name, "a", encoding="utf-8") as outfile:
        json.dump(dictionary, outfile, ensure_ascii=False, indent=4)
        outfile.write("\n")


def load_implicature_seed(seed_related_dataset):
    if os.path.exists("./sample.json"):
        new_utterance, new_response = loading_implicature("./sample.json")
    else:
        data = load_dataset(seed_related_dataset, "0-shot", split="validation")
        utterance = data["utterance"]
        new_utterance, new_response = sample_implicature(utterance, K=10)
        d_dict = {"samples": []}
        for idx in range(len(new_utterance)):
            d = {"utterance": new_utterance[idx], "response": new_response[idx]}
            d_dict["samples"].append(d)
        json_object = json.dumps(d_dict, indent=4)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
    return new_utterance, new_response


def load_casual_seed(seed_related_dataset):
    if os.path.exists("./sample.json"):
        cause, effect = loading_ce("./sample.json")
    else:
        data = load_dataset(seed_related_dataset, split="train")
        sub_data = data["gpt_causal_graph"]
        cause, effect = sample_inputs_CE(sub_data, K=10)
        d_dict = {"samples": []}
        for idx in range(len(cause)):
            d = {"cause": cause[idx], "effect": effect[idx]}
            d_dict["samples"].append(d)
        json_object = json.dumps(d_dict, indent=4)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
    return cause, effect


def load_code_seed(seed_related_dataset):
    if os.path.exists("samples.json"):
        instructions, choices = loading("samples.json")
    else:
        py_code_data = load_dataset(
            seed_related_dataset, split="train", trust_remote_code=True
        )
        if "math" in seed_related_dataset:
            py_code = py_code_data["Problem"]
        else:
            py_code = py_code_data["output"]
        instructions, choices = sample_inputs(py_code, K=10)
        d_dict = {"samples": []}
        for idx in range(len(instructions)):
            inst = instructions[idx]
            d_dict["samples"].append(inst)
        with open("samples.json", "w") as outfile:
            json.dump(d_dict, outfile)
    return instructions, choices


def save_path(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    syn_all_file = dirs + "all_synthetic_data.json"
    syn_diver_file = dirs + "diversity_synthetic_data.json"
    syn_reason_file = dirs + "reason_synthetic_data.json"
    syn_concrete_file = dirs + "concrete_synthetic_data.json"
    syn_const_file = dirs + "constraint_synthetic_data.json"
    return (
        syn_const_file,
        syn_concrete_file,
        syn_reason_file,
        syn_diver_file,
        syn_all_file,
    )


def add_info(x, k_hop, persona, operation, knowledge, question, target_score):
    x["k-hop"].append(k_hop)
    x["persona"].append(persona)
    x["op"].append(operation)
    x["knowledge"].append(knowledge)
    x["input"].append(question)
    x["target_scores"].append(target_score)
    return x


def save_config_info_data(
    ds, k_hop, persona, operation, knowledge, question, choices, use_case
):
    if "cause" in use_case:
        question = question.strip()
        choices = choices.strip()
        sub_dictionary = {}
        sub_dictionary[question] = 1
        sub_dictionary[choices] = 0
    else:
        question = question.strip()
        choices = choices.strip()
        choices += "\n"
        all_choices = re.findall("correct.(.*?)\n", choices)
        incorrects = re.findall("incorrect.(.*?)\n", choices)
        ts = ""
        for c in all_choices:
            if c in incorrects:
                c += ":0\n"
                ts += c
            else:
                c += ":1\n"
                ts += c
    ds = add_info(ds, k_hop, persona, operation, knowledge, question, ts)
    return ds


def make_synthetic_dataset(ds):
    dataset = DatasetDict()
    synthetic_dataset = Dataset.from_pandas(
        pd.DataFrame.from_dict(
            {
                "k-hop": [h for h in ds["k-hop"]],
                "persona": [p for p in ds["persona"]],
                "op": [o for o in ds["op"]],
                "knowledge": [k for k in ds["knowledge"]],
                "input": [i for i in ds["input"]],
                "target_scores": [ts for ts in ds["target_scores"]],
            }
        )
    )
    dataset["all"] = synthetic_dataset
    print("dataset['all'][0]", dataset["all"][0])
    return dataset


def initialize_ds():
    ds = {
        "k-hop": [],
        "persona": [],
        "op": [],
        "knowledge": [],
        "input": [],
        "target_scores": [],
    }
    return ds


def write_dataset_to_json(ds):
    ds.save_to_disk("synthetic_data_AIDE")


def load_mmlu_seed(seed_related_dataset, name):
    if os.path.exists("samples.json"):
        instructions, choices = loading("samples.json")
    else:
        if "gsm8k" in seed_related_dataset:
            name = "main"
            data = load_dataset(
                seed_related_dataset, name=name, split="train", trust_remote_code=True
            )
        elif "mmlu" in seed_related_dataset:
            data = load_dataset(
                seed_related_dataset,
                name=name,
                split="validation",
                trust_remote_code=True,
            )
        elif "truthful_qa" in seed_related_dataset:
            name = "multiple_choice"
            data = load_dataset(
                seed_related_dataset,
                name=name,
                split="validation",
                trust_remote_code=True,
            )
        data = data["question"]
        instructions, choices = sample_implicature(data, K=10)
        d_dict = {"samples": []}
        for idx in range(len(instructions)):
            d = {"question": instructions[idx], "response": choices[idx]}
            d_dict["samples"].append(d)
        json_object = json.dumps(d_dict, indent=4)
        with open("sample.json", "w", encoding="utf-8") as outfile:
            outfile.write(json_object)
    return instructions, choices


def load_arc_seed(seed_related_dataset, name):
    if os.path.exists("samples.json"):
        instructions, choices = loading("samples.json")
    else:
        name = "ARC-Challenge"
        data_set = load_dataset(
            seed_related_dataset, name=name, split="train", trust_remote_code=True
        )
        keyword_dict = {
            "Mercury": [],
            "MCAS": [],
            "MDSA": [],
            "AKDE&ED": [],
            "ACTAAP": [],
            "NYSEDREGENTS": [],
            "TAKS": [],
            "TIMSS": [],
            "MEA": [],
            "FCAT": [],
        }
        for data in data_set:
            idx = data["id"].split("_")[0].strip()
            if idx in keyword_dict.keys():
                keyword_dict[idx].append(data["question"])
        instructions, choices = [], []
        for k, v in keyword_dict.items():
            sample_idx = random.sample(list(enumerate(v)), 1)
            for idx, val in sample_idx:
                ut = val.strip()
                instructions.append(ut)
                choices.append("options")
        d_dict = {"samples": []}
        for idx in range(len(instructions)):
            d = {"question": instructions[idx], "response": choices[idx]}
            d_dict["samples"].append(d)
        json_object = json.dumps(d_dict, indent=4)
        with open("sample.json", "w", encoding="utf-8") as outfile:
            outfile.write(json_object)
    return instructions, choices


def load_fin_seed(seed_related_dataset, seed, num_samples_syn):

    dataset = load_dataset(seed_related_dataset, trust_remote_code=True)["test"]
    seed_related_dataset = seed_related_dataset.replace("/", "_")
    random.seed(seed)
    rows_to_syn = set(range(num_samples_syn))
    new_dataset = dataset.shuffle(seed=seed).select(rows_to_syn)
    filtered_dataset = dataset.filter(
        lambda example, idx: idx not in rows_to_syn, with_indices=True
    )
    print(f"Original dataset size: {len(dataset)}")
    print(f"Filtered dataset size: {len(filtered_dataset)}")
    print(f"new dataset size: {len(new_dataset)}")
    os.makedirs("./test_datasets", exist_ok=True)
    dataset_dict = DatasetDict({"test": filtered_dataset}).save_to_disk(
        "./test_datasets/filter_" + seed_related_dataset
    )
    print(f"saving the filtered dataset dictionary: {dataset_dict}")
    d_dict = {"samples": []}
    progress_bar = tqdm(
        total=len(new_dataset), desc="Processing", unit="sample", dynamic_ncols=True
    )
    for idx in range(len(new_dataset)):
        text = fix_text(new_dataset[idx]["query"])
        text = text.split("CHOICES")[0]
        answer = fix_text(new_dataset[idx]["answer"])
        d = {"question": text, "response": answer}
        d_dict["samples"].append(d)
        json_object = json.dumps(d_dict, ensure_ascii=False, indent=4)
        os.makedirs("./samples", exist_ok=True)
        with open(
            "./samples/" + seed_related_dataset + "_sample.json", "w", encoding="utf-8"
        ) as outfile:
            outfile.write(json_object)
        progress_bar.update(1)
    progress_bar.close()
    instruct, choices = [], []
    for d in d_dict["samples"]:
        instruct.append(d["question"])
        choices.append(d["response"])
    return instruct, choices


def load_legal_seed(seed_related_dataset, name, num_samples_syn):

    dataset = load_dataset(seed_related_dataset, name=name, trust_remote_code=True)
    seed_related_dataset = seed_related_dataset.replace("/", "_")
    print(f"keys in dataset: {dataset.keys()}")
    print(f"len of training data: {len(dataset['train'])}")
    print(f"len of test data: {len(dataset['test'])}")
    size_train = len(dataset["train"])
    if size_train > num_samples_syn:
        rows_to_syn = set(range(num_samples_syn))
        dataset = dataset["train"].shuffle(seed=42).select(rows_to_syn)
    else:
        dataset = dataset["train"].shuffle(seed=42)
    if "label" in dataset.column_names:
        dataset = dataset.rename_columns({"label": "answer"})
    d_dict = {"samples": []}
    progress_bar = tqdm(
        total=len(dataset), desc="Processing", unit="sample", dynamic_ncols=True
    )
    for idx in range(len(dataset)):
        text = fix_text(dataset[idx]["text"])
        if name in task_name.keys():
            text = task_name[name] + " " + text
        answer = fix_text(dataset[idx]["answer"])
        question = (
            fix_text(dataset[idx]["question"])
            if "question" in dataset.column_names
            else ""
        )
        if dataset[idx]["text"][-1] in SYMBOLS:
            d = {
                "question": text + " " + question,
                "response": answer,
            }
        else:
            d = {
                "question": text + ". " + question,
                "response": answer,
            }
        d_dict["samples"].append(d)
        os.makedirs("./samples", exist_ok=True)
        json_object = json.dumps(d_dict, ensure_ascii=False, indent=4)
        with open(
            "./samples/" + seed_related_dataset + "_" + name + "_sample.json",
            "w",
            encoding="utf-8",
        ) as outfile:
            outfile.write(json_object)
        progress_bar.update(1)
    progress_bar.close()
    instruct, choices = [], []
    for d in d_dict["samples"]:
        instruct.append(d["question"])
        choices.append(d["response"])
    return instruct, choices


def load_health_seed(seed_related_dataset, seed, num_samples_syn, num_sample_test):

    dataset = load_dataset(seed_related_dataset, trust_remote_code=True)["train"]
    seed_related_dataset = seed_related_dataset.replace("/", "_")
    random.seed(seed)
    rows_to_syn = set(range(num_samples_syn))
    syn_dataset = dataset.shuffle(seed=seed).select(rows_to_syn)
    filtered_dataset = dataset.filter(
        lambda example, idx: idx not in rows_to_syn, with_indices=True
    )
    # for test set
    rows_to_test = set(range(num_sample_test))
    test_dataset = filtered_dataset.shuffle(seed=seed).select(rows_to_test)
    print(f"Original dataset size: {len(dataset)}")
    print(f"test dataset size: {len(test_dataset)}")
    print(f"generate dataset size: {len(syn_dataset)}")
    os.makedirs("./test_datasets", exist_ok=True)
    dataset_dict = DatasetDict({"test": test_dataset}).save_to_disk(
        "./test_datasets/filter_" + str(seed_related_dataset)
    )
    print(f"saving the filtered dataset dictionary: {dataset_dict}")
    d_dict = {"samples": []}
    progress_bar = tqdm(
        total=len(syn_dataset), desc="Processing", unit="sample", dynamic_ncols=True
    )
    for idx in range(len(syn_dataset)):
        text = fix_text(syn_dataset[idx]["input"])
        text = re.sub(r"\{.*?\}", "", text)
        answer = fix_text(syn_dataset[idx]["output"])
        d = {"question": text, "response": answer}
        d_dict["samples"].append(d)
        json_object = json.dumps(d_dict, ensure_ascii=False, indent=4)
        os.makedirs("./samples", exist_ok=True)
        with open(
            "./samples/" + str(seed_related_dataset) + "_sample.json",
            "w",
            encoding="utf-8",
        ) as outfile:
            outfile.write(json_object)
        progress_bar.update(1)
    progress_bar.close()
    instruct, choices = [], []
    for d in d_dict["samples"]:
        instruct.append(d["question"])
        choices.append(d["response"])
    return instruct, choices