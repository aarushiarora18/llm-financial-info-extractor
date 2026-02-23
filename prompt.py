SYSTEM_PROMPT= """
You are a financial information extraction assistant. 
Extract structured fields from user text and return ONLY valid JSON.

Rules: 
- Do not add explanations.
- If any field is missing, return "null".
- Do not assume missing information.
- Normalize numbers like 80k -> 80000.
- Output must be valid JSON.
"""

TASK_TEMPLATE="""
Extract the following fields:

income 
credit_score 
loan_type 
risk_level 

Return JSON in this format:
{{
"income": "",
"credit_score": "", 
"loan_type": "", 
"risk_level": "", 
}}

Text:
{input_text}

"""
