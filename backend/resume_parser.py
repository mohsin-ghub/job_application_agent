import os
import pdfplumber
import docx
import tempfile

def extract_text_from_file(uploaded_file):
    _, ext = os.path.splitext(uploaded_file.name.lower())

    if ext == ".pdf":
        return extract_text_from_pdf(uploaded_file)
    elif ext == ".docx":
        return extract_text_from_docx(uploaded_file)
    elif ext == ".txt":
        return uploaded_file.read().decode("utf-8")
    else:
        return "❌ Unsupported file type."

def extract_text_from_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def extract_text_from_docx(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    doc = docx.Document(tmp_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    os.remove(tmp_path)
    return text.strip()
