import fitz
from summarizer import summarize_text
from preprocess import clean_arabic_text

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

if __name__ == "__main__":
    pdf_path = r"D:\arabic_text_sum\arabic_env\demo.pdf"  
    print("📥 Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    print("🧹 Cleaning text...")
    text = clean_arabic_text(text)

    print("🤖 Summarizing...")
    summary = summarize_text(text)

    print("\n📝 Final Summary:\n")
    print(summary)

    with open("summary_output.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("\n✅ Summary saved to summary_output.txt")
