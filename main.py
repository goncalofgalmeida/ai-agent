import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
	program_args = sys.argv

	if not len(program_args) == 2:
		print("Error: No prompt provided!")
		print('Usage: python3 main.py "Place your prompt here"')
		exit(1)

	load_dotenv()
	api_key = os.environ.get("GEMINI_API_KEY")
	client = genai.Client(api_key=api_key)

	output = client.models.generate_content(
		model="gemini-2.0-flash-001",
		contents=program_args[1]
	)
	response = output.text
	print(response)
	print(f"Prompt tokens: {output.usage_metadata.prompt_token_count}")
	print(f"Response tokens: {output.usage_metadata.candidates_token_count}")

main()