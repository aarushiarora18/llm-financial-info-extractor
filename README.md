# LLM Financial Information Extractor

A lightweight AI pipeline that extracts structured financial data from unstructured text using prompt engineering and Large Language Models (LLMs).

---

## Overview

This project converts raw financial notes into structured JSON output.  
It demonstrates core AI engineering concepts such as:

- Prompt design
- LLM API integration
- Structured JSON generation
- Defensive parsing and error handling

The extractor identifies fields like:

- Income
- Credit Score
- Loan Type
- Risk Level

---

## Pipeline Flow

User Input Text  
→ Prompt Template + System Instructions  
→ Groq LLM API  
→ Structured JSON Response  
→ Python JSON Parsing  
→ Usable Data

---

## Tech Stack

- Python
- Groq API (Llama 3.1 models)
- Requests
- python-dotenv
- JSON parsing

---

## Project Structure

financial-extractor/

- extractor.py  → Main pipeline script  
- prompt.py     → System and task prompts  
- requirements.txt  
- README.md  

---

## Example

Input:

Client earns 40k monthly. Credit Score 800. Wants personal loan.

Output:

{
  "income": 40000,
  "credit_score": 800,
  "loan_type": "personal",
  "risk_level": null
}

---

## Setup

1. Clone the repository
2. Install dependencies:

pip install -r requirements.txt

3. Create a .env file:

GROQ_API_KEY=your_api_key_here

4. Run the extractor:

python extractor.py

---

## Notes

- API keys are excluded using .gitignore
- Output is parsed into Python dictionaries for programmatic use
- Designed as a foundational AI engineering mini-project

---

## Future Improvements

- Automatic JSON cleaning for inconsistent outputs
- Batch processing support
- Simple UI integration
  
