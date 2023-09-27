from docx_scribe import find_and_replace


replacements = {
    "<owenTitle>": "THIS IS",
    "<date>": "THIS BE THE DATE",
    "<positionRole>": "HERE IT BE",
    "<companyName>": "HERE",
    "<companyParagraph>": "YUHS",
}

find_and_replace(
    "assets/docx_source/Climate_Manager_CL_Template.docx",
    replacements,
    "assets/docx_source/Climatssssss.docx",
)
