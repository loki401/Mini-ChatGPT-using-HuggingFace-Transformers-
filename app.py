import gradio as gr
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load GPT-2
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

# Chatbot function
def chat_with_gpt2(message):
    prompt = f"Human: {message}\nAI:"
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)

    with torch.no_grad():
        output = model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_length=150,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            repetition_penalty=1.2
        )

    response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response.strip()

# Gradio interface
iface = gr.Interface(
    fn=chat_with_gpt2,
    inputs=gr.Textbox(lines=4, placeholder="Type your message here..."),
    outputs="text",
    title="Mini ChatGPT",
    description="Chat with a mini GPT-2 model using HuggingFace Transformers and Gradio."
)

iface.launch()
