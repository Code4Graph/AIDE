from self_reflection import *
from few_shot import *
from persona import (
    generate_diversity_persona,
    sample_save_persona_hub,
    loading_persona_file,
)
from KG_expand import expand_kg
from utils import *
from meta_instruction import *
import argparse
from claude_sonnet35_access import *


def generate_meta_info(instruction, context):
    system = "You are an instruction analyzer."
    prompt = base_meta_info_instruction.format(
        "Now, show me a topic and related knowledge through analyzing the following the given instruction."
    )
    prompt += """ \nYour output should follow the format of examples, which means preserve the same format."""
    prompt += "\n<The Given Instruction> {} </The Given Instruction>".format(
        instruction
    )
    return system, prompt


def rewrite_constraint(
    topic, instruction, starting_inst, opt, use_case, skill, choice_type
):
    system = "You are a Prompt Writer"
    skip_connect = ""
    if len(skip_connect) > 0:
        skip_connect = "\n<EXPECTATION> The <Rewritten Prompt> SHOULD BE SIMILAR TO {}. </EXPECTATION>"
        skip_connect = skip_connect.format(starting_inst)
    if "binary_choice" in choice_type:
        content = """\n<EXPECTATION> <Rewritten Prompt> should be {}. </EXPECTATION>
                         \n<EXPECTATION> The <Rewritten Prompt> can be obtained by adding simple constraints/requirements into <The Given Prompt>. </EXPECTATION>
                         \n<EXPECTATION> The <Rewritten Prompt> is related to {} and {}. </EXPECTATION>
                         \n<EXPECTATION> <Rewritten Prompt> should be solved by 'Yes' or 'No'. </EXPECTATION>
                         \n<EXPECTATION> You can write implicature to response <Rewritten Prompt> in the <Response> or you can write irrelevant content in the <Response>. </EXPECTATION>
                		 \n<EXPECTATION> <Response> should be more than two words. </EXPECTATION>
                		 \n<EXPECTATION> <The Given Prompt>, <Rewritten Prompt>, 'given prompt' and 'rewritten prompt' are not allowed to appear in <Rewritten Prompt>. </EXPECTATION>
                		 \nFollow the below examples to adding constraints into <The Given Prompt> and generate <Rewritten Prompt> and <Response>.
                		 \n{}
                      """
    else:
        content = """\n<EXPECTATION> <Rewritten Prompt> should be {}. </EXPECTATION>
                     \n<EXPECTATION> The <Rewritten Prompt> can be obtained by adding simple constraints into content in <The Given Prompt> </EXPECTATION>
                     \n<EXPECTATION> The <Rewritten Prompt> is related to {} and {}. </EXPECTATION>
                     \n<EXPECTATION> Make the <Rewritten Prompt> become as SHORT as possible. </EXPECTATION>
                     \n<EXPECTATION> <The Given Prompt>, <Rewritten Prompt>, 'given prompt' and 'rewritten prompt' are not allowed to appear in <Rewritten Prompt>. </EXPECTATION>
                     \nFollow the below examples to generate <Rewritten Prompt> by adding constraints into <The Given Prompt>.
                     \n{}
                  """

    if "multi_choice" in choice_type:
        if (
            "code" in use_case
            or "programming" in use_case
            or "implementation" in use_case
        ):
            few_shot = constraint_code_multi
        elif "cause" in use_case:
            few_shot = constraint_cause_multi
        elif "math" in use_case or "arithmetic" in use_case or "bio" in use_case:
            few_shot = constraint_math_multi
        elif "computer" in use_case:
            few_shot = constraint_computer_multi
        elif "temporal" in use_case:
            few_shot = constraint_temporal_multi
        elif "philosophy" in use_case:
            few_shot = constraint_philosophy_multi
        elif "marketing" in use_case:
            few_shot = constraint_marketing_multi
        elif "truth" in use_case:
            few_shot = constraint_truth_multi
        elif "health" in use_case:
            few_shot = constraint_health
        elif "finance" in use_case:
            few_shot = constraint_fin
    elif "binary_choice" in choice_type:
        if (
            "code" in use_case
            or "programming" in use_case
            or "implementation" in use_case
        ):
            few_shot = constraint_code_binary
        elif "math" in use_case or "arithmetic" in use_case:
            few_shot = constraint_math_binary
        elif "implicature" in use_case:
            few_shot = constraint_imp_binary
        elif "legal" in use_case:
            few_shot = constraint_legal
    else:
        few_shot = constraint_normal
    content = content.format(use_case, topic, skill, few_shot)
    if len(skip_connect) > 0:
        content = skip_connect + content
    prompt = base_instruction_rewrite.format(content)
    prompt += """\nYour output should follow the format of examples, which means preserve the same format."""
    if "implicature" in use_case or "temporal" in use_case:
        prompt += "\nPut the response within the <Response></Response> xml tags."
    prompt += "\n<The Given Prompt> {} </The Given Prompt>".format(instruction)
    return system, prompt


def rewrite_concrete(
    topic, instruction, starting_inst, opt, use_case, skill, choice_type
):
    system = "You are a Prompt Writer"
    skip_connect = ""
    if len(skip_connect) > 0:
        skip_connect = "\n<EXPECTATION> The <Rewritten Prompt> SHOULD BE SIMILAR TO the instruction {}. </EXPECTATION>"
        skip_connect = skip_connect.format(starting_inst)
    if "binary_choice" in choice_type:
        content = """\n<EXPECTATION> <Rewritten Prompt> can be {}. </EXPECTATION>
                     \n<EXPECTATION> Replace general concepts in <The Given Prompt> with more specific but simple content in <Rewritten Prompt>. </EXPECTATION>
                     \n<EXPECTATION> <Rewritten Prompt> related to {} can be solved by {}. </EXPECTATION>
                     \n<EXPECTATION> <Rewritten Prompt> Should BE answered by 'Yes' or 'No'. </EXPECTATION>
                     \n<EXPECTATION> Alternately generate a random number either 0 or 1. If the random number is 1, <Response> implicitly responds to <Rewritten Prompt>. If the random number is 0, <Response> outputs irrelevant contents to the <Rewritten Prompt>. </EXPECTATION>
                     \n<EXPECTATION> <Response> should be more than two words. </EXPECTATION>
                     \n<EXPECTATION> '<The Given Prompt>', '<Rewritten Prompt>', ‘given prompt’ and ‘rewritten prompt’ are not allowed to appear in <Rewritten Prompt>. </EXPECTATION>
                     \nFollow the below examples to add more specific but simple content in <The Given Prompt> and generate <Rewritten Prompt> and <Response>.
                     \n{}
                      """
    else:
        content = """\n<EXPECTATION> <Rewritten Prompt> can be {}. </EXPECTATION>
                     \n<EXPECTATION> Replace general concepts in <The Given Prompt> with more specific but simple content in <Rewritten Prompt>. </EXPECTATION>
                     \n<EXPECTATION> <Rewritten Prompt> related to {} task can be solved by {}. </EXPECTATION>
                     \n<EXPECTATION> Make the <Rewritten Prompt> become as SHORT as possible. </EXPECTATION>
                     \n<EXPECTATION> <The Given Prompt>, <Rewritten Prompt>, 'given prompt' and 'rewritten prompt' are not allowed to appear in <Rewritten Prompt>. </EXPECTATION>
                     \nFollow the below examples to generate <Rewritten Prompt> by concreting <The Given Prompt>. 
                     \n{}
                 """
    if "multi_choice" in choice_type:
        if (
            "code" in use_case
            or "programming" in use_case
            or "implementation" in use_case
        ):
            few_shot = concrete_code_multi
        elif "cause" in use_case:
            few_shot = concrete_cause_multi
        elif (
            "math" in use_case
            or "mathematical" in use_case
            or "arithmetic" in use_case
            or "bio" in use_case
        ):
            few_shot = concrete_math_multi
        elif "computer" in use_case:
            few_shot = concrete_computer_multi
        elif "temporal" in use_case:
            few_shot = concrete_temporal_multi
        elif "philosophy" in use_case:
            few_shot = concrete_philosophy_multi
        elif "marketing" in use_case:
            few_shot = concrete_marketing_multi
        elif "truth" in use_case:
            few_shot = concrete_truth_multi
        elif "health" in use_case:
            few_shot = concrete_health
        elif "finance" in use_case:
            few_shot = concrete_fin
    elif "binary_choice" in choice_type:
        if (
            "code" in use_case
            or "programming" in use_case
            or "implementation" in use_case
        ):
            few_shot = concrete_code_binary
        elif (
            "math" in use_case or "mathematical" in use_case or "arithmetic" in use_case
        ):
            few_shot = concrete_math_binary
        elif "implicature" in use_case:
            few_shot = concrete_imp_binary
        elif "legal" in use_case:
            few_shot = concrete_legal
    else:
        few_shot = concrete_normal
    content = content.format(use_case, topic, skill, few_shot)
    if len(skip_connect) > 0:
        content = skip_connect + content
    prompt = base_instruction_rewrite.format(content)
    prompt += """\nYour output should follow the format of examples, which means preserve the same format."""
    if "implicature" in use_case or "temporal" in use_case:
        prompt += "\nPut the response within the <Response></Response> xml tags."
    prompt += "\n<The Given Prompt> {} </The Given Prompt>".format(instruction)
    return system, prompt


def rewrite_reasoning(
    topic, instruction, starting_inst, opt, use_case, skill, choice_type
):
    system = "You are a Prompt Writer"
    skip_connect = ""
    if len(starting_inst) > 0:
        skip_connect = "\n<EXPECTATION> The rewritten prompt within the <Rewritten Prompt></Rewritten Prompt> xml tags SHOULD BE SIMILAR TO {}. </EXPECTATION>"
        skip_connect = skip_connect.format(starting_inst)
    if "binary_choice" in choice_type:
        content = """\n<EXPECTATION> The rewritten prompt within the <Rewritten Prompt></Rewritten Prompt> xml tags can be {}. </EXPECTATION>
                     \n<EXPECTATION> Rewrite the given prompt as a rewritten prompt with different but simple content by increasing reasoning within the <Rewritten Prompt></Rewritten Prompt> xml tags. </EXPECTATION>
                     \n<EXPECTATION> The rewritten prompt related to {} can be solved by {}. </EXPECTATION>
                     \n<EXPECTATION> The rewritten prompt can be answered by 'Yes' or 'No'. </EXPECTATION>
                     \n<EXPECTATION> Alternately generate a random number either 0 or 1. If the random number is 1, a response within <Response></Response> xml tags implicitly responds to the rewritten prompt. If the random number is 0, the response has irrelevant contents to the rewritten prompt. </EXPECTATION>
                     \n<EXPECTATION> The response should be more than two words. </EXPECTATION>
                     \n<EXPECTATION> 'The Given Prompt', 'Rewritten Prompt', ‘given prompt’ and ‘rewritten prompt’ are not allowed to appear in the rewritten prompt. </EXPECTATION>
                     \nFollow the below examples to increases reasoning of the given prompt and generate rewritten prompt and response. 
                     \n{}
                     """
    else:
        content = """\n<EXPECTATION> The rewritten prompt within the <Rewritten Prompt></Rewritten Prompt> xml tags can be {}. </EXPECTATION>
                     \n<EXPECTATION> Rewrite the given prompt as a rewritten prompt with different but simple content by increasing reasoning within the <Rewritten Prompt></Rewritten Prompt> xml tags. </EXPECTATION>
                     \n<EXPECTATION> The rewritten prompt related to {} can be solved by {}. </EXPECTATION>
                     \n<EXPECTATION> Make the rewritten prompt become as SHORT as possible. </EXPECTATION>
                     \n<EXPECTATION> 'The Given Prompt', 'Rewritten Prompt', ‘given prompt’ and ‘rewritten prompt’ are not allowed to appear in <Rewritten Prompt>. </EXPECTATION>
                     \nFollow the below examples to increases reasoning of the given prompt and generate the rewritten prompt. </EXPECTATION>
                     \n{}
                  """
    if "multi_choice" in choice_type:
        if "code" in use_case or "programming" in use_case:
            few_shot = reasoning_code_multi
        elif "cause" in use_case:
            few_shot = reasoning_cause_multi
        elif "math" in use_case or "arithmetic" in use_case or "bio" in use_case:
            few_shot = reasoning_math_multi
        elif "computer" in use_case:
            few_shot = reasoning_computer_multi
        elif "temporal" in use_case:
            few_shot = reasoning_temporal_multi
        elif "philosophy" in use_case:
            few_shot = reasoning_philosophy_multi
        elif "marketing" in use_case:
            few_shot = reasoning_marketing_multi
        elif "truth" in use_case:
            few_shot = reasoning_truth_multi
        elif "health" in use_case:
            few_shot = reasoning_health
        elif "finance" in use_case:
            few_shot = reasoning_fin
    elif "binary_choice" in choice_type:
        if (
            "code" in use_case
            or "programming" in use_case
            or "implementation" in use_case
        ):
            few_shot = reasoning_code_binary
        elif (
            "math" in use_case or "mathematical" in use_case or "arithmetic" in use_case
        ):
            few_shot = reasoning_math_binary
        elif "implicature" in use_case:
            few_shot = reasoning_imp_binary
        elif "legal" in use_case:
            few_shot = reasoning_legal
    else:
        few_shot = reasoning_normal
    content = content.format(use_case, topic, skill, few_shot)
    if len(skip_connect) > 0:
        content = skip_connect + content
    prompt = base_instruction_rewrite.format(content)
    prompt += """\nYour output should follow the format of examples, which means preserve the same format."""
    if "implicature" in use_case or "temporal" in use_case:
        prompt += "\nPut the response within the <Response></Response> xml tags."
    prompt += "\n<The Given Prompt> {} </The Given Prompt>".format(instruction)
    return system, prompt


def generate_binary_choice(inst, type):
    system = "You are an expert of understanding implicatures which are the phenomenon whereby a person means to convey a message that is not explicitly expressed. "
    if "implicature" in type:
        prompt = base_instruction_binary_choice.format(
            generate_binary_choice_implicatures,
            "predict whether Speaker 2 explicitly or implicitly answers to Speaker 1",
            "Now, show me the <Choices> through solving the following <Rewritten Prompt> by step and step thinking.",
        )
    elif "legal" in type:
        prompt = base_instruction_binary_choice.format(
            generate_binary_choice_legal,
            "The question is related to Yes or No.",
            "Now, show me the <Choices> through solving the following <Rewritten Prompt> by step and step thinking.",
        )
    else:
        return "", ""
    prompt += """\nYour output should follow the format of examples, which means preserve the same format and put the choices within the <Choices></Choices> xml tags."""
    prompt += "\n<Rewritten Prompt> {} </Rewritten Prompt>".format(inst)
    return system, prompt


def generate_normal_answer(inst, type):
    system = "You are an expert of solving the question"
    prompt = base_instruction_common
    prompt += """\nYour output should follow the format of examples, which means preserve the same format and put the choices within the <Choices></Choices> xml tags."""
    prompt += "\n<Rewritten Prompt> {} </Rewritten Prompt>".format(inst)
    return system, prompt


def generate_multi_choice(inst, type):
    system = "You are an solver of {} questions and must give the answer.".format(type)
    if "code" in type:
        prompt = base_instruction_mul_choice_generate.format(
            generate_mul_choice_code,
            "Now, show me the <Choices> through solving the following <Rewritten Prompt> by step and step thinking.",
        )
    elif "cause" in type:
        prompt = base_instruction_mul_choice_generate.format(
            generate_mul_choice_ce,
            "Now, show me the <Choices> through solving the following <Rewritten Prompt> by step and step thinking.",
        )
    elif "math" in type or "arithmetic" in type or "bio" in type:
        prompt = base_instruction_mul_choice_generate.format(
            generate_mul_choice_math,
            "Now, show me the <Choices> through solving the following <Rewritten Prompt> by step and step thinking.",
        )
    elif "temporal" in type:
        prompt = base_instruction_mul_choice_generate.format(
            generate_mul_choice_temp,
            "Now, show me the <Choices> through solving the following <Rewritten Prompt> by step and step thinking.",
        )
    elif "computer" in type:
        prompt = base_instruction_mul_choice_generate.format(
            generate_mul_choice_computer,
            "Now, show me the <Choices> through solving the following <Rewritten Prompt> by step and step thinking.",
        )
    elif "philosophy" in type:
        prompt = base_instruction_mul_choice_generate.format(
            generate_mul_choice_philosophy,
            "Now, show me the <Choices> through solving the following <Rewritten Prompt> by step and step thinking.",
        )
    elif "marketing" in type:
        prompt = base_instruction_mul_choice_generate.format(
            generate_mul_choice_marketing,
            "Now, show me the <Choices> through solving the following <Rewritten Prompt> by step and step thinking.",
        )
    elif "truth" in type or "health" in type or "finance" in type:
        prompt = base_instruction_mul_choice_generate.format(
            generate_mul_choice_truth,
            "Now, show me the <Choices> through solving the following <Rewritten Prompt> by step and step thinking.",
        )
    else:
        return "", ""
    prompt += """ Your output should follow the format of examples, which means preserve the same format. \r\n"""
    prompt += "<Rewritten Prompt> {} </Rewritten Prompt>".format(inst)
    return system, prompt


def generate_diversity(inst, choice, use_case, topic):
    system = "You are a Prompt Creator."
    if "binary_choice" in choice:
        content = """\n<EXPECTATION> <Created Prompt> should be {} related to the topic {}. </EXPECTATION> 
                     \n<EXPECTATION>  Use external knowledge to select a topic related to <The Given Prompt> but in same domain. </EXPECTATION> 
                     \n<EXPECTATION>  Use the selected topic to generate a new instruction <Created Prompt>. </EXPECTATION> 
                     \n<EXPECTATION>  <Created Prompt> Should BE answered by 'Yes' or 'No'. </EXPECTATION> 
                     \n<EXPECTATION>  <Created Prompt> should be more diverse than <The Given Prompt>. </EXPECTATION> 
                     \n<EXPECTATION>  Alternately generate a random number either 0 or 1. If the random number is 1, <Response> implicitly responds to <Rewritten Prompt>. If the random number is 0, <Response> outputs irrelevant contents to the <Rewritten Prompt>. </EXPECTATION> 
                     \n<EXPECTATION>  Should have <Response> and <Response> should be more than two words. </EXPECTATION> 
                     \nFollow the examples below to generate <Created Prompt> and <Response>. 
                     {}
                     """
    else:
        content = """\n<EXPECTATION>  <Created Prompt> should be {} related to the topic {}. </EXPECTATION> 
                     \n<EXPECTATION>  Use external knowledge to select a topic related to <The Given Prompt> but in same domain. </EXPECTATION> 
                     \n<EXPECTATION>  Use the selected topic to generate a new and complicate instruction <Created Prompt>. </EXPECTATION> 
                     \n<EXPECTATION>  <Created Prompt> should be more diverse than <The Given Prompt>. </EXPECTATION> 
                     \n<EXPECTATION>  You should try your best not to make the <Created Prompt> become verbose. </EXPECTATION> 
                     \n<EXPECTATION>  ‘<The Given Prompt>’, ‘<Created Prompt>’, ‘given prompt’ and ‘created prompt’ are not allowed to appear in <Created Prompt>. </EXPECTATION> 
                     \nFollow the examples below to generate <Created Prompt>.
                     {}
                  """
    if "multi_choice" in choice:
        if "code" in use_case or "programming" in use_case:
            few_shot = diversity_code_multi
        elif "cause" in use_case:
            few_shot = diversity_cause_multi
        elif "math" in use_case or "mathematical" in use_case or "bio" in use_case:
            few_shot = diversity_math_multi
        elif "computer" in use_case:
            few_shot = diversity_computer_multi
        elif "temporal" in use_case:
            few_shot = diversity_tmp_multi
        elif "philosophy" in use_case:
            few_shot = diversity_philosophy_multi
        elif "marketing" in use_case:
            few_shot = diversity_marketing_multi
        elif "truth" in use_case:
            few_shot = diversity_truth_multi
    elif "binary_choice" in choice:
        if "code" in use_case or "programming" in use_case:
            few_shot = diversity_code_binary
        elif "math" in use_case or "mathematical" in use_case:
            few_shot = diversity_math_binary
        elif "implicature" in use_case:
            few_shot = diversity_imp_binary
    else:
        few_shot = diversity_normal
    content = content.format(use_case, topic, few_shot)
    prompt = base_instruction_creator.format(content)
    prompt += """\nYour output should follow the format of examples, which means preserve the same format and put the answer within the <Created Prompt></Created Prompt> xml tags.."""
    if "implicature" in use_case or "temporal" in use_case:
        prompt += "\nPut the response within the <Response></Response> xml tags."
    prompt += "\n<The Given Prompt> {} </The Given Prompt>".format(inst)
    return system, prompt


def call_relevance_synthesis(
    reflection,
    topic,
    use_case,
    layer,
    skip_conn,
    skill,
    start_ins,
    instr,
    opts,
    direction,
    choice_type,
    len_token,
):
    if layer > skip_conn:
        if "reasoning" in direction:
            system_pt, prompt = rewrite_reasoning(
                topic=topic,
                instruction=instr,
                starting_inst=start_ins,
                opt=opts,
                use_case=use_case,
                skill=skill,
                choice_type=choice_type,
            )
        elif "concrete" in direction:
            system_pt, prompt = rewrite_concrete(
                topic=topic,
                instruction=instr,
                starting_inst=start_ins,
                opt=opts,
                use_case=use_case,
                skill=skill,
                choice_type=choice_type,
            )
        elif "constraint" in direction:
            system_pt, prompt = rewrite_constraint(
                topic=topic,
                instruction=instr,
                starting_inst=start_ins,
                opt=opts,
                use_case=use_case,
                skill=skill,
                choice_type=choice_type,
            )
        else:
            raise Exception("The given condition has not been implement!")
    else:
        if "reasoning" in direction:
            system_pt, prompt = rewrite_reasoning(
                topic=topic,
                instruction=instr,
                starting_inst="",
                opt=opts,
                use_case=use_case,
                skill=skill,
                choice_type=choice_type,
            )
        elif "concrete" in direction:
            system_pt, prompt = rewrite_concrete(
                topic=topic,
                instruction=instr,
                starting_inst="",
                opt=opts,
                use_case=use_case,
                skill=skill,
                choice_type=choice_type,
            )
        elif "constraint" in direction:
            system_pt, prompt = rewrite_constraint(
                topic=topic,
                instruction=instr,
                starting_inst="",
                opt=opts,
                use_case=use_case,
                skill=skill,
                choice_type=choice_type,
            )
        else:
            raise Exception("The given condition has not been implement!")
    ans = get_claude_response(system_pt, prompt)
    print("prompt: ", prompt)
    print("ans: ", ans)
    llm_response, llm_rewrite = "", ""
    if ("<Rewritten Prompt>" in ans and "</Rewritten Prompt>" in ans) or (
        "<rewritten prompt>" in ans and "</rewritten prompt>" in ans
    ):
        if "<Rewritten Prompt>" in ans and "</Rewritten Prompt>" in ans:
            llm_rewrite = re.findall(
                "<Rewritten Prompt>(.*?)</Rewritten Prompt>", ans, re.S
            )[-1].strip()
        else:
            llm_rewrite = re.findall(
                "<rewritten prompt>(.*?)</rewritten prompt>", ans, re.S
            )[-1].strip()
    else:
        llm_rewrite = ""
    if ("<Response>" in ans and "</Response>" in ans) or (
        "<response>" in ans and "</response>" in ans
    ):
        if "<Response>" in ans and "</Response>" in ans:
            llm_response = re.findall("<Response>(.*?)</Response>", ans, re.S)[
                -1
            ].strip()
        else:
            llm_response = re.findall("<response>(.*?)</response>", ans, re.S)[
                -1
            ].strip()
    else:
        llm_response = ""
    if "implicature" in use_case:
        res = (
            "Speaker 1: "
            + "'"
            + llm_rewrite.strip()
            + "'"
            + " Speaker 2: "
            + "'"
            + llm_response.strip()
            + "'"
        )
    elif "temporal" in use_case:
        res = (
            llm_rewrite.strip()
            + " Between what times could they have gone? \nWe know that: "
            + llm_response.strip()
        )
    else:
        res = llm_rewrite.strip() + llm_response.strip()
    if "multi_choice" in choice_type:
        c_system, c_prompt = generate_multi_choice(res, use_case)
    elif "binary_choice" in choice_type:
        c_system, c_prompt = generate_binary_choice(res, use_case)
    else:
        c_system, c_prompt = generate_normal_answer(inst, use_case)
    choice_ans = get_claude_response(c_system, c_prompt)
    print(choice_ans)
    if ("<Choices>" in choice_ans and "</Choices>" in choice_ans) or (
        "<choices>" in choice_ans and "</choices>" in choice_ans
    ):
        if "<Choices>" in choice_ans and "</Choices>" in choice_ans:
            res_choice = re.findall("<Choices>(.*?)</Choices>", choice_ans, re.S)[
                -1
            ].strip()
        else:
            res_choice = re.findall("<choices>(.*?)</choices>", choice_ans, re.S)[
                -1
            ].strip()
    else:
        res_choice = ""
    imp_ans = res
    imp_choice = res_choice
    if reflection:
        imp_ans, imp_choice = reflection_relevance(
            start_ins,
            res,
            res_choice,
            choice_type=choice_type,
            use_case=use_case,
            len_token=len_token,
        )
    return imp_ans, imp_choice


def topic_attributes(inst, context):
    system_info, prompt = generate_meta_info(inst, context)
    ans = get_claude_response(system_info, prompt).strip()
    topic = re.findall("<Topic>(.*?)</Topic>", ans)[-1].strip()
    attributes = (
        re.findall("<Related knowledge>(.*?)</Related knowledge>", ans)[-1]
        .strip()
        .split(",")
    )
    t, s = [], []
    for i in range(len(topic)):
        t.append(topic[i].lower())
    for i in range(len(attributes)):
        s.append(attributes[i].strip().lower())
    return topic, attributes


def call_diversity_synthesis(
    reflection, instruction, use_case, choice_type, persona, len_token, topic
):
    if len(persona):
        system, prompt = generate_diversity_persona(
            instruction, choice_type, use_case, persona, topic
        )
    else:
        system, prompt = generate_diversity(inst, choice_type, use_case, topic)
    ans = get_claude_response(system, prompt)
    print("ans: ", ans)
    llm_diversity, llm_response = "", ""
    if ("<Created Prompt>" in ans and "</Created Prompt>" in ans) or (
        "<created prompt>" in ans and "</created prompt>" in ans
    ):
        if "<Created Prompt>" in ans and "</Created Prompt>" in ans:
            llm_diversity = re.findall(
                "<Created Prompt>(.*?)</Created Prompt>", ans, re.S
            )[-1].strip()
        else:
            llm_diversity = re.findall(
                "<created prompt>(.*?)</created prompt>", ans, re.S
            )[-1].strip()
    else:
        llm_diversity = ""
    if ("<Response>" in ans and "</Response>" in ans) or (
        "<response>" in ans and "</response>" in ans
    ):
        if "<Response>" in ans and "</Response>" in ans:
            llm_response = re.findall("<Response>(.*?)</Response>", ans, re.S)[
                -1
            ].strip()
        else:
            llm_response = re.findall("<response>(.*?)</response>", ans, re.S)[
                -1
            ].strip()
    else:
        llm_response = ans
    if "implicature" in use_case:
        f_q = (
            "Speaker 1: "
            + "'"
            + llm_diversity.strip()
            + "'"
            + " Speaker 2: "
            + "'"
            + llm_response.strip()
            + "'"
        )
    elif "temporal" in use_case:
        f_q = (
            llm_diversity.strip()
            + " Between what times could they have gone? \nWe know that: "
            + llm_response.strip()
        )
    else:
        f_q = llm_diversity.strip() + llm_response.strip()
    if "multi_choice" in choice_type:
        c_system, c_prompt = generate_multi_choice(f_q, use_case)
    elif "binary_choice" in choice_type:
        c_system, c_prompt = generate_binary_choice(f_q, use_case)
    else:
        c_system, c_prompt = generate_normal_answer(f_q, use_case)
    choice_ans = get_claude_response(c_system, c_prompt)
    if ("<Choices>" in choice_ans and "</Choices>" in choice_ans) or (
        "<choices>" in choice_ans and "</choices>" in choice_ans
    ):
        if "<Choices>" in choice_ans and "</Choices>" in choice_ans:
            f_choice = re.findall("<Choices>(.*?)</Choices>", choice_ans, re.S)[
                -1
            ].strip()
        else:
            f_choice = re.findall("<choices>(.*?)</choices>", choice_ans, re.S)[
                -1
            ].strip()
    else:
        f_choice = ""
    imp_q = f_q
    imp_choice = f_choice
    if reflection:
        imp_q, imp_choice = reflection_diversity(
            instruction,
            f_q,
            f_choice,
            choice_type=choice_type,
            use_case=use_case,
            len_token=len_token,
        )
    return imp_q, imp_choice


def reflection_diversity(
    pre_inst, inst, opts, choice_type, use_case, len_token, max_improve=20, max_opt=20
):
    cnt_improve = 0
    cnt_opt = 0
    relevance = 10
    save_inst = inst
    if len_token < len(inst):
        reflection = "The length of <The Given Prompt> is too long when comparing with the <Pre-prompt>, please make <The Given Prompt> shorter in the <Improved Prompt>."
        inst = improve(inst, pre_inst, reflection, use_case)
    if save_inst != inst:
        if len(opts):
            if "multi_choice" in choice_type:
                c_system, c_prompt = generate_multi_choice(inst, use_case)
            elif "binary_choice" in choice_type:
                c_system, c_prompt = generate_binary_choice(inst, use_case)
            else:
                c_system, c_prompt = generate_normal_answer(inst, use_case)
            choice_ans = get_claude_response(c_system, c_prompt)
            if ("<Choices>" in choice_ans and "</Choices>" in choice_ans) or (
                "<choices>" in choice_ans and "</choices>" in choice_ans
            ):
                if "<Choices>" in choice_ans and "</Choices>" in choice_ans:
                    opts = re.findall("<Choices>(.*?)</Choices>", choice_ans, re.S)[
                        -1
                    ].strip()
                else:
                    opts = re.findall("<choices>(.*?)</choices>", choice_ans, re.S)[
                        -1
                    ].strip()
            else:
                opts = ""
    while cnt_improve < max_improve:
        diversity = check_diversity(inst, pre_inst, use_case)
        if diversity > 4:
            if len(opts):
                while (
                    not check_sol_choice(inst, opts, use_case)
                    and cnt_opt < max_opt
                    and choice_type != "binary_choice"
                ):
                    if "multi_choice" in choice_type:
                        c_system, c_prompt = generate_multi_choice(inst, use_case)
                    elif "binary_choice" in choice_type:
                        c_system, c_prompt = generate_binary_choice(inst, use_case)
                    else:
                        c_system, c_prompt = generate_normal_answer(inst, use_case)
                    choice_ans = get_claude_response(c_system, c_prompt)
                    if ("<Choices>" in choice_ans and "</Choices>" in choice_ans) or (
                        "<choices>" in choice_ans and "</choices>" in choice_ans
                    ):
                        if "<Choices>" in choice_ans and "</Choices>" in choice_ans:
                            opts = re.findall(
                                "<Choices>(.*?)</Choices>", choice_ans, re.S
                            )[-1].strip()
                        else:
                            opts = re.findall(
                                "<choices>(.*?)</choices>", choice_ans, re.S
                            )[-1].strip()
                    else:
                        opts = ""
                    cnt_opt += 1
                return inst, opts
            else:
                return inst, opts
        elif diversity <= 4:
            inst = self_reflection(inst, pre_inst, use_case, relevance, diversity)
            if len(opts):
                if "multi_choice" in choice_type:
                    c_system, c_prompt = generate_multi_choice(inst, use_case)
                elif "binary_choice" in choice_type:
                    c_system, c_prompt = generate_binary_choice(inst, use_case)
                else:
                    c_system, c_prompt = generate_normal_answer(inst, use_case)
                choice_ans = get_claude_response(c_system, c_prompt)
                if ("<Choices>" in choice_ans and "</Choices>" in choice_ans) or (
                    "<choices>" in choice_ans and "</choices>" in choice_ans
                ):
                    if "<Choices>" in choice_ans and "</Choices>" in choice_ans:
                        opts = re.findall("<Choices>(.*?)</Choices>", choice_ans, re.S)[
                            -1
                        ].strip()
                    else:
                        opts = re.findall("<choices>(.*?)</choices>", choice_ans, re.S)[
                            -1
                        ].strip()
                else:
                    opts = ""
        cnt_improve += 1
    return inst, opts


def reflection_relevance(
    pre_inst, inst, opts, choice_type, use_case, len_token, max_improve=5, max_opt=5
):
    cnt_improve = 0
    cnt_opt = 0
    diversity = 10
    save_inst = inst
    if len_token < len(inst):
        reflection = "The length of <The Given Prompt> is too long when comparing with the <Pre-prompt>, please make <The Given Prompt> shorter in the <Improved Prompt>."
        inst = improve(inst, pre_inst, reflection, use_case)
    if save_inst != inst:
        if len(opts):
            if "multi_choice" in choice_type:
                c_system, c_prompt = generate_multi_choice(inst, use_case)
            elif "binary_choice" in choice_type:
                c_system, c_prompt = generate_binary_choice(inst, use_case)
            else:
                c_system, c_prompt = generate_normal_answer(inst, use_case)
            choice_ans = get_claude_response(c_system, c_prompt)
            if ("<Choices>" in choice_ans and "</Choices>" in choice_ans) or (
                "<choices>" in choice_ans and "</choices>" in choice_ans
            ):
                if "<Choices>" in choice_ans and "</Choices>" in choice_ans:
                    opts = re.findall("<Choices>(.*?)</Choices>", choice_ans, re.S)[
                        -1
                    ].strip()
                else:
                    opts = re.findall("<choices>(.*?)</choices>", choice_ans, re.S)[
                        -1
                    ].strip()
            else:
                opts = ""
    while cnt_improve < max_improve:
        relevance = check_relevance(inst, pre_inst, use_case)
        if relevance > 4:
            if len(opts):
                while not check_sol_choice(inst, opts, use_case) and cnt_opt < max_opt:
                    if "multi_choice" in choice_type:
                        c_system, c_prompt = generate_multi_choice(inst, use_case)
                    elif "binary_choice" in choice_type:
                        c_system, c_prompt = generate_binary_choice(inst, use_case)
                    else:
                        c_system, c_prompt = generate_normal_answer(inst, use_case)
                    choice_ans = get_claude_response(c_system, c_prompt)
                    if ("<Choices>" in choice_ans and "</Choices>" in choice_ans) or (
                        "<choices>" in choice_ans and "</choices>" in choice_ans
                    ):
                        if "<Choices>" in choice_ans and "</Choices>" in choice_ans:
                            opts = re.findall(
                                "<Choices>(.*?)</Choices>", choice_ans, re.S
                            )[-1].strip()
                        else:
                            opts = re.findall(
                                "<choices>(.*?)</choices>", choice_ans, re.S
                            )[-1].strip()
                    else:
                        opts = ""
                    cnt_opt += 1
                return inst, opts
            else:
                return inst, opts
        else:
            inst = self_reflection(inst, pre_inst, use_case, relevance, diversity)
            if len(opts):
                if "multi_choice" in choice_type:
                    c_system, c_prompt = generate_multi_choice(inst, use_case)
                elif "binary_choice" in choice_type:
                    c_system, c_prompt = generate_binary_choice(inst, use_case)
                else:
                    c_system, c_prompt = generate_normal_answer(inst, use_case)
                choice_ans = get_claude_response(c_system, c_prompt)
                if ("<Choices>" in choice_ans and "</Choices>" in choice_ans) or (
                    "<choices>" in choice_ans and "</choices>" in choice_ans
                ):
                    if "<Choices>" in choice_ans and "</Choices>" in choice_ans:
                        opts = re.findall("<Choices>(.*?)</Choices>", choice_ans, re.S)[
                            -1
                        ].strip()
                    else:
                        opts = re.findall("<choices>(.*?)</choices>", choice_ans, re.S)[
                            -1
                        ].strip()
                else:
                    opts = ""
        cnt_improve += 1
    return inst, opts


def mixed_meta_path_synthesis(
    reflection,
    ds,
    write_json,
    ex_kg,
    persona_hub,
    use_case,
    num_triples,
    start_inst,
    input_inst,
    input_opt,
    choice_type,
    cond_list,
    layer,
    r_depth,
    d_depth,
    sk_conn,
    syn_all_file,
    syn_diver_file,
    syn_reason_file,
    syn_concrete_file,
    syn_const_file,
    len_token,
    last_direction,
):
    topic, attributes = topic_attributes(input_inst, "")
    print("topic: ", topic)
    print("attributes: ", attributes)
    if layer <= r_depth and len(attributes) > 0:
        if ex_kg:
            triples = make_triples(topic, attributes)
            expand_skill = expand_kg(triples, num_triples, topic)
            if len(expand_skill):
                attributes = list(set(attributes + expand_skill))
        for s in attributes:
            for key in cond_list:
                output_inst, output_opt = "", ""
                if "reasoning" == key:
                    output_inst, output_opt = call_relevance_synthesis(
                        reflection,
                        topic=topic,
                        use_case=use_case,
                        layer=layer,
                        skip_conn=sk_conn,
                        skill=s,
                        start_ins=start_inst,
                        instr=input_inst,
                        opts=input_opt,
                        direction=key,
                        choice_type=choice_type,
                        len_token=len_token,
                    )
                    write_json(output_inst, output_opt, syn_reason_file)
                elif "concrete" == key:
                    output_inst, output_opt = call_relevance_synthesis(
                        reflection,
                        topic=topic,
                        use_case=use_case,
                        layer=layer,
                        skip_conn=sk_conn,
                        skill=s,
                        start_ins=start_inst,
                        instr=input_inst,
                        opts=input_opt,
                        direction=key,
                        choice_type=choice_type,
                        len_token=len_token,
                    )
                    write_json(output_inst, output_opt, syn_concrete_file)
                elif "constraint" == key:
                    output_inst, output_opt = call_relevance_synthesis(
                        reflection,
                        topic=topic,
                        use_case=use_case,
                        layer=layer,
                        skip_conn=sk_conn,
                        skill=s,
                        start_ins=start_inst,
                        instr=input_inst,
                        opts=input_opt,
                        direction=key,
                        choice_type=choice_type,
                        len_token=len_token,
                    )
                    write_json(output_inst, output_opt, syn_const_file)
                if len(output_inst) != 0:
                    ds = save_config_info_data(
                        ds, layer, "", key, s, output_inst, output_opt, use_case
                    )
                    write_json(output_inst, output_opt, syn_all_file)
                    if "implicatures" in use_case:
                        output_inst = (
                            output_inst.split("Speaker 2")[0]
                            .strip()
                            .split("Speaker 1")[1]
                            .strip()
                        )
                    if "temporal" in use_case:
                        output_inst = output_inst.split(
                            " Between what times could they have gone? \nWe know that: "
                        )[0].strip()
                    mixed_meta_path_synthesis(
                        reflection,
                        ds,
                        write_json,
                        ex_kg,
                        persona_hub,
                        use_case,
                        num_triples,
                        start_inst,
                        output_inst,
                        output_opt,
                        choice_type,
                        cond_list,
                        layer + 1,
                        r_depth,
                        d_depth,
                        sk_conn,
                        syn_all_file,
                        syn_diver_file,
                        syn_reason_file,
                        syn_concrete_file,
                        syn_const_file,
                        len_token,
                        key,
                    )
    if layer <= d_depth:
        cur_direction = "diversity"
        if persona_hub:
            if os.path.exists("./persona_samples.json"):
                persona_list = loading_persona_file("./persona_samples.json")
            else:
                persona_dataset = load_dataset(
                    "proj-persona/PersonaHub", data_files="persona.jsonl"
                )["train"]
                persona_list = sample_save_persona_hub(
                    persona_dataset, K=5, category=use_case, s_thresold=0.75
                )
            for persona in persona_list:
                persona = persona.strip()
                output_inst, output_opt = call_diversity_synthesis(
                    reflection,
                    input_inst,
                    use_case,
                    choice_type,
                    persona,
                    len_token,
                    topic,
                )
                write_json(output_inst, output_opt, syn_diver_file)
                if len(output_inst) != 0:
                    ds = save_config_info_data(
                        ds, layer, persona, "", "", output_inst, output_opt, use_case
                    )
                    write_json(output_inst, output_opt, syn_all_file)
                    if "implicatures" in use_case:
                        output_inst = (
                            output_inst.split("Speaker 2")[0]
                            .strip()
                            .split("Speaker 1")[1]
                            .strip()
                        )
                    if "temporal" in use_case:
                        output_inst = output_inst.split(
                            " Between what times could they have gone? \nWe know that: "
                        )[0].strip()
                    mixed_meta_path_synthesis(
                        reflection,
                        ds,
                        write_json,
                        ex_kg,
                        persona_hub,
                        use_case,
                        num_triples,
                        start_inst,
                        output_inst,
                        output_opt,
                        choice_type,
                        cond_list,
                        layer + 1,
                        r_depth,
                        d_depth,
                        sk_conn,
                        syn_all_file,
                        syn_diver_file,
                        syn_reason_file,
                        syn_concrete_file,
                        syn_const_file,
                        len_token,
                        cur_direction,
                    )

        else:
            output_inst, output_opt = call_diversity_synthesis(
                reflection, input_inst, use_case, choice_type, "", len_token, topic
            )
            write_json(output_inst, output_opt, syn_diver_file)
            if len(output_inst) != 0:
                ds = save_config_info_data(
                    ds, layer, "", "", "", output_inst, output_opt, use_case
                )
                write_json(output_inst, output_opt, syn_all_file)
                if "implicatures" in use_case:
                    output_inst = (
                        output_inst.split("Speaker 2")[0]
                        .strip()
                        .split("Speaker 1")[1]
                        .strip()
                    )
                if "temporal" in use_case:
                    output_inst = output_inst.split(
                        " Between what times could they have gone? \nWe know that: "
                    )[0].strip()
                mixed_meta_path_synthesis(
                    reflection,
                    ds,
                    write_json,
                    ex_kg,
                    persona_hub,
                    use_case,
                    num_triples,
                    start_inst,
                    output_inst,
                    output_opt,
                    choice_type,
                    cond_list,
                    layer + 1,
                    r_depth,
                    d_depth,
                    sk_conn,
                    syn_all_file,
                    syn_diver_file,
                    syn_reason_file,
                    syn_concrete_file,
                    syn_const_file,
                    len_token,
                    cur_direction,
                )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--choice_type",
        type=str,
        default="multi_choice",
        help="multi_choice, binary_choice or null",
    )
    parser.add_argument(
        "--seed_related_dataset", type=str, default="TheFinAI/flare-cfa", help=""
    )
    parser.add_argument("--len_token", type=int, default=500, help="")
    parser.add_argument("--r_depth", type=int, default=2, help="")
    parser.add_argument("--d_depth", type=int, default=2, help="")
    parser.add_argument("--sk_conn", type=int, default=1, help="")
    parser.add_argument("--num_triples", type=int, default=2, help="")
    parser.add_argument("--use_case", type=str, default="finance", help="")
    parser.add_argument("--benchmark", type=str, default="finance", help="")
    parser.add_argument("--ex_kg", type=bool, default=True, help="")
    parser.add_argument("--persona_hub", type=bool, default=True, help="")
    parser.add_argument("--reflection", type=bool, default=False, help="")
    args = parser.parse_args()

    choice_type = args.choice_type
    seed_related_dataset = args.seed_related_dataset
    len_token = args.len_token
    r_depth = args.r_depth
    d_depth = args.d_depth
    sk_conn = args.sk_conn
    num_triples = args.num_triples
    use_case = args.use_case
    ex_kg = args.ex_kg
    benchmark = args.benchmark
    persona_hub = args.persona_hub
    reflection = args.reflection
    cond_list = ["reasoning", "concrete", "constraint"]

    if "BIG-Bench" == benchmark:
        if "implicatures" in seed_related_dataset:
            new_inst, new_res = load_implicature_seed(seed_related_dataset)
        elif "causal" in seed_related_dataset:
            new_inst, new_res = load_casual_seed(seed_related_dataset)
        elif (
            "code" in seed_related_dataset
            or "temporal" in seed_related_dataset
            or "math" in seed_related_dataset
        ):
            new_inst, new_res = load_code_seed(seed_related_dataset)
        else:
            new_inst, new_res = [], []
    elif "mmlu" == benchmark or "gsm8k" == benchmark or "truth" == benchmark:
        new_inst, new_res = load_mmlu_seed(seed_related_dataset, use_case)
    elif "arc" == benchmark:
        new_inst, new_res = load_arc_seed(seed_related_dataset, use_case)
    elif "finance" == benchmark:
        new_inst, new_res = load_fin_seed(
            seed_related_dataset, seed=42, num_samples_syn=6
        )
    elif "health" == benchmark:
        new_inst, new_res = load_health_seed(
            seed_related_dataset, seed=42, num_samples_syn=6, num_sample_test=1000
        )
    elif "contract_qa" == benchmark:
        new_inst, new_res = load_legal_seed(
            seed_related_dataset, name=benchmark, num_samples_syn=6
        )
    else:
        raise Exception("no implementation loading the datasets!")

    # init write function
    if "cause" in use_case:
        write_json = write_json_ce
    else:
        write_json = write_json_general

    # save synthetic data
    dirs = "./synthesis_data_" + use_case + "/"
    syn_const_file, syn_concrete_file, syn_reason_file, syn_diver_file, syn_all_file = (
        save_path(dirs)
    )
    ds = initialize_ds()

    # start to synthesis
    for idx in range(len(new_inst)):
        inst = new_inst[idx]
        opt = ""
        if len(choice_type):
            opt = new_res[idx]
        mixed_meta_path_synthesis(
            reflection,
            ds,
            write_json,
            ex_kg,
            persona_hub,
            use_case,
            num_triples,
            inst,
            inst,
            opt,
            choice_type=choice_type,
            cond_list=cond_list,
            layer=1,
            r_depth=r_depth,
            d_depth=d_depth,
            sk_conn=sk_conn,
            syn_all_file=syn_all_file,
            syn_diver_file=syn_diver_file,
            syn_reason_file=syn_reason_file,
            syn_concrete_file=syn_concrete_file,
            syn_const_file=syn_const_file,
            len_token=len_token,
            last_direction="",
        )

    print("finish the synthesis!")
    syn_dataset = make_synthetic_dataset(ds)
    write_dataset_to_json(syn_dataset)
    print("save all synthesis in disk!")
