import pdfplumber
from docx import Document
import re


# ---------- READ PDF ----------

def read_pdf(file):

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    return text


# ---------- READ DOCX ----------

def read_docx(file):

    doc = Document(file)

    text = "\n".join([p.text for p in doc.paragraphs])

    return text


# ---------- NAME ----------

def extract_name(text):

    lines = text.split("\n")

    for line in lines[:5]:

        line = line.strip()

        if len(line.split()) <= 3 and "@" not in line and not any(char.isdigit() for char in line):

            return line

    return ""


# ---------- EMAIL ----------

def extract_email(text):

    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return email[0] if email else ""


# ---------- PHONE ----------

def extract_phone(text):

    phone = re.findall(
        r"\+?\d[\d -]{8,12}\d",
        text
    )

    return phone[0] if phone else ""


# ---------- EDUCATION ----------

def extract_education(text):

    education_pattern = re.findall(
        r'\b(B\.?Tech|M\.?Tech|B\.?Sc|M\.?Sc|BCA|MCA|MBA|PhD|Bachelor|Master)\b',
        text,
        re.IGNORECASE
    )

    if education_pattern:

        degrees = set([e.lower() for e in education_pattern])

        return ", ".join(degrees)

    return ""


# ---------- LOCATION ----------

def extract_location(text):

    patterns = [
        r'Location[:\-]?\s*([A-Za-z ]+)',
        r'Address[:\-]?\s*([A-Za-z ]+)',
        r'Based in\s*([A-Za-z ]+)',
        r'([A-Za-z]+,\s*India)'
    ]

    for pattern in patterns:

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group(1).strip()

    return ""


# ---------- EXPERIENCE (YEARS + MONTHS) ----------

def extract_experience(text):

    text = text.lower()

    years = re.findall(r'(\d+)\+?\s*years?', text)

    months = re.findall(r'(\d+)\+?\s*months?', text)

    total_exp = 0

    if years:
        total_exp += max([int(y) for y in years])

    if months:
        total_exp += max([int(m) for m in months]) / 12

    return round(total_exp, 2)