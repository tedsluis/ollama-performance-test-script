
import requests
import time
import json
import argparse
from tabulate import tabulate

# --- Default Configuration (can be overridden by command-line arguments) ---
DEFAULT_OLLAMA_API_URL = "http://localhost:11434/api/generate"
DEFAULT_MODELS_TO_TEST = ["mistral:7b","Gemma3:4b", "deepseek-coder-v2:16b", "codellama:7b"]
DEFAULT_PROMPTS = [
    "Write a Python function to calculate the factorial of a number.",
    "Explain the difference between a list and a tuple in Python.",
    "What is the capital of France?",
    "Summarize the plot of the movie Inception.",
    "Write a short story about a robot who discovers music."
]
DEFAULT_REPETITIONS = 2

# --- Main Test Function ---
def run_performance_test(api_url, models, prompts, repetitions):
    """Runs the performance tests for the specified models and prompts."""
    results = []

    for model in models:
        print(f"--- Testing Model: {model} ---")
        for i in range(repetitions):
            for prompt in prompts:
                print(f"  Test {i+1}/{repetitions}, Prompt: '{prompt[:30]}...'")
                try:
                    start_time = time.time()

                    # --- API Request ---
                    response = requests.post(
                        api_url,
                        json={"model": model, "prompt": prompt, "stream": True},
                    )
                    response.raise_for_status()

                    # --- Process Streaming Response ---
                    full_response_text = ""
                    final_data = {}

                    for line in response.iter_lines():
                        if line:
                            try:
                                data = json.loads(line)
                                full_response_text += data.get("response", "")
                                # The final response object contains all the stats
                                if data.get("done"):
                                    final_data = data
                            except json.JSONDecodeError:
                                print(f"  Warning: Could not decode JSON line: {line}")

                    end_time = time.time()

                    # --- Calculations ---
                    # Use wall-clock time for user-perceived latency
                    total_latency_wall_clock = end_time - start_time

                    # Use more accurate metrics from the Ollama API response
                    prompt_tokens = final_data.get("prompt_eval_count", 0)
                    response_tokens = final_data.get("eval_count", 0)

                    # Ollama durations are in nanoseconds, convert to seconds
                    total_duration_api = final_data.get("total_duration", 0) / 1e9

                    # Use API duration for TPS calculation if available, otherwise fall back to wall-clock time
                    latency_for_tps_calc = total_duration_api if total_duration_api > 0 else total_latency_wall_clock

                    # Avoid division by zero
                    prompt_tps = prompt_tokens / latency_for_tps_calc if latency_for_tps_calc > 0 else 0
                    response_tps = response_tokens / latency_for_tps_calc if latency_for_tps_calc > 0 else 0

                    # --- Store Result ---
                    results.append({
                        "Model": model,
                        "Prompt": f"{prompt[:30]}...",
                        "Test Run": i + 1,
                        "Latency (s)": f"{total_latency_wall_clock:.2f}",
                        "Prompt Tokens": prompt_tokens,
                        "Response Tokens": response_tokens,
                        "Prompt Tok/s": f"{prompt_tps:.2f}",
                        "Response Tok/s": f"{response_tps:.2f}"
                    })

                except requests.exceptions.RequestException as e:
                    print(f"  Error testing model {model}: {e}")
                    results.append({
                        "Model": model, "Prompt": f"{prompt[:30]}...", "Test Run": i + 1,
                        "Latency (s)": "Error", "Prompt Tokens": "N/A", "Response Tokens": "N/A",
                        "Prompt Tok/s": "N/A", "Response Tok/s": "N/A"
                    })

    # --- Print Results Table ---
    if not results:
        print("No results to display.")
        return

    # Convert list of dictionaries to list of lists for tabulate
    headers = list(results[0].keys())
    rows = [list(r.values()) for r in results]

    print("\n--- Performance Test Results ---")
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def main():
    """Parses command-line arguments and runs the test."""
    parser = argparse.ArgumentParser(description="Ollama Performance Test Script.")
    parser.add_argument("--api-url", type=str, default=DEFAULT_OLLAMA_API_URL,
                        help=f"Ollama generate API URL (default: {DEFAULT_OLLAMA_API_URL})")
    parser.add_argument("--models", nargs='+', default=DEFAULT_MODELS_TO_TEST,
                        help=f"Space-separated list of models to test (default: {' '.join(DEFAULT_MODELS_TO_TEST)})")
    parser.add_argument("--prompts", nargs='+', default=DEFAULT_PROMPTS,
                        help="A list of prompts to use for testing.")
    parser.add_argument("--repetitions", type=int, default=DEFAULT_REPETITIONS,
                        help=f"Number of times to repeat each prompt test (default: {DEFAULT_REPETITIONS})")

    args = parser.parse_args()

    print("Starting Ollama performance test...")
    print(f"Models: {', '.join(args.models)}")
    print(f"Repetitions per prompt: {args.repetitions}")
    print("This may take a while depending on the models and hardware.")
    print("Please ensure you have the 'requests' and 'tabulate' libraries installed.")
    print("You can install them using: pip install requests tabulate")

    run_performance_test(args.api_url, args.models, args.prompts, args.repetitions)

if __name__ == "__main__":
    main()
