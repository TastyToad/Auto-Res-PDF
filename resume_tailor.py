#!/usr/bin/env python3
import os
import re
import json
import anthropic

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

os.environ["G_MESSAGES_DEBUG"] = "none"
os.environ["GLIB_LOG_LEVEL"] = "none"

client = anthropic.Anthropic(api_key='')  # keep your key here for testing, set as environment variable if actually being used 

def load_master_json():
    try:
        with open('john_doe.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: 'john_doe.json' not found.")
        return None  

def load_returned_json():
    try:
        with open('returned_resume.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: 'returned_resume.json' not found. Run send_receive_prompt first.")
        return None

def send_receive_prompt(resume_data, job_description):
    print("Sending to Claude...")
    
    prompt = f"""You are a resume tailoring assistant. Given the master resume JSON and a job description,
return a tailored version of the resume JSON that highlights the most relevant experience
and skills for this specific job.

CRITICAL: Respond with ONLY a valid JSON object. No markdown, no code fences, no explanation, no text before or after the JSON.

Master Resume JSON:
{json.dumps(resume_data, indent=2)}

Job Description:
{job_description}
"""

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=8000,
        messages=[{"role": "user", "content": prompt}]
    )

    response_text = message.content[0].text.strip()

    # 
    # handles ```json, ```JSON, ``` json, ```, etc.
    fence_match = re.search(r'```[a-zA-Z\s]*\n?([\s\S]*?)\n?```', response_text)
    if fence_match:
        response_text = fence_match.group(1).strip()

    #  if no leading brace, find the first { and last }
    #  slice to just that range, discarding any preamble/postamble text
    if not response_text.startswith('{'):
        start = response_text.find('{')
        end   = response_text.rfind('}')
        if start != -1 and end != -1 and end > start:
            response_text = response_text[start:end + 1]

    # check before attempting parse
    if not response_text:
        raise ValueError("Response was empty after stripping. Check Claude's raw output.")
    if not response_text.startswith('{'):
        raise ValueError(f"Could not locate JSON object in response. First 300 chars:\n{response_text[:300]}")

    try:
        tailored_data = json.loads(response_text)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"JSON parse failed: {e}\n"
            f"Problematic text around error (char {e.pos}):\n"
            f"...{response_text[max(0, e.pos-100):e.pos+100]}..."
        )

    with open('returned_resume.json', 'w') as f:
        json.dump(tailored_data, f, indent=2)

    print("Tailored JSON saved as 'returned_resume.json'.")
    return tailored_data

def generate_resume(tailored_data):
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('blank_resume_template.html')
    html_out = template.render(data=tailored_data)

    with open('filled_resume.html', 'w', encoding='utf-8') as f:
        f.write(html_out)
    print("Resume generated as 'filled_resume.html'.")

    HTML(string=html_out).write_pdf("john_doe.json_Resume.pdf")
    print("PDF created successfully!") 






if __name__ == "__main__":  
    job_description = input("Paste the job description and press Enter twice:\n")

    resume_data = load_master_json()
    if resume_data is None:
        exit(1)

    tailored_data = send_receive_prompt(resume_data, job_description)  
    
    generate_resume(tailored_data)  