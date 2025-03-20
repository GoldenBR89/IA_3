import re

def extract_cnpj(text):
    pattern = r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b"
    match = re.search(pattern, text)
    return match.group(0) if match else ""