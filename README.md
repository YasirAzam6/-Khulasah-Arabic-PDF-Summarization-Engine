# 📄 Khulasah – Arabic PDF Summarization Engine

**Khulasah** is an Arabic-language document summarization tool that extracts text from Arabic PDFs and generates concise summaries using transformer-based large language models. It is optimized for native Arabic input and designed to work directly with Hugging Face’s hosted inference API—no GPU setup or model downloads required.

---

## 📚 Table of Contents

- [About](#-about)
- [Key Features](#-key-features)
- [Models Used](#-models-used)
- [System Architecture](#-system-architecture)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [License](#-license)

---

## 🧠 About

Khulasah solves the common problem of dealing with lengthy Arabic documents—academic articles, official reports, or news analysis—by offering high-quality, language-specific summarization in a fully automated pipeline.

---

## ✨ Key Features

- 🧾 PDF text extraction using `PyMuPDF`
- 🧹 Arabic-specific preprocessing and cleaning
- 🤖 Transformer-based summarization with instruction-following
- 🌐 Hugging Face hosted inference—no downloads or GPUs required
- 📤 Outputs saved to `.txt` for further processing
- 💬 UTF-8 support for Arabic script

---

## 🧠 Models Used

| Model Name | Description | Hosted On |
|------------|-------------|------------|
| `ALLaM-AI/ALLaM-7B-Instruct-preview` | A 7B parameter instruction-tuned Arabic-centric model, ideal for summarization and reasoning tasks in Arabic. | Hugging Face Inference API |
| Alternatives | `csebuetnlp/mT5_multilingual_XLSum`, `aubmindlab/aragpt2-base`, `bert-base-arabic-camelbert-ca` | Optional fallback options |

**Model Access:**  
Khulasah uses the `InferenceClient` from `huggingface_hub`, requiring an API token (free-tier available).

---

## 🏗️ System Architecture

PDF (Arabic) → Text Extraction → Arabic Cleaning → Prompt → HF API (ALLaM) → Summary Output

markdown
Copy
Edit

- `extract_text_from_pdf`: Uses `PyMuPDF` to get full page-wise content
- `clean_arabic_text`: Removes diacritics, Latin noise, and extra whitespace
- `summarize_text`: Sends the processed text to Hugging Face inference endpoint
- Result saved to `summary_output.txt`

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.10+
- `huggingface_hub`
- `PyMuPDF` (`fitz`)
- `.env` with Hugging Face token

### 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/khulasah.git
cd khulasah
python -m venv arabic_env
arabic_env\Scripts\activate       # On Windows
# or
source arabic_env/bin/activate    # On Linux/Mac

pip install -r requirements.txt
🔐 Hugging Face Token
Get your token from https://huggingface.co/settings/tokens

Save it as HF_TOKEN in a .env file or directly use in code.

▶️ Usage
Add your Arabic .pdf file in the project directory (e.g. demo.pdf)

Run:

bash
Copy
Edit
python main.py
Output will be printed and saved to summary_output.txt.

📂 Project Structure
bash
Copy
Edit
khulasah/
│
├── main.py                # Entry point: handles PDF input and final summary
├── summarizer.py          # Handles interaction with HF API
├── preprocess.py          # Cleans Arabic text for better input
├── utils.py               # (Optional) Helper functions for logs, etc.
├── requirements.txt       # Required Python packages
└── summary_output.txt     # Final summary output
📝 Sample Output
Input: Full Arabic PDF document
Output (Generated by ALLaM-7B):

Copy
Edit
يتوقع علماء تسجيل أقصر يوم في تاريخ الأرض بسبب التسارع الغامض لدورانها. هذا التغير قد يؤثر على الأنظمة التقنية مثل GPS والاتصالات. العلماء يدرسون أسباب هذا التغير مثل حركة النواة الداخلية وذوبان الأنهار الجليدية.
⚖️ License
This project is released under the MIT License.
Model usage must comply with ALLaM-AI’s license and terms.

vbnet
Copy
Edit
