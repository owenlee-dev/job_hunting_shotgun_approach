import json
import os
import pprint
import shutil
from datetime import date

from fallback.assets.cover_letters import manager_role
from docx_scribe import convert_docx_to_pdf, find_and_replace

"""
Shotgun approach sucks
@inputs
- Job Title
- Company Name
- Company Location
- Job Description

--> Output Prompt

- Paragraph

@output
- Application Package
"""
current_template = "assets\docx_source\Product_CL_Template.docx"


def gather_job_info():
    with open("job_info.json") as f:
        data = json.load(f)
    return data


def generate_prompt(
    position_title,
    company_name,
    job_description,
    cover_letter_text,
):
    prompt = f"I'm writing a cover letter for the {position_title} position at {company_name}. I need a unique paragraph that stands out and complements my existing cover letter without repeating any points. It strictly must be no more than 40 words and should strongly emphasize my interest in {company_name} and its values or attributes. The tone should be professional yet approachable. For context: - Job Description: {job_description} - Existing Cover Letter (replace <openAI paragraph goes here>): {cover_letter_text} - My motivations: 1) Work in a fast-paced environment 2) Grow with a company 3) Become a long-term asset.Please craft a paragraph that deeply resonates with {company_name} and is distinct from what's already in my cover letter. Furthermore, it should not mention the job description or my career aspirations and should avoid absolute adjectives, like perfect"
    with open("prompt.txt", "w", encoding="utf-8") as f:
        f.write(json.dumps(prompt))


# def generate_app_package():
#   job_info=gather_job_info()
#   prompt=generate_prompt()

# get job info
job_info = gather_job_info()
# use job info to generate prompt
generate_prompt(
    position_title=job_info["position_title"],
    company_name=job_info["company_name"],
    job_description=job_info["job_description"],
    cover_letter_text=manager_role,
)
# use prompt to externally generate a paragraph
paragraph = input("input the linking paragraph:")

# use all of this information to generate an application package
replacements = {
    "<owenTitle>": str(job_info["owen_title"]),
    "<date>": date.today().strftime("%B %d, %Y"),
    "<positionRole>": str(job_info["position_title"]),
    "<positionLocation>": str(job_info["position_location"]),
    "<companyName>": str(job_info["company_name"]),
    "<companyParagraph>": paragraph,
}
find_and_replace(current_template, replacements, "assets/docx_source/temp_doc.docx")

file_name = job_info["employer_name"].replace(" ", "_")
mypath = f"assets/application_packages/{file_name}"

if not os.path.exists(mypath):
    os.makedirs(mypath)

# cover letter

# resume
shutil.copy(
    "assets/docx_source/temp_doc.docx", f"{mypath}/{file_name}_cover_letter.docx"
)
shutil.copy("assets/owen-resume.pdf", f"{mypath}/owen-resume.pdf")
