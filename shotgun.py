import json
import os
import shutil
from datetime import date
from pprint import pprint

from docx2pdf import convert

from api.jsearch_endpoint import get_jobs
from api.openai_endpoint import get_personalized_paragraph
from assets.cover_letters import *
from assets.settings import *
from docx_scribe import convert_docx_to_pdf, find_and_replace
from filter import filter_job_listings


def list_to_bullet_points(items):
    bullet = "\u2022"  # Unicode character for a bullet point
    return "\n".join(bullet + " " + item.replace("<br>", "\n") for item in items)


"""
Strategy:
1. Get list of jobs from jsearch api
2. Filter jobs
3. loop through filtered jobs
  4. Generate custom paragraph from job info using openai api
  5. Fill in cover letters with job info and openai paragraph
  6. Zip cover letter, resume and application link into a folder
7. Profit
"""

# Cover Letter Template
# TODO how to select the appropriate one of the 5, another openai call?
current_template = "assets/docx_source/Product_CL_Template.docx"
job_info_template = "assets/docx_source/job_info_template.docx"
num_applications = 0
# 1
job_listings = get_jobs(job_search_prompt, is_live)

# 2
jobs_filtered = filter_job_listings(job_listings)

# 3
# print("\n\n")
# for listing in jobs_filtered:
#     print(listing.employer_name)

for listing in jobs_filtered:
    num_applications += 1
    # 4
    paragraph = get_personalized_paragraph(
        is_live,
        company_name=listing.employer_name.title(),
        position_title=listing.job_job_title.title(),
        job_description=listing.job_description,
        cover_letter_text=product_role.title(),
    )
    # 5
    replacements = {
        "<owenTitle>": str(listing.job_job_title.title()),
        "<date>": date.today().strftime("%B %d, %Y"),
        "<positionRole>": str(listing.job_job_title.title()),
        "<positionLocation>": listing.job_city + ", " + listing.job_country,
        "<companyName>": str(listing.employer_name.title()),
        "<companyParagraph>": paragraph,
    }
    find_and_replace(current_template, replacements, "assets/docx_source/temp_doc.docx")
    # 6
    file_name = listing.employer_name.replace(" ", "_")
    mypath = f"assets/application_packages/{file_name}"

    if not os.path.exists(mypath):
        os.makedirs(mypath)

    # cover letter
    convert_docx_to_pdf(
        "assets/docx_source/temp_doc.docx",
        f"{mypath}/{file_name}_cover_letter.pdf",
    )

    # resume
    shutil.copy("assets/owen-resume.pdf", f"{mypath}/owen-resume.pdf")

    linkedin_link = "None"
    # get linkedin link
    for option in listing.apply_options:
        if option["publisher"] == "LinkedIn":
            linkedin_link = option["apply_link"]
            break

    # Job info
    replacements = {
        "<app_number>": str(num_applications),
        "<company_name>": str(listing.employer_name),
        "<job_title>": str(listing.job_title),
        "<job_location>": listing.job_city + ", " + listing.job_country,
        "<company_type>": str(listing.employer_company_type),
        "<company_website>": listing.employer_website,
        "<linkedin>": linkedin_link,
        "<app_link>": listing.job_apply_link,
        "<required_skills>": list_to_bullet_points(listing.job_required_skills),
        "<job_description>": str(listing.job_description),
    }
    find_and_replace(job_info_template, replacements, f"{mypath}/{file_name}_info.docx")

    break
