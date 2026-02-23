import os
import requests
import json
from dotenv import load_dotenv
from prompt import SYSTEM_PROMPT, TASK_TEMPLATE

load_dotenv()
API_KEY= os.getenv("GROQ_API_KEY")

def call_llm(input_text):
    url="https://api.groq.com/openai/v1/chat/completions"
    headers= {
        "Authorization" :f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload={
        "model": "llama-3.1-8b-instant",
        "messages":[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":TASK_TEMPLATE.format(input_text=input_text)},

        ],
        "temperature":0
    }

    response= requests.post(url, headers=headers, json=payload)
    result=response.json()
    if "choices" not in result:
        print("API ERROR:", result)
        return None

    return result["choices"][0]["message"]["content"]

if __name__=="__main__":
    text=input("Enter financial text: ")
    output=call_llm(text)
    if output is None:
        print("No response from model.")
        exit()
    try:
        parsed_output= json.loads(output)
        print("\nParsed JSON\n")
        print(parsed_output)
    except Exception as e:
        print("JSON parsing failed",e)
        print("Raw output:", output)