## AIDE: Attribute-Guided MultI-Hop Data Expansion for Data Scarcity in Task-Specific Fine-tuning
--------------------------------------------------------------------------------------------
This is the implementation of AIDE related to the paper:

[AIDE: Attribute-Guided MultI-Hop Data Expansion for Data Scarcity in Task-Specific Fine-tuning, ACL 2025 Industry Track (Oral)](https://arxiv.org/abs/2412.06136)

## Introduction
- We have two options to use a strong LLM.
    1. `claude_sonnet35_access.py` provides an interface to call Claude Sonnet 3.5
    2. `openai_access.py` provides an interface to call GPT-3.5-Turbo (or GPT-4o)
    3. Note that you need to have the api_key or role_arn

- `few_shot.py` includes few-shot examples.

- `KG_expand.py` can be used to expand a knowledge graph by adding more related knowledge into a given knowledge graph.

- `meta_instruction.py` includes meta prompts.

- `persona.py` is used to retrieved top-k topic-related personas from Persona Hub and also has a function to generate diverse data using given personas.

- `post_process.py` is used to post-process synthetic data such as filtering out some noise data (This part can be customized).

- `self_reflection.py` is used to improve each synthetic data point.

- `utils.py` includes some helper functions such as writing results to json files and loading data.

- `AIDE_synthesis_data.py` is the main file which calls functions from above python files.

- `prepare_fin_data.py` demonstrates how to perform data preparation using the "TheFinAI/flare-cfa" model as an example (This part can be customized).

## Data Preparation
An example to prepare data (i.e., seed data, gold data and test data). 

    python prepare_fin_data.py

## Run Code
Here is an example to synthesize data using AIDE when finishing data preparation (enabling the reflection would slow down the synthesis):

    python AIDE_synthesis_data.py --choice_type 'multi_choice' --seed_related_dataset 'TheFinAI/flare-cfa' --len_token 500 --r_depth 2 --d_depth 2 --sk_conn 1 --num_triples 2 --use_case "finance" --benchmark "finance" --ex_kg True --persona_hub True --reflection False

## Explanation of Parameters
- `choice_type`: the synthetic data can be multiple choice or binary choice or only simple question (options: "multi_choic", "binary_choice", "").

- `seed_related_dataset`: sampling seed data from a related dataset.

- `len_token`: length of synthetic data.

- `r_depth`: the depth of K-hop synthesis in the direction of relevance.

- `d_depth`: the depth of K-hop synthesis in the direction of diversity.

- `sk_conn`: a threshold related to adding residual connections.

- `num_triples`: number of triplets to expand a knowledge graph.

- `use_case`: a specific task.

- `ex_kg`: if enabling the expansion of knowledge graphs.

- `persona_hub`: if enabling personas to diversify data during synthesis.

- `reflection`: if enabling the reflection mechanism.
