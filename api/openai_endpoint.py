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
    # f"I am writing a cover letter for an open {position_title} at {company_name} and I need your help in crafting a specific paragraph. I have written the rest of the cover letter, but am missing a personalized paragraph that will tie together my skill set, my interest in this specific position and why I want to work at the company. I am going to give you some information to help craft this paragraph, you should not use all of the information but enough to make a tasteful paragraph.\nJob Description: {job_description}\nRest of cover letter: {cover_letter_text}\nMy Motivations: a) work in a fast paced environment b) grow with a company c) become a long term asset to the company\n Other instructions: The paragraph must be 2 sentences, the tone should be formal, yet approachable, it should not mention my career aspirations or the job posting or description or the work benefits and values, it should not be too wordy (try and avoid too many adjectives), Please only return the paragraph with no comments from chatgpt, it should primarily be the custom paragraph connecting the cover letter to the companies mission, I dont have much experience so don't make it sound like I have extensive knowledge"
    return f"I am writing a cover letter for an open {position_title} at {company_name} and I need your help in crafting a specific paragraph. I have written the rest of the cover letter, but am missing a personalized paragraph that will tie together my skill set, my interest in this specific position and why I want to work at the company. I am going to give you some information to help craft this paragraph, you should not use all of the information but enough to make a tasteful paragraph.\nJob Description: {job_description}\nRest of cover letter: {cover_letter_text}\nMy Interests in the job: a) work in a fast paced environment b) grow with a company c) become a long term asset to the company\n Form: The paragraph must be 2 sentences, the first expressing why I am interested in the company and the second expressing my ability and enthusiasm to contribute. Also, please just return the paragraph and make it not too wordy, avoid flashy adjectives and keep it under 45 words"


# Function takes in company and owen information and outputs a personalized paragraph
def get_personalized_paragraph(
    position_title, company_name, job_description, cover_letter_text
):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": generate_prompt(
                    position_title, company_name, job_description, cover_letter_text
                ),
            }
        ],
    )
    return response
