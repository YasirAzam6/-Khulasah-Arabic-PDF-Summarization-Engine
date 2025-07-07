from huggingface_hub import InferenceClient

HF_TOKEN = "Your Token"

client = InferenceClient(
    model="csebuetnlp/mT5_multilingual_XLSum",
    token=HF_TOKEN
)

def chunk_text(text, max_words=100):
    """Split text into chunks of ~100 words each."""
    sentences = text.split(" ")
    chunks = []
    for i in range(0, len(sentences), max_words):
        chunk = " ".join(sentences[i:i+max_words])
        if len(chunk.strip()) > 0:
            chunks.append(chunk)
    return chunks

def summarize_text(text):
    chunks = chunk_text(text)
    all_summaries = []

    for i, chunk in enumerate(chunks):
        try:
            print(f"Summarizing chunk {i+1}/{len(chunks)}...")
            result = client.summarization(chunk)
            summary = result["summary_text"].strip()
            all_summaries.append(summary)
        except Exception as e:
            print(f"Error in chunk {i+1}: {e}")
            continue

    final_summary = "\n".join(all_summaries)
    return final_summary
