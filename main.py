import sys
sys.stdout.reconfigure(encoding='utf-8')


import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

CHATGPT_API_KEY = os.getenv("OPENAI_API_KEY", "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")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "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")

def query_chatgpt_with_image(image_url, prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {CHATGPT_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_url}}
                ]
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Function to query DeepSeek for TEXT input
def query_deepseek(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "deepseek/deepseek-r1-distill-llama-70b:free",
        "messages": [{"role": "user", "content": prompt}],
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Main function
if __name__ == "__main__":
    case_file = "data/case1.txt"

    if os.path.exists(case_file):
        with open(case_file, "r", encoding="utf-8") as file:
            case_text = file.read()
        print("\n🔹 **Analyzing Legal Document (case1.txt) with DeepSeek...**")
        deepseek_response = query_deepseek(f"Summarize this legal case in simple terms:\n\n{case_text}")
        print("📝 **DeepSeek Summary:**\n", deepseek_response)
    else:
        print(f"❌ Error: File {case_file} not found!")

    # Optional: If you have an evidence image, analyze it too
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
    print("\n🔹 **Analyzing Evidence Image with GPT-4o-mini...**")
    chatgpt_response = query_chatgpt_with_image(image_url, "Describe the contents of this image.")
    print("📝 **GPT-4o-mini Image Analysis:**\n", chatgpt_response)

    # Save results
    with open("data/analysis_output.txt", "w", encoding="utf-8") as output_file:
        output_file.write(f"🔹 **DeepSeek Summary:**\n{deepseek_response}\n\n")
        output_file.write(f"🔹 **GPT-4o-mini Image Analysis:**\n{chatgpt_response}\n")