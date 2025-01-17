from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI()

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")

@app.get("/")
def read_root():
    return {"message": "Welcome to Doom's AI!"}

@app.get("/doom")
def doom_speaks(prompt: str):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=50)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"doom_says": response}
