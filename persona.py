from meta_instruction import *
import json
from few_shot import *
from transformers import AutoModel
import torch
import numpy as np


def loading_persona_file(file):
    f = open(file)
    data = json.load(f)
    persona_list = data["persona"]
    return persona_list


def sample_save_persona_hub(persona_dataset, K, category, s_thresold):
    persona_list = []
    # model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-code', trust_remote_code=True)
    model = AutoModel.from_pretrained(
        "jinaai/jina-embeddings-v2-base-en", trust_remote_code=True
    )
    compare_embeddings = model.encode(
        persona_dataset["persona"][:50000], convert_to_tensor=True
    )
    source_embeddings = model.encode(category, convert_to_tensor=True)
    cosine_similarities = torch.nn.functional.cosine_similarity(
        source_embeddings, compare_embeddings
    ).tolist()
    idx = np.where(np.array(cosine_similarities) > s_thresold)[0].tolist()
    idx_sim = {}
    for id in idx:
        idx_sim[id] = cosine_similarities[id]
    sorted_idx = sorted(idx_sim)
    if len(sorted_idx) > K:
        for id in sorted_idx[-K:]:
            persona_list.append(persona_dataset["persona"][id])
    else:
        for id in sorted_idx:
            persona_list.append(persona_dataset["persona"][id])
    d_dict = {"persona": persona_list}
    json_object = json.dumps(d_dict, indent=4)
    with open("persona_samples.json", "w") as outfile:
        outfile.write(json_object)
    return persona_list


def generate_diversity_persona(inst, choice, use_case, persona, topic):
    system = "You are a helpful assistant."
    if "binary_choice" in choice:
        content = """\n<Action> <Created Prompt> can be {} related to the topic {} </Action>
                     \n<Action> use the character from <The Given Persona> to generate <Created Prompt>. </Action>
                     \n<Action> <Created Prompt> should be different from <The Given Prompt>. </Action>
                     \n<Action> <Created Prompt> Should BE answered by 'Yes' or 'No'. </Action>
                     \n<Action> <Created Prompt> should be more diverse than <The Given Prompt>. </Action>
                     \n<Action> Alternately generate a random number either 0 or 1. If the random number is 1, <Response> implicitly responds to <Rewritten Prompt>. If the random number is 0, <Response> outputs irrelevant contents to the <Rewritten Prompt>. </Action>
                     \n<Action> Should have <Response> and <Response> should be more than two words. </Action>
                     \nFollow the examples below to generate <Created Prompt> and <Response>. \
                     {}
                  """
    else:
        content = """\n<Action> <Created Prompt> can be {} related to the topic {}. </Action>
                     \n<Action> use the character from <The Given Persona> to generate <Created Prompt>. </Action>
                     \n<Action> <Created Prompt> should be different from <The Given Prompt>. </Action>
                     \n<Action> You should try your best not to make the <Created Prompt> become verbose. </Action>
                     \nFollow the examples below to generate <Created Prompt>.\
                     \n{}\
                  """
    if "multi_choice" in choice:
        if "code" in use_case or "programming" in use_case:
            few_shot = persona_code_multi
        elif "cause" in use_case:
            few_shot = persona_cause_multi
        elif "math" in use_case or "mathematical" in use_case or "bio" in use_case:
            few_shot = persona_math_multi
        elif "computer" in use_case:
            few_shot = persona_computer_multi
        elif "temporal" in use_case:
            few_shot = persona_tmp_multi
        elif "philosophy" in use_case:
            few_shot = persona_philosophy_multi
        elif "marketing" in use_case:
            few_shot = persona_marketing_multi
        elif "truth" in use_case:
            few_shot = persona_truth_multi
        elif "health" in use_case:
            few_shot = persona_health
        elif "finance" in use_case:
            few_shot = persona_fin
    elif "binary_choice" in choice:
        if "code" in use_case or "programming" in use_case:
            few_shot = diversity_code_binary
        elif "math" in use_case or "mathematical" in use_case:
            few_shot = diversity_math_binary
        elif "implicature" in use_case:
            few_shot = persona_imp_binary
        elif "legal" in use_case:
            few_shot = persona_legal
    else:
        few_shot = persona_normal
    content = content.format(use_case, topic, few_shot)
    prompt = base_instruction_creator.format(content)
    prompt += """\nYour output should follow the format of examples, which means preserve the same format and output created prompt within <Created Prompt></Created Prompt> xml tags."""
    if "implicature" in use_case or "temporal" in use_case:
        prompt += "\nPut the response within the <Response></Response> xml tags."
    prompt += "\n<The Given Prompt> {} </The Given Prompt>".format(inst)
    prompt += "\n<The Given Persona> {} </The Given Persona>".format(persona)
    return system, prompt
