import re

def clean_arabic_text(text):
    # Remove tashkeel (diacritics)
    text = re.sub(r'[ًٌٍَُِّْـ]', '', text)
    # Normalize letters
    text = re.sub(r'[إأآا]', 'ا', text)
    text = re.sub(r'ى', 'ي', text)
    text = re.sub(r'ؤ', 'ء', text)
    text = re.sub(r'ئ', 'ء', text)
    text = re.sub(r'ة', 'ه', text)
    # Remove extra spaces and symbols
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
