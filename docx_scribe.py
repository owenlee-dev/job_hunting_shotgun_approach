from docx import Document

def find_and_replace(file_path, find_text, replace_text):
    document = Document(file_path)
    
    # Iterate through each paragraph and perform replacement
    for paragraph in document.paragraphs:
        if find_text in paragraph.text:
            for run in paragraph.runs:
                run.text = run.text.replace(find_text, replace_text)

    # Save the updated content back to the file
    document.save(file_path)

