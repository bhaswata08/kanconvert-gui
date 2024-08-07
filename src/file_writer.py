def write_file(file_path, content):
    file_extension = file_path.split('.')[-1].lower()

    if file_extension == 'txt':
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    elif file_extension in ['doc', 'docx']:
        # Use a library like python-docx to create a Word document
        # Example using python-docx:
        from docx import Document
        document = Document()
        document.add_paragraph(content)
        document.save(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")
