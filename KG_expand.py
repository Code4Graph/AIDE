from claude_sonnet35_access import *
import re

base_instruction_creator = """A knowledge graph can be represented by a triple [entity1, relation, entity2], which means entity1 has a relationship with entity2. 
\nYou are asked to use the given triples within the <The Given triples></The Given triples> xml tags to perform the following actions:
\n- use your knowledge to explore potential entities included by {}.
\n- entity1 in each triple should be {}.
\n- use the above exploration to create different triples.
\n- the generated triples are different from the given triples.
\nFollow the examples below to generate output within the <Output></Output> xml tags.
\n
\n<Example>
\n<The Given triples> ["code", "has", "if"] </The Given triples>
\n<Output>
\n1. ["code", "includes", "break"]\
\n2. ["code", "has", "if"]\
\n3. ["code", "uses", "while"]</Output>
\n</Example>
\n
\nYou must follow the format of the above example to generate {} triples in <Output> and show me the <Output>.\
\n<The Given triples> {} </The Given triples> 
"""


def expand_kg(triples, num_triples, use_case):
    system = "You are a helpful assistant."
    prompt = base_instruction_creator.format(use_case, use_case, num_triples, triples)
    ans = get_claude_response(system, prompt).lower()
    print("expand kg ans: ", ans)
    if ("<Output>" in ans and "</Output>" in ans) or (
        "<output>" in ans and "</output>" in ans
    ):
        if "<Output>" in ans and "</Output>" in ans:
            res = re.findall("<Output>(.*?)</Output>", ans, re.S)[-1].strip()
        else:
            res = re.findall("<output>(.*?)</output>", ans, re.S)[-1].strip()
    else:
        res = ""
    res = res.split("\n")
    l = []
    for r in res:
        if "[" not in r or "]" not in r:
            continue
        if '"' in r:
            result = re.findall(r'"(.*?)"', r)[-1]
        elif "'" in r:
            result = re.findall(r"\'(.*?)\'", r)[-1]
        else:
            result = r.split(",")[-1].strip()
        l.append(result.lower())
    return l
