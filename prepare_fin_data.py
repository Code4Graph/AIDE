from datasets import load_dataset, DatasetDict, Dataset
import json
from tqdm import tqdm
import random
from ftfy import fix_text
import os
import re


def process_data_test(seed_related_dataset, syn_dataset, target_size, test=None):
    d_dict = {"examples": []}
    progress_bar = tqdm(
        total=len(syn_dataset), desc="Processing", unit="sample", dynamic_ncols=True
    )
    select_idx = []
    for idx in range(len(syn_dataset)):
        original_text = fix_text(syn_dataset[idx]["query"])
        text = original_text.split(",CHOICES")[0]
        choices_part = re.search(r"CHOICES:\s*(.*) Answer:", original_text).group(1)
        options = dict(re.findall(r"([A-C]):\s*([^,]+)", choices_part))
        answer = fix_text(syn_dataset[idx]["answer"])
        reformatted = {
            value: 1 if key == answer else 0 for key, value in options.items()
        }
        if len(reformatted) != 3:
            continue
        select_idx.append(idx)
        d = {"input": text, "target_scores": reformatted}
        d_dict["examples"].append(d)
        json_object = json.dumps(d_dict, ensure_ascii=False, indent=4)
        os.makedirs("./samples", exist_ok=True)
        if test:
            save_file_name = (
                "./samples/" + str(seed_related_dataset) + "_test_sample.json"
            )
        else:
            save_file_name = "./samples/" + str(seed_related_dataset) + "_sample.json"
        with open(save_file_name, "w", encoding="utf-8") as outfile:
            outfile.write(json_object)
        progress_bar.update(1)
        if len(d_dict["examples"]) == target_size:
            break
    print(f"size of current dataset is {len(d_dict["examples"])}")
    progress_bar.close()
    filtered_dataset = syn_dataset.filter(
        lambda example, idx: idx not in select_idx, with_indices=True
    )
    return filtered_dataset


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

    candidate_gold_training_dataset = process_data_test(
        seed_related_dataset, filtered_dataset, target_size=100, test=True
    )
    print(f"saving the filtered dataset dictionary")
    target_size = (
        1914
        if len(candidate_gold_training_dataset) > 1914
        else len(candidate_gold_training_dataset)
    )
    process_data_test(
        seed_related_dataset + "_gold",
        candidate_gold_training_dataset,
        target_size=target_size,
    )
    print(f"saving the gold train dataset dictionary")


load_fin_seed(
    "TheFinAI/flare-cfa", 42, num_samples_syn=6
)  # https://huggingface.co/datasets/TheFinAI/flare-cfa
print(f"finish sampling")
