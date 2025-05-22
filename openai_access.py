from openai import OpenAI
import openai
import time
import requests

client = OpenAI(api_key="your key")


def get_oai_completion(system, prompt):
    response = client.chat.completions.create(
        model="gpt-4o-2024-05-13",
        # model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        temperature=1,
        max_tokens=2048,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
    )
    res = response.choices[0].message.content
    gpt_output = res
    return gpt_output


def call_chatgpt2(ins):
    success = False
    re_try_count = 15
    ans = ""
    while not success and re_try_count >= 0:
        re_try_count -= 1
        try:
            ans = get_oai_completion(ins)
            success = True
        except:
            time.sleep(5)
            print("retry for sample:", ins)
    return ans


def call_chatgpt(system, ins):
    ans = get_oai_completion(system, ins)
    return ans
