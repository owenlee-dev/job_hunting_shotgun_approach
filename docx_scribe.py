from docx import Document


def find_and_replace(file_path, replacements, save_path):
    document = Document(file_path)

    # Handle paragraphs
    for paragraph in document.paragraphs:
        replace_in_paragraph(paragraph, replacements)

    # Handle tables
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                replace_in_paragraph(cell, replacements)

    # Handle headers and footers
    for section in document.sections:
        for header in section.header.paragraphs:
            replace_in_paragraph(header, replacements)
        for footer in section.footer.paragraphs:
            replace_in_paragraph(footer, replacements)

    # Save the updated content to the new location
    document.save(save_path)

def replace_in_paragraph(paragraph, replacements):
    for find_text, replace_text in replacements.items():
        # print(find_text+", "+replace_text)
        paragraph.text = paragraph.text.replace(find_text, replace_text)


# replacements = {
#     "<owenTitle>": "THIS IS",
#     "<date>": "THIS BE THE DATE",
#     "<positionRole>": "HERE IT BE",
#     "<companyName>": "HERE",
#     "<companyParagraph>": "YUHS",
# }

# find_and_replace(
#     "assets/docx_cover_letters/testing.docx",
#     replacements,
#     "assets/docx_cover_letters/Climatssssss.docx",
# )
  