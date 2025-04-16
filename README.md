# 🧠 AI Legal Case Analyzer

This project leverages AI models from [OpenRouter.ai](https://openrouter.ai) — specifically **DeepSeek** and **GPT-4o-mini** — to assist in analyzing legal case documents and image evidence. It performs two key functions:

- Summarizes a legal document (`case1.txt`) using **DeepSeek**.
- Analyzes an image (from a URL) using **GPT-4o-mini** to describe its content.

---

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/legal-analyzer.git
cd legal-analyzer

pip install requests python-dotenv


in  .env file 
OPENAI_API_KEY=your_openrouter_chatgpt_key
DEEPSEEK_API_KEY=your_openrouter_deepseek_key

I kept the legal text to be nalyzed in a text file inside the root folder  and used the command:
python analyzer.py

this gives the following:

Read and summarize the legal document using DeepSeek.

Analyze an image from a hardcoded URL using GPT-4o-mini.

Print both outputs to the console and save them in data/analysis_output.txt.


the reoles of both models:-
DEEPSEEK-

This case involves a contractual dispute between two parties where the plaintiff claims the defendant failed to fulfill their obligations.(this tackles with the cases which are in text format)

GPT-4o-mini-

The image depicts a wooden boardwalk extending into a forested wetland, surrounded by lush greenery under a clear blue sky.(basically it mainly used to tackel cases which have images related to crime scene )

