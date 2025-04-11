import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load environment variables
load_dotenv()

model_path = os.getenv("TINY_LLAMA_MODEL_PATH")
if not model_path:
    raise ValueError("⚠️ TINY_LLAMA_MODEL_PATH not found in .env")

# Load tokenizer and model locally
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True)

# Create pipeline
llama_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=0 if torch.cuda.is_available() else -1,
)

def generate_lesson(prompt: str) -> str:
    result = llama_pipeline(prompt, max_new_tokens=300, temperature=0.7)
    return result[0]["generated_text"]
