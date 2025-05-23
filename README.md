## AIDE: Attribute-Guided MultI-Hop Data Expansion for Data Scarcity in Task-Specific Fine-tuning
--------------------------------------------------------------------------------------------
This is the implementation of AIDE related to the paper:

[AIDE: Attribute-Guided MultI-Hop Data Expansion for Data Scarcity in Task-Specific Fine-tuning, ACL 2025 Industry Track (Oral)](https://arxiv.org/abs/2412.06136)

## Introduction
-We have two options to use a strong LLM to do generation.
    1. we implement an interface to call Claude Sonnet 3.5 and obtain its outputs based on a given prompt by using claude_sonnet35_access.py.
    2. we implement an interface to call GPT-3.5-Turbo (or GPT-4o) and obtain its outputs based on a given prompt by using openai_access.py.

-few_shot.py includes few-shot examples.

-KG_expand.py can be used to expand a knowledge graph by adding more related knowledge into a given knowledge graph.

-meta_instruction.py includes meta prompts.

-persona.py is used to retrieved top-k topic-related personas from Persona Hub and also has a function to generate diverse data using given personas.

-post_process.py is used to post-process synthetic data such as filtering out some noise data (This part can be customized).

-self_reflection.py is used to improve each synthetic data point.

-utils.py includes some helper functions such as writing results to json files and loading data.

-AIDE_synthesis_data.py is the main file which calls functions from above python files.

-prepare_fin_data.py demonstrates how to perform data preparation using the "TheFinAI/flare-cfa" model as an example.

## Data Preparation


