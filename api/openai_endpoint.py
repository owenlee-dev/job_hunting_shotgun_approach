import openai
from .keys.constants import OPENAI_KEY

# Initialize with your API key
openai.api_key = OPENAI_KEY


def generate_prompt(
    position_title,
    company_name,
    job_description,
    cover_letter_text,
):
    prompt= f"I'm writing a cover letter for the {position_title} position at {company_name}. I need a unique paragraph that stands out and complements my existing cover letter without repeating any points. It strictly must be no more than 40 words and should strongly emphasize my interest in {company_name} and its values or attributes. The tone should be professional yet approachable. For context: - Job Description: {job_description} - Existing Cover Letter (replace <openAI paragraph goes here>): {cover_letter_text} - My motivations: 1) Work in a fast-paced environment 2) Grow with a company 3) Become a long-term asset.Please craft a paragraph that deeply resonates with {company_name} and is distinct from what's already in my cover letter. Furthermore, it should not mention the job description or my career aspirations and should avoid absolute adjectives, like perfect"
    with open ('prompts.txt','a', encoding="utf-8") as f:
        f.write(prompt+ "\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    return prompt

# Function takes in company and owen information and outputs a personalized paragraph
def get_personalized_paragraph(
    is_live, position_title, company_name, job_description, cover_letter_text
):
    if is_live:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": generate_prompt(
                        position_title, company_name, job_description, cover_letter_text
                    ),
                }
            ],
            temperature=0,
            max_tokens=200,
        )
        return str(response["choices"][0]["message"]["content"])
    else:
        return "Eiusmod aliquip pariatur ad cillum id cillum ut cupidatat commodo reprehenderit in excepteur. Sint esse mollit id voluptate ad qui exercitation. Amet non ipsum irure nulla Lorem. Nostrud cillum irure qui officia sit irure id. Fugiat ullamco mollit consectetur exercitation laborum qui sint est commodo ea sunt sit."
