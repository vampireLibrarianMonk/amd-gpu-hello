import os
import sys
import torch
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM

# Available Models for Secure Enclave Compatibility Analysis
# This script provides an overview of models suited for structured, instruction-following tasks required in secure
# enclave compatibility assessments. Each model is described with its specific strengths, ideal tasks, and loading code.

# Developed by Meta, Llama 2 is an advanced language model series fine-tuned for chat and conversational tasks.
# The 7B and 13B variants provide different levels of depth: the 7B model is suitable for general-purpose tasks and
# runs efficiently on single GPUs, while the 13B model offers enhanced contextual understanding and generates more
# detailed responses, ideal for more complex analysis.
# model_name = "meta-llama/Llama-2-7b-chat-hf"
# model_name = "meta-llama/Llama-2-13b-chat-hf"

# GPT-J 6B is an open-access language model from EleutherAI, designed for a variety of general-purpose natural
# language tasks. It is known for its balanced performance in generating coherent, structured text and can follow
# moderately complex instructions well. This model is a strong alternative for tasks requiring clear and structured responses.
# model_name = "EleutherAI/gpt-j-6B"

# A large open-access model from EleutherAI, GPT-NeoX 20B is designed for complex language generation tasks and can
# produce detailed, coherent responses with greater depth than smaller models. It is ideal for tasks that require
# nuanced understanding and structured outputs, though it may be memory-intensive.
# model_name = "EleutherAI/gpt-neox-20b"

# Flan-T5 models are fine-tuned for instruction-following tasks, making them ideal for prompts that require structured
# responses. These models are designed to respond accurately to explicit instructions, so they may better follow the
# complex and structured prompts needed for secure enclave compatibility assessments. The flan-t5-large model is a
# balanced choice for general-purpose tasks, while flan-t5-xl provides additional depth for more detailed analysis.
# model_name = "google/flan-t5-large"
# model_name = "google/flan-t5-xl"

# BLOOM is an open-access multilingual model developed by BigScience. With 176 billion parameters, BLOOM can handle
# complex language generation tasks and is particularly useful for research purposes. The smaller BLOOM variants (e.g.,
# bloom-7b1) can provide detailed responses while being suitable for single-GPU setups.
# model_name = "bigscience/bloom-7b1"

# MosaicML’s MPT (Mosaic Pre-trained Transformer) models, especially MPT-7B and MPT-7B-Instruct, are tuned for
# instruction-following and structured response generation. MPT-7B-Instruct is optimized for tasks that require adhering
# to specific prompts, making it suitable for compatibility analysis tasks.
# model_name = "mosaicml/mpt-7b"
# model_name = "mosaicml/mpt-7b-instruct"

# T0pp is a variant of the T0 model fine-tuned for zero-shot tasks, optimized for responding to specific instructions
# without additional context. It performs well with direct instructions and could be beneficial for clear prompt-following
# tasks where secure enclave compatibility needs are defined.
# model_name = "bigscience/T0pp"

# Step 1: Authenticate with Hugging Face
if len(sys.argv) < 2:
    print("Error: Hugging Face token is required as the first argument.")
    sys.exit(1)

hugging_face_token = sys.argv[1]
login(token=hugging_face_token)

# Step 2: Check Requirements
def check_requirements():
    """
    Checks for necessary libraries and CUDA availability.
    Returns:
        str: Device for model inference ('cuda' if available, otherwise 'cpu').
    """
    if not torch.cuda.is_available():
        print("Warning: CUDA is not available. Using CPU for inference.")
        return "cpu"
    else:
        print("CUDA is available. Using GPU for inference.")
        return "cuda"

device = check_requirements()

# Step 3: Load the Model and Tokenizer
model_name = "meta-llama/Llama-2-7b-chat-hf"  # Default model for testing
print(f"Loading model {model_name}...")
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype=torch.float16).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Step 4: Function to Test the Model
def test_model(prompt):
    """
    Generates a response from the model for a given prompt.
    Args:
        prompt (str): Input text prompt.
    Returns:
        str: Model-generated response.
    """
    print(f"Generating response for prompt: {prompt}")
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True).to(device)
    outputs = model.generate(inputs["input_ids"], max_length=200, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Step 5: Example Usage
if __name__ == "__main__":
    # Example prompt for testing the model
    print("Available models:")
    print("- meta-llama/Llama-2-7b-chat-hf (default)")
    print("- EleutherAI/gpt-j-6B")
    print("- EleutherAI/gpt-neox-20b")
    print("- google/flan-t5-large")
    print("- google/flan-t5-xl")
    print("- bigscience/bloom-7b1")
    print("- mosaicml/mpt-7b")
    print("- mosaicml/mpt-7b-instruct")
    print("- bigscience/T0pp")

    test_prompt = "Explain the concept of gravity in simple terms."
    response = test_model(test_prompt)
    print("\nModel Response:")
    print(response)
