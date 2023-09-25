import openai
from keys.constants import OPENAI_KEY

# Initialize with your API key
openai.api_key = OPENAI_KEY



def get_personalized_paragraph(position_title, company_name, job_description, company_information, cover_letter_text):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=
    f"I am writing a cover letter for an open {position_title} at {company_} and I need your help in crafting a specific paragraph. I have written the rest of the cover letter, but am missing a personalized paragraph that will tie together my skill set, my interest in this specific position and why I want to work at the company. I am going to give you some information to help craft this paragraph, you should not use all of the information but enough to make a tasteful paragraph.\nJob Description: {job_description}\n Company information: {company_information}\nRest of cover letter: {cover_letter_text}\nMy Motivations: a) work in a fast paced environment b) grow with a company c) become a long term asset to the company\n Other instructions: The paragraph should be between 300 and 350 characters, the tone should be formal, yet approachable, it should not mention my career aspirations or the job posting or description, and it should not be too wordy (try and avoid too many adjectives)",
    max_tokens=85
)