# Ollama Performance Test Script

This repository contains a Python script designed to benchmark the performance of different large language models (LLMs) served by an Ollama instance. It measures key metrics such as latency, token counts, and tokens per second (TPS) for various models and prompts.

## Features

*   **Model Benchmarking:** Test multiple Ollama models with a predefined set of prompts.
*   **Customizable Tests:** Easily configure the Ollama API URL, models to test, prompts, and the number of test repetitions via command-line arguments.
*   **Detailed Metrics:** Captures and displays latency, prompt tokens, response tokens, and tokens per second (TPS) for both prompt evaluation and response generation.
*   **Tabulated Output:** Presents performance results in a clear, easy-to-read table format.
*   **Streaming Response Handling:** Correctly processes streaming responses from the Ollama API to accurately measure performance.

## Requirements

*   Python 3.x
*   An active Ollama instance running locally or accessible via a network.

## Dependencies

The script relies on the following Python libraries:

*   `requests`: For making HTTP requests to the Ollama API.
*   `tabulate`: For formatting the output results into a readable table.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```
    (Note: Replace `your-username/your-repo-name.git` with the actual repository URL if this is not a local clone.)

2.  **Install dependencies:**
    ```bash
    pip install requests tabulate
    ```

## Getting Started

Before running the tests, ensure your Ollama instance is up and running and the models you intend to test are downloaded.

## Usage

Run the script from your terminal. By default, it will connect to `http://localhost:11434/api/generate` and test a predefined set of models and prompts.

```bash
python ollama_performance_test.py
```

### Command-Line Arguments

You can customize the test parameters using the following arguments:

*   `--api-url <URL>`: Specify the Ollama generate API URL (default: `http://localhost:11434/api/generate`).
*   `--models <MODEL1> <MODEL2> ...`: Space-separated list of models to test (e.g., `mistral:7b llama2:7b`).
*   `--prompts <PROMPT1> <PROMPT2> ...`: A list of prompts to use for testing. Enclose prompts with spaces in quotes.
*   `--repetitions <NUMBER>`: Number of times to repeat each prompt test (default: `2`).

## Examples

### Run with default settings

```bash
python ollama_performance_test.py
```

### Test specific models

```bash
python ollama_performance_test.py --models llama2:7b codellama:7b
```

### Use custom prompts and more repetitions

```bash
python ollama_performance_test.py --prompts "Tell me a joke." "Write a short poem about nature." --repetitions 5
```

### Specify a different API URL

```bash
python ollama_performance_test.py --api-url http://192.168.1.100:11434/api/generate
```

## Configuration

The script includes default configurations that can be overridden by command-line arguments:

*   `DEFAULT_OLLAMA_API_URL = "http://localhost:11434/api/generate"`
*   `DEFAULT_MODELS_TO_TEST = ["mistral:7b", "Gemma3:4b", "deepseek-coder-v2:16b", "codellama:7b"]`
*   `DEFAULT_PROMPTS = [...]` (a list of common prompts)
*   `DEFAULT_REPETITIONS = 2`

## Performance

The script measures performance based on wall-clock time for overall latency and utilizes metrics provided directly by the Ollama API (`prompt_eval_count`, `eval_count`, `total_duration`) for more accurate tokens-per-second calculations.

## Changelog

This section summarizes the significant changes and improvements made to the `ollama_performance_test.py` script.

### Functionality

The `ollama_performance_test.py` script is a command-line tool for benchmarking the performance of different models running on an Ollama instance. It sends prompts to the Ollama API and measures key performance metrics.

The script allows users to customize:
- The Ollama API endpoint.
- The models to be tested.
- The prompts used for testing.
- The number of repetitions for each test.

The script then outputs a table with the following metrics:
- **Latency:** The total time taken for the API call.
- **Prompt Tokens:** The number of tokens in the input prompt.
- **Response Tokens:** The number of tokens in the generated response.
- **Prompt Tok/s:** The rate at which prompt tokens are processed.
- **Response Tok/s:** The rate at which response tokens are generated.

### Changes and Improvements

- **Initial Commit:** The first version of the script had hardcoded values for the API URL, models, and prompts. It used the `transformers` library to count tokens.
- **Second Commit:** The script was significantly improved by:
    - Introducing command-line arguments using `argparse` to make the script more flexible.
    - Removing the `transformers` library and instead using the token metrics directly from the Ollama API's response, which is more accurate and efficient.
    - Restructuring the code into `run_performance_test` and `main` functions for better organization.

### Bug Fixes

There are no specific bug fixes mentioned in the commit history, but the improvements in the second commit can be seen as a fix for the initial version's lack of flexibility and potential for inaccurate token counting.

## Troubleshooting

*   **"requests" or "tabulate" not found:** Ensure you have installed the required dependencies using `pip install requests tabulate`.
*   **Connection refused to Ollama API:** Verify that your Ollama instance is running and accessible at the specified API URL. Check the port and IP address.
*   **No results displayed:** This might happen if there were errors connecting to the Ollama API or if the models specified are not available on your Ollama instance. Check the console output for error messages.
*   **Inaccurate TPS metrics:** The script relies on `total_duration` from the Ollama API response for TPS calculation. If this metric is not available or is zero, it falls back to wall-clock time. Ensure your Ollama version provides these metrics.
