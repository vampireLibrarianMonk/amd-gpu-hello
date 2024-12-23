import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Step 1: Define model and tokenizer paths
MODEL_NAME = "meta-llama/LLaMA-2-7b-chat-hf"  # Change to your desired model
TOKENIZER_NAME = MODEL_NAME  # Usually the same as the model

# Step 2: Set device to use ROCm GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Step 3: Load the tokenizer and model
print("Loading the model and tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(device)

# Step 4: Create a test prompt
prompt = "Explain the concept of gravity in simple terms."

# Step 5: Tokenize the input prompt
print("Tokenizing input...")
inputs = tokenizer(prompt, return_tensors="pt").to(device)

# Step 6: Generate a response
print("Generating response...")
outputs = model.generate(
    inputs.input_ids,
    max_length=100,  # Adjust the maximum length of the response
    num_return_sequences=1,  # Number of responses to generate
    temperature=0.7,  # Adjust creativity level
)

# Step 7: Decode and print the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("\nGenerated Response:")
print(response)
