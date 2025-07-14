# Changelog

## Summary

This document outlines the functionality, changes, and improvements for the `ollama_performance_test.py` script.

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
