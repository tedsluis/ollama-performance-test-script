
import requests
import time
import json
from transformers import AutoTokenizer
from tabulate import tabulate

# --- Configuration ---
OLLAMA_API_URL = "http://192.168.11.167:11434/api/generate"
MODELS_TO_TEST = ["mistral:7b","Gemma3:4b", "deepseek-coder-v2:16b", "codellama:7b"]
TEST_PROMPTS = [
    "Write a Python function to calculate the factorial of a number.",
    "Explain the difference between a list and a tuple in Python.",
    "What is the capital of France?",
    "Summarize the plot of the movie Inception.",
    "Write a short story about a robot who discovers music."
]
TEST_REPETITIONS = 2

# --- Tokenizer ---
# Initialize the tokenizer from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("gpt2") # Using gpt2 tokenizer as a general-purpose tokenizer

def count_tokens(text):
    """Counts the number of tokens in a given text using the Hugging Face tokenizer."""
    return len(tokenizer.encode(text))

# --- Main Test Function ---
def run_performance_tests():
    """Runs the performance tests for the specified models and prompts."""
    results = []

    for model in MODELS_TO_TEST:
        print(f"--- Testing Model: {model} ---")
        for i in range(TEST_REPETITIONS):
            for prompt in TEST_PROMPTS:
                print(f"  Test {i+1}/{TEST_REPETITIONS}, Prompt: '{prompt[:30]}...'")
                try:
                    start_time = time.time()

                    # --- API Request ---
                    response = requests.post(
                        OLLAMA_API_URL,
                        json={"model": model, "prompt": prompt},
                        stream=True
                    )
                    response.raise_for_status()

                    # --- Process Streaming Response ---
                    full_response = ""
                    response_token_count = 0
                    
                    for line in response.iter_lines():
                        if line:
                            data = json.loads(line)
                            full_response += data.get("response", "")
                            if data.get("done"):
                                response_token_count = data.get("eval_count", 0)


                    end_time = time.time()

                    # --- Calculations ---
                    latency = end_time - start_time
                    prompt_token_count = count_tokens(prompt)
                    
                    # Avoid division by zero
                    req_tokens_per_sec = prompt_token_count / latency if latency > 0 else 0
                    res_tokens_per_sec = response_token_count / latency if latency > 0 else 0


                    # --- Store Result ---
                    results.append([
                        model,
                        f"{prompt[:30]}...",
                        i + 1,
                        f"{latency:.2f}s",
                        prompt_token_count,
                        response_token_count,
                        f"{req_tokens_per_sec:.2f}",
                        f"{res_tokens_per_sec:.2f}"
                    ])

                except requests.exceptions.RequestException as e:
                    print(f"  Error testing model {model}: {e}")
                    results.append([model, f"{prompt[:30]}...", i + 1, "Error", "N/A", "N/A", "N/A", "N/A"])


    # --- Print Results Table ---
    headers = [
        "Model", "Prompt", "Test Run", "Latency", 
        "Prompt Tokens", "Response Tokens", 
        "Request Tok/s", "Response Tok/s"
    ]
    print("--- Performance Test Results ---")
    print(tabulate(results, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    print("Starting Ollama performance test...")
    print("This may take a while depending on the models and hardware.")
    print("Please ensure you have the 'transformers', 'torch', and 'tabulate' libraries installed.")
    print("You can install them using: pip install transformers torch tabulate")
    run_performance_tests()
