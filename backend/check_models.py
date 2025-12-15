import google.generativeai as genai
import os
from dotenv import load_dotenv
import sys

# Add current directory to path to ensure .env is found if needed, or just let load_dotenv work
sys.path.append(os.getcwd())

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in environment")
    sys.exit(1)

try:
    genai.configure(api_key=api_key)
    print(f"Library version: {genai.__version__}")

    print("Available models:")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")

    # Explicitly test the model we want to use
    print("\nTesting gemini-1.5-flash connection...")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Hello")
    print(f"Response: {response.text}")

except Exception as e:
    print(f"Error: {e}")
