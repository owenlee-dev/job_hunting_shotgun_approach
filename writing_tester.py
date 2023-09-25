from docx_scribe import find_and_replace


replacements = {
    "<owenTitle>": "THIS IS",
    "<date>": "THIS BE THE DATE",
    "<positionRole>": "HERE IT BE",
    "<companyName>": "HERE",
    "<companyParagraph>": "YUHS",
}

find_and_replace(
    "assets/docx_cover_letters/Climate_Manager_CL_Template.docx",
    replacements,
    "assets/docx_cover_letters/Climatssssss.docx",
)
