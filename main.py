import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
	if len(sys.argv) < 2:
		print("Error: No prompt provided!")
		print('Usage: python3 main.py "Place your prompt here [optional flags]"')
		sys.exit(1)

	user_prompt = sys.argv[1]

	load_dotenv()
	api_key = os.environ.get("GEMINI_API_KEY")
	client = genai.Client(api_key=api_key)
	
	messages = [
		types.Content(role="user", parts=[types.Part(text=user_prompt)]),
	]

	output = client.models.generate_content(
		model="gemini-2.0-flash-001",
		contents=messages,
	)
	response = output.text
	if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
		print(f"User prompt: {user_prompt}")
		print(f"Prompt tokens: {output.usage_metadata.prompt_token_count}")
		print(f"Response tokens: {output.usage_metadata.candidates_token_count}")
	print(response)

if __name__ == "__main__":
	main()