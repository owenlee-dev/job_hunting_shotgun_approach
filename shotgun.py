from datetime import date
from pprint import pprint

from api.jsearch_endpoint import get_jobs
from api.openai_endpoint import get_personalized_paragraph
from assets.cover_letters import *
from docx_scribe import find_and_replace
from filter import filter_job_listings
import json

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
current_template = "assets/docx_cover_letters/Product_CL_Template.docx"

# 1
job_listings = get_jobs("Product Owner in Berlin, Germany")
# 2
jobs_filtered = filter_job_listings(job_listings)

# 3
# print("\n\n")
# for listing in jobs_filtered:
#     print(listing.employer_name)

# # for listing in jobs_filtered:
# #     # 4
# #     paragraph = get_personalized_paragraph(
# #         company_name=listing.employer_name,
# #         position_title=listing.job_job_title,
# #         job_description=listing.job_description,
# #         cover_letter_text=product_role,
# #     )
# #     # 5
# #     replacements = {
# #         "<owenTitle>": str(listing.job_job_title),
# #         "<date>": date.today().strftime("%B %d, %Y"),
# #         "<positionRole>": str(listing.job_job_title),
# #         "<positionLocation>": listing.job_city + ", " + listing.job_country,
# #         "<companyName>": str(listing.employer_name),
# #         "<companyParagraph>": paragraph,
# #     }


# #     find_and_replace(
# #         current_template, replacements, "assets/docx_cover_letters/test_file.docx"
# #     )
#     break
