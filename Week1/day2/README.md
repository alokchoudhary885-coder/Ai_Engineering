
# Day 2 - AI Engineering

## Topics Learned

1. Python virtual environment using UV.
2. Installing dependencies using `uv add`.
3. Environment variables using python-dotenv.
4. Groq API integration.
5. Groq client initialization.
6. LLM model selection.
7. System Role and User Role.
8. Prompt engineering fundamentals.
9. Temperature parameter and response randomness.
10. Sending chat completion requests.

## Technologies Used

- Python 3.14.7
- UV
- Groq SDK
- python-dotenv
- Groq LLM API
- VS Code

## Project

Created a Python application that connects to the Groq API and generates AI responses using a selected language model.

## Problems Faced and Solutions

### 1. UV Command Error
- Initially used an incorrect virtual environment command.
- Fixed using `uv venv --python 3.14.7`.

### 2. Missing Python Packages
- Encountered `ModuleNotFoundError: No module named 'dotenv'`.
- Installed dependencies using `uv add python-dotenv groq`.

### 3. API Key Not Found
- Initially received `ValueError: API key not found`.
- Checked environment file location and variable loading.
- Used an explicit `.env` path with `load_dotenv()`.

### 4. API Key Loading Returned False
- Debugged environment variable loading using `os.getenv()`.
- Verified that the API key was successfully loaded.

### 5. Temperature Parameter Error
- Tested temperature value 3.
- Groq returned HTTP 400 because the maximum supported value for this request was 2.
- Fixed by setting temperature to 1.

### 6. Response Access Error
- Encountered `TypeError: 'method' object is not subscriptable`.
- Corrected the response access syntax to:
  `response.choices[0].message.content`

## Key Learnings

- How Python communicates with an LLM API.
- How to securely manage API keys.
- How system instructions influence AI responses.
- How temperature affects response randomness.
- How to debug API and environment configuration errors.

## Day 2 Status

Completed basic Groq API integration and experimented with system roles, prompts, and temperature settings.
