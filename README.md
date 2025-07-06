# Mini-ChatGPT-using-HuggingFace-Transformers-
Built a lightweight conversational AI assistant using the GPT2-small model from HuggingFace. Implemented a Flask-based web interface for real-time user interaction. Designed prompt templates to simulate human-AI dialogue and handled model inference using PyTorch. Applied sampling techniques (top-k, top-p, temperature) 

# 🧠 Mini ChatGPT using GPT-2

A lightweight chatbot powered by **GPT-2 small** and deployed with **Gradio**. This project simulates a basic conversational AI using HuggingFace Transformers.

> 🚀 Built and deployed by [Logesh Murugan](https://www.linkedin.com/in/logesh-m-72b801258/)

---

## 🌐 Live Demo

👉 [Click here to try the chatbot live](https://huggingface.co/spaces/muruganlogesh/projects)

---

## 💡 Features

- 🤖 Chatbot built with GPT2-small
- 🧠 Real-time text generation
- 🪄 Prompt engineering for simple conversation flow
- 🌐 Deployed on Hugging Face Spaces using Gradio

---

## 📦 Tech Stack

- Python
- Gradio
- Transformers (HuggingFace)
- PyTorch

---

## 🛠️ How It Works

1. User types a message
2. The message is appended to a prompt format: `Human: <message>\nAI:`
3. The GPT-2 model generates a continuation
4. The response is shown in the Gradio interface

---

## 📁 Files

- `app.py` — Core chatbot logic
- `requirements.txt` — Dependencies
- `README.md` — You're reading it!

---

## 🧑‍💻 Author

**Logesh Murugan**  
- 🎓 AI & Data Science Student, Panimalar Engineering College  
- 🔗 [LinkedIn](https://www.linkedin.com/in/logesh-m-72b801258/)  
- 💻 [GitHub](https://github.com/lebazirmoses)

---

## 📝 Notes

- GPT-2 is not fine-tuned; it's the raw pre-trained version.
- You can upgrade this by:
  - Fine-tuning on custom Q&A data
  - Switching to OpenAI GPT-3.5 via API
  - Adding memory / chat history
