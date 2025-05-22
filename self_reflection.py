from claude_sonnet35_access import *
from few_shot import *
import re
import copy

base_instruction_quality = """I want you to act as a grader to rate the quality of <The Given Prompt> with domain expertise. 
                            \nYou should give an overall score on a scale of 1 to 10, where a higher score indicates the <The Given Prompt> has a sufficient challenge with high quality. 
                            \nYou must just give <Score>. 
                            \nFollow the examples and format below to analyze and rate <The Given Instruction> within <Score></Score> xml tags.
                            \n{}
                            \n{}
                            """

base_instruction_correctness = """I want you to act as a grader to check if there exists an answer for <The Given Prompt>. 
                                \nGiven <The Given Prompt>, you should think step by step to search the answer for <The Given Prompt>. 
                                \nYou should response Yes if <The Given Prompt> has an answer. Otherwise you response No. 
                                \nYou should not care about if <The Given Prompt> is correct or not. 
                                \nYou must just give an answer within <Answer></Answer> xml tags. 
                                \nFollow the examples and format below to analyze <The Given Instruction>. 
                                \n
                                \n<Example>
                                \n<The Given Prompt> 1+1=? </The Given Prompt>
                                \n<Thinking> we can compute 1+1 with the solution 1+1=2, and hence the given prompt is correct. </Thinking>
                                \n<Answer> Yes </Answer> 
                                \n</Example>
                                
                                \n<Example>
                                \n<The Given Prompt> Given a=2 and f(x)=2a+b+x, how about the answer f(5)? </The Given Prompt>
                                \n<Thinking> For computing the f(5), we can have f(5)=2*2+b+5, which is equal to f(5)=9+b. However, we don;t know the value of b. Therefore, we cannot get solution and the given prompt is incorrect. </Thinking>
                                \n<Answer> No </Answer> 
                                \n</Example>
                                
                                \n{}
                                """

base_instruction_diversity = """ I want you to act as a domain expert to rate the diversity of <The Given Prompt> comparing with <The Original Prompt>. 
                            \nYou should give an overall score on a scale of 1 to 10, where a higher score indicates the <The Given Prompt> is more different from <The Original Prompt>. 
                            \nYou must just give score within the <Score></Score> xml tags. 
                            \nFollow the examples and format below to analyze and rate <The Given Instruction> within the <Score></Score> xml tags. 
                            
                            \n{}
                            
                            \n{}
                            """

base_instruction_choice = """I want you to act as an solver of questions. 
                           \nThink step by step 
                           \nGiven <The Given Prompt>, you should use your knowledge to check if the answer of <The Given Prompt> is in the <Choices>. 
                           \nYour <Response> is Yes when the answer of <The Given Prompt> is in the <Choices>. when the answer of <The Given Prompt> is not in the <Choices>, your <Response> is No.
                           \nYou must just give response within the <Response></Response> xml tags. 
                           \nFollow the examples and format below to analyze and check if the answer of <The Given Prompt> is in <Choices> or not.
                           \n{}
                           \n{}
                           """

base_instruction_ce_reflect = """I want you to act as an solver of causes.\
                           \nThink step by step.\
                           \nGiven <The Given Prompt>, you should use your knowledge to check if <The Given Prompt> is the cause of the effect in the <Choices>.\
                           \nYour <Response> is Yes when the answer of <The Given Prompt> is in the <Choices>. when the answer of <The Given Prompt> is not in the <Choices>, your <Response> is No.\
                           \nYou must just give response within the <Response></Response> xml tags. 
                           \nFollow the examples and format below to analyze and check if the answer of <The Given Prompt> is in <Choices> or not.\
                           \n{}\
                           \n
                           \n{}
                           """

base_instruction_implicature = """I want you to act as an solver of implicature.\
                           \nWith <The Given Prompt>, you should think step by step and predict whether Speaker 2 explicitly or implicitly answers to Speaker 1.\
                           \nOnce the Speaker 2 implicitly answers to Speaker 1 or the Speaker 2 explicitly answers to Speaker 1, your prediction should be 'Yes'. Otherwise, your prediction should be 'No'.\
                           \nExtract the option with 'correct.' from the <Choices> and think about if the extracted option aligns with the prediction.
                           \nOutput 'Yes' in the <Response> if the prediction aligns with the extracted option in the <Choices>. Otherwise, output 'No' in the <Response>.\
                           \nYou must just give response within the <Response></Response> xml tags. 
                           \nFollow the below format to show <Response>.\
                           \n{}\
                           \n
                           \n{}
                           """

base_instruction_relevance = """\nI want you to act as a domain expert to rate the relevance of <The Given Prompt> and <The Original Prompt>.
                            \nYou should give an overall score on a scale of 1 to 10, where a higher score indicates the <The Given Prompt> is more relevant to <The Original Prompt>.
                            \nYou must just give <Score> without any other reasons within the <Score></Score> xml tags.
                            \nFollow the examples below to analyze and rate relevance of <The Given Instruction> and <The Original Prompt> in <Score>.
                            \n{}
                            \n{}
                            """


def check_sol_choice(inst, opt, use_case):
    few_shot = ""
    if "code" in use_case or "programming" in use_case or "implementation" in use_case:
        few_shot = solution_choice_code
        system = "\nYou are an expert to check if the solution of <The Given Prompt> is in the <Choices>."
        prompt = base_instruction_choice.format(
            few_shot,
            "Now, show me the answer in the <Response> through checking if the solution of <The Given Prompt> is in the <Choices>.",
        )
    elif "cause" in use_case:
        few_shot = solution_choice_effect
        system = "\nYou are an expert to check if the cause of <The Given Prompt> has correct effect in the <Choices>."
        prompt = base_instruction_ce_reflect.format(
            few_shot,
            "Now, show me the answer in the <Response> through checking if <The Given Prompt> is the cause of the effect in the <Choices>.",
        )
    elif "implicature" in use_case:
        few_shot = solution_choice_implicature
        system = "\nYou are an expert of understanding implicatures which are the phenomenon whereby a person means to convey a message that is not explicitly expressed."
        prompt = base_instruction_implicature.format(
            few_shot, "Now, show me the answer in the <Response>"
        )
    elif "temporal" in use_case:
        few_shot = solution_choice_temporal
        system = "\nYou are an expert to check if the solution of <The Given Prompt> is in the <Choices>."
        prompt = base_instruction_choice.format(
            few_shot,
            "Now, show me the answer in the <Response> through checking if the solution of <The Given Prompt> is in the <Choices>.",
        )
    elif "math" in use_case or "bio" in use_case:
        few_shot = solution_choice_math
        system = "\nYou are an expert to check if the solution of <The Given Prompt> is in the <Choices>."
        prompt = base_instruction_choice.format(
            few_shot,
            "Now, show me the answer in the <Response> through checking if the solution of <The Given Prompt> is in the <Choices>.",
        )
    elif "computer" in use_case:
        few_shot = solution_choice_computer
        system = "\nYou are an expert to check if the solution of <The Given Prompt> is in the <Choices>."
        prompt = base_instruction_choice.format(
            few_shot,
            "Now, show me the answer in the <Response> through checking if the solution of <The Given Prompt> is in the <Choices>.",
        )
    elif "philosophy" in use_case:
        few_shot = solution_choice_philosophy
        system = "\nYou are an expert to check if the solution of <The Given Prompt> is in the <Choices>."
        prompt = base_instruction_choice.format(
            few_shot,
            "Now, show me the answer in the <Response> through checking if the solution of <The Given Prompt> is in the <Choices>.",
        )
    elif "marketing" in use_case:
        few_shot = solution_choice_marketing
        system = "\nYou are an expert to check if the solution of <The Given Prompt> is in the <Choices>."
        prompt = base_instruction_choice.format(
            few_shot,
            "Now, show me the answer in the <Response> through checking if the solution of <The Given Prompt> is in the <Choices>.",
        )
    elif "truth" in use_case:
        few_shot = solution_choice_truth
        system = "\nYou are an expert to check if the solution of <The Given Prompt> is in the <Choices>."
        prompt = base_instruction_choice.format(
            few_shot,
            "Now, show me the answer in the <Response> through checking if the solution of <The Given Prompt> is in the <Choices>.",
        )
    else:
        system = "\nYou are an expert of understanding implicatures which are the phenomenon whereby a person means to convey a message that is not explicitly expressed."
        prompt = base_instruction_implicature.format(
            few_shot, "Now, show me the answer in the <Response>"
        )

    prompt += """\nYour output should follow the format of examples and show the answer within the <Response><Response> xml tags."""
    prompt += "\n<The Given Prompt> {} </The Given Prompt>".format(inst)
    prompt += "\n<Choices> {} </Choices>".format(opt)
    ret = get_claude_response(system, prompt)
    if ("<Response>" in ret and "</Response>" in ret) or (
        "<response>" in ret and "</response>" in ret
    ):
        if "<Response>" in ret and "</Response>" in ret:
            ans = re.findall("<Response>(.*?)</Response>", ret, re.S)[-1].strip()
        else:
            ans = re.findall("<response>(.*?)</response>", ret, re.S)[-1].strip()
    else:
        ans = ""
    if "Yes" in ans:
        return True
    return False


def check_diversity(inst, pre_inst, use_case):
    few_shot = ""
    if "code" in use_case or "programming" in use_case or "implementation" in use_case:
        few_shot = check_code_diversity
    if "cause" in use_case:
        few_shot = check_cause_diversity
    if "implicature" in use_case:
        inst = inst.split("Speaker 2:")[0].strip().split("Speaker 1:")[1].strip()
        few_shot = check_imp_diversity
    if "temporal" in use_case:
        inst = inst.split(" Between what times could they have gone? \nWe know that: ")[
            0
        ].strip()
        few_shot = check_tmp_diversity
    if "math" in use_case or "bio" in use_case:
        few_shot = check_math_diversity
    if "computer" in use_case:
        few_shot = check_computer_diversity
    if "philosophy" in use_case:
        few_shot = check_philosophy_diversity
    if "marketing" in use_case:
        few_shot = check_marketing_diversity
    if "truth" in use_case:
        few_shot = check_truth_diversity
    system = "You are a domain expert to rate the diversity of <The Given Prompt> comparing with <The Original Prompt>."
    prompt = base_instruction_diversity.format(
        few_shot,
        "Now, only show me the <Score> of diversity by comparing <The Given Prompt> with <The Original Prompt>.",
    )
    prompt += """\nYour output should follow the format of examples, which means preserve the same format and show the score within <Score></Score> xml tags."""
    prompt += "\n<The Original Prompt> {} </The Original Prompt>".format(pre_inst)
    prompt += "\n<The Given Prompt> {} </The Given Prompt>".format(inst)
    ret = get_claude_response(system, prompt)
    if ("<Score>" in ret and "</Score>" in ret) or (
        "<score>" in ret and "</score>" in ret
    ):
        if "<Score>" in ret and "</Score>" in ret:
            ans = re.findall("<Score>(.*?)</Score>", ret, re.S)[-1].strip()
        else:
            ans = re.findall("<score>(.*?)</score>", ret, re.S)[-1].strip()
    else:
        ans = ""
    grade = re.findall(r"\d+", ans)
    print("grade diversity: ", grade)
    if len(grade) > 0:
        return int(grade[0])
    else:
        return 0


def check_relevance(inst, pre_inst, use_case):
    few_shot = ""
    if "code" in use_case or "programming" in use_case or "implementation" in use_case:
        few_shot = relevance_code
    elif "cause" in use_case:
        few_shot = relevance_cause
    elif "implicature" in use_case:
        inst = inst.split("Speaker 2:")[0].strip().split("Speaker 1:")[1].strip()
        few_shot = relevance_implicature
    elif "temporal" in use_case:
        inst = inst.split(" Between what times could they have gone? \nWe know that: ")[
            0
        ].strip()
        few_shot = relevance_tmp
    elif "math" in use_case or "bio" in use_case:
        few_shot = relevance_math
    elif "computer" in use_case:
        few_shot = relevance_computer
    elif "philosophy" in use_case:
        few_shot = relevance_philosophy
    elif "marketing" in use_case:
        few_shot = relevance_marketing
    elif "truth" in use_case:
        few_shot = relevance_truth
    system = "\nYou are a domain expert to rate the relevance of <The Given Prompt> and <The Original Prompt>."
    prompt = base_instruction_relevance.format(
        few_shot,
        "Now, show me the <Score> of relevance by comparing <The Given Prompt> with <The Original Prompt>.",
    )
    prompt += """\nYour output should follow the format of examples, which means preserve the same format and show the score within <Score></Score> xml tags."""
    prompt += "\n<The Original Prompt> {} </The Original Prompt>".format(pre_inst)
    prompt += "\n<The Given Prompt> {} </The Given Prompt>".format(inst)
    ret = get_claude_response(system, prompt)
    print("ret: ", ret)
    if ("<Score>" in ret and "</Score>" in ret) or (
        "<score>" in ret and "</score>" in ret
    ):
        if "<Score>" in ret and "</Score>" in ret:
            ans = re.findall("<Score>(.*?)</Score>", ret, re.S)[-1].strip()
        else:
            ans = re.findall("<score>(.*?)</score>", ret, re.S)[-1].strip()
    else:
        ans = ""
    grade = re.findall(r"\d+", ans)
    print("relevant grade: ", grade)
    if len(grade) > 0:
        return int(grade[0])
    else:
        return 0


base_instruction_enhance = """{}
                              \nUsing <Pre-prompt> and <Reflection>, you are asked to rewrite <The Given Prompt>.
                              \nGenerate <Improved Prompt> that reflect the insights and suggestions from the reflection.
                              \n<Pre-prompt> {} </Pre-prompt>
                              \n<The Given Prompt> {} </The Given Prompt>
                              \n<Reflection> {} </Reflection>
                              {}
                           """

follow_example_instruction = """\nFollow the format of examples to rewrite <The Given Prompt> using <Pre-prompt> and <Reflection>.
                                {}"""


def improve(inst, pre_inst, reflection, use_case):
    save_inst = copy.deepcopy(inst)
    few_shot = ""
    system = "You are a professional data generator"
    if "code" in use_case or "programming" in use_case or "implementation" in use_case:
        few_shot = enhance_code
        suffix = """Must only generate simple python code within the <Improved Prompt></Improved Prompt> xml tags. \r\n """
    if "cause" in use_case:
        few_shot = enhance_cause
        suffix = ""
    if "implicature" in use_case:
        few_shot = enhance_implicature
        inst = inst.split("Speaker 2:")[0].strip().split("Speaker 1:")[1].strip()
        suffix = """Alternately generate a random number either 0 or 1.
                    \nIf the random number is 1, You must write implicature to response <Improved Prompt> within the <Response></Response> xml tags. 
                    \nIf the random number is 0, you must outputs irrelevant contents with several words within the <Response></Response> xml tags.
                    """
    if "temporal" in use_case:
        few_shot = (
            "\nIn the <Response>, You shouldn't show the relationship between the entities from <Improved Prompt>."
            + enhance_temporal
        )
        inst = inst.split(" Between what times could they have gone? \nWe know that: ")[
            0
        ].strip()
        suffix = ""
    if "math" in use_case or "bio" in use_case:
        few_shot = enhance_math
        suffix = """Must only generate a math problem within the <Improved Prompt></Improved Prompt> xml tags. \r\n """
    if "computer" in use_case:
        few_shot = enhance_computer
        suffix = """Must only generate a computer science problem within the <Improved Prompt></Improved Prompt> xml tags. \r\n """
    if "philosophy" in use_case:
        few_shot = enhance_philosophy
        suffix = """Must only generate a philosophy problem within the <Improved Prompt></Improved Prompt> xml tags. \r\n """
    if "marketing" in use_case:
        few_shot = enhance_marketing
        suffix = """Must only generate a marketing problem within the <Improved Prompt></Improved Prompt> xml tags. \r\n """
    if "truth" in use_case:
        few_shot = enhance_truth
        suffix = """Must only generate a common sense question within the <Improved Prompt></Improved Prompt> xml tags. \r\n """
    follow_instruction = follow_example_instruction.format(few_shot)
    prompt = base_instruction_enhance.format(
        suffix, pre_inst, inst, reflection, follow_instruction
    )
    prompt += """\nYour output should have the same format of examples, which must output within <Improved Prompt></Improved Prompt> and <Response></Response> xml tags."""
    ret = get_claude_response(system, prompt)
    print("ret: ", ret)
    if ("<Response>" in ret and "</Response>" in ret) or (
        "<response>" in ret and "</response>" in ret
    ):
        if "<Response>" in ret and "</Response>" in ret:
            llm_response = re.findall("<Response>(.*?)</Response>", ret, re.S)[
                -1
            ].strip()
        else:
            llm_response = re.findall("<response>(.*?)</response>", ret, re.S)[
                -1
            ].strip()
    else:
        llm_response = ""

    if ("<Improved Prompt>" in ret and "</Improved Prompt>" in ret) or (
        "<improved prompt>" in ret and "</improved prompt>" in ret
    ):
        ans = re.findall("<Improved Prompt>(.*?)</Improved Prompt>", ret, re.S)[
            -1
        ].strip()
    else:
        ans = re.findall("<improved prompt>(.*?)</improved prompt>", ret, re.S)[
            -1
        ].strip()
    if "implicature" in use_case:
        if len(ans) == 0:
            ans = save_inst
        ans = (
            "Speaker 1: "
            + "'"
            + ans.strip()
            + "'"
            + " Speaker 2: "
            + "'"
            + llm_response.strip()
            + "'"
        )
    elif "temporal" in use_case:
        if len(ans) == 0:
            ans = save_inst
        ans = (
            ans.strip()
            + " Between what times could they have gone? \nWe know that: "
            + llm_response.strip()
        )
    else:
        ans = ans.strip()
    return ans


def self_reflection(inst, pre_inst, use_case, relevance, diversity):
    reflection = ""
    if relevance <= 4:
        reflection += "<The Given Prompt> is not relevant to <Pre-prompt>, please generate the <Improved Prompt> using the <Pre-prompt>."
    if diversity <= 4:
        reflection += "<The Given Prompt> is similar to the <Pre-prompt>, please generate the <Improved Prompt> with more diversity using the <Pre-prompt>."
    improved_prompt = improve(inst, pre_inst, reflection, use_case)
    return improved_prompt
