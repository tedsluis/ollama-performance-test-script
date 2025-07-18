$
 python ollama_performance_test.py

ℹ Starting Ollama performance test...
  Models: mistral:7b, Gemma3:4b, deepseek-coder-v2:16b, codellama:7b
  Repetitions per prompt: 2
  This may take a while depending on the models and hardware.
  Please ensure you have the 'requests' and 'tabulate' libraries installed.
  You can install them using: pip install requests tabulate
  --- Testing Model: mistral:7b ---
    Test 1/2, Prompt: 'Write a Python function to cal...'
    Test 1/2, Prompt: 'Explain the difference between...'
    Test 1/2, Prompt: 'What is the capital of France?...'
    Test 1/2, Prompt: 'Summarize the plot of the movi...'
    Test 1/2, Prompt: 'Write a short story about a ro...'
    Test 2/2, Prompt: 'Write a Python function to cal...'
    Test 2/2, Prompt: 'Explain the difference between...'
    Test 2/2, Prompt: 'What is the capital of France?...'
    Test 2/2, Prompt: 'Summarize the plot of the movi...'
    Test 2/2, Prompt: 'Write a short story about a ro...'
  --- Testing Model: Gemma3:4b ---
    Test 1/2, Prompt: 'Write a Python function to cal...'
    Test 1/2, Prompt: 'Explain the difference between...'
    Test 1/2, Prompt: 'What is the capital of France?...'
    Test 1/2, Prompt: 'Summarize the plot of the movi...'
    Test 1/2, Prompt: 'Write a short story about a ro...'
    Test 2/2, Prompt: 'Write a Python function to cal...'
    Test 2/2, Prompt: 'Explain the difference between...'
    Test 2/2, Prompt: 'What is the capital of France?...'
    Test 2/2, Prompt: 'Summarize the plot of the movi...'
    Test 2/2, Prompt: 'Write a short story about a ro...'
  --- Testing Model: deepseek-coder-v2:16b ---
    Test 1/2, Prompt: 'Write a Python function to cal...'
    Test 1/2, Prompt: 'Explain the difference between...'
    Test 1/2, Prompt: 'What is the capital of France?...'
    Test 1/2, Prompt: 'Summarize the plot of the movi...'
    Test 1/2, Prompt: 'Write a short story about a ro...'
    Test 2/2, Prompt: 'Write a Python function to cal...'
    Test 2/2, Prompt: 'Explain the difference between...'
    Test 2/2, Prompt: 'What is the capital of France?...'
    Test 2/2, Prompt: 'Summarize the plot of the movi...'
    Test 2/2, Prompt: 'Write a short story about a ro...'
  --- Testing Model: codellama:7b ---
    Test 1/2, Prompt: 'Write a Python function to cal...'
    Test 1/2, Prompt: 'Explain the difference between...'
    Test 1/2, Prompt: 'What is the capital of France?...'
    Test 1/2, Prompt: 'Summarize the plot of the movi...'
    Test 1/2, Prompt: 'Write a short story about a ro...'
    Test 2/2, Prompt: 'Write a Python function to cal...'
    Test 2/2, Prompt: 'Explain the difference between...'
    Test 2/2, Prompt: 'What is the capital of France?...'
    Test 2/2, Prompt: 'Summarize the plot of the movi...'
    Test 2/2, Prompt: 'Write a short story about a ro...'

  --- Performance Test Results ---
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | Model                 | Prompt                            |   Test Run |   Latency (s) |   Prompt Tokens |   Response Tokens |   Prompt Tok/s |   Response Tok/s |
  +=======================+===================================+============+===============+=================+===================+================+==================+
  | mistral:7b            | Write a Python function to cal... |          1 |          9.8  |              17 |               348 |           1.74 |            35.53 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | mistral:7b            | Explain the difference between... |          1 |          9.79 |              17 |               391 |           1.74 |            39.97 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | mistral:7b            | What is the capital of France?... |          1 |          0.24 |              11 |                 8 |          46.08 |            33.51 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | mistral:7b            | Summarize the plot of the movi... |          1 |          9.23 |              15 |               370 |           1.63 |            40.1  |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | mistral:7b            | Write a short story about a ro... |          1 |         18.45 |              16 |               727 |           0.87 |            39.42 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | mistral:7b            | Write a Python function to cal... |          2 |          5.62 |              17 |               228 |           3.03 |            40.6  |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | mistral:7b            | Explain the difference between... |          2 |          7.32 |              17 |               294 |           2.32 |            40.19 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | mistral:7b            | What is the capital of France?... |          2 |          1.36 |              11 |                54 |           8.07 |            39.64 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | mistral:7b            | Summarize the plot of the movi... |          2 |         10.77 |              15 |               425 |           1.39 |            39.47 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | mistral:7b            | Write a short story about a ro... |          2 |         18.42 |              16 |               716 |           0.87 |            38.88 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | Gemma3:4b             | Write a Python function to cal... |          1 |         14.27 |              21 |               635 |           1.47 |            44.55 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | Gemma3:4b             | Explain the difference between... |          1 |         16.54 |              21 |               888 |           1.27 |            53.71 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | Gemma3:4b             | What is the capital of France?... |          1 |          0.73 |              16 |                39 |          22.09 |            53.85 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | Gemma3:4b             | Summarize the plot of the movi... |          1 |         12.09 |              19 |               650 |           1.57 |            53.76 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | Gemma3:4b             | Write a short story about a ro... |          1 |         14.15 |              20 |               757 |           1.41 |            53.5  |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | Gemma3:4b             | Write a Python function to cal... |          2 |         10.8  |              21 |               578 |           1.94 |            53.53 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | Gemma3:4b             | Explain the difference between... |          2 |         16.52 |              21 |               878 |           1.27 |            53.17 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | Gemma3:4b             | What is the capital of France?... |          2 |          0.75 |              16 |                40 |          21.47 |            53.67 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | Gemma3:4b             | Summarize the plot of the movi... |          2 |         10.97 |              19 |               585 |           1.73 |            53.33 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | Gemma3:4b             | Write a short story about a ro... |          2 |         14.31 |              20 |               760 |           1.4  |            53.13 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | deepseek-coder-v2:16b | Write a Python function to cal... |          1 |          8.04 |              21 |               446 |           2.61 |            55.51 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | deepseek-coder-v2:16b | Explain the difference between... |          1 |          9.38 |              20 |               696 |           2.13 |            74.25 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | deepseek-coder-v2:16b | What is the capital of France?... |          1 |          0.19 |              15 |                 9 |          80.17 |            48.1  |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | deepseek-coder-v2:16b | Summarize the plot of the movi... |          1 |          8.12 |              19 |               606 |           2.34 |            74.65 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | deepseek-coder-v2:16b | Write a short story about a ro... |          1 |         11.09 |              19 |               824 |           1.71 |            74.36 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | deepseek-coder-v2:16b | Write a Python function to cal... |          2 |          5.51 |              21 |               412 |           3.81 |            74.82 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | deepseek-coder-v2:16b | Explain the difference between... |          2 |          9.19 |              20 |               683 |           2.18 |            74.36 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | deepseek-coder-v2:16b | What is the capital of France?... |          2 |          0.19 |              15 |                 9 |          79.06 |            47.44 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | deepseek-coder-v2:16b | Summarize the plot of the movi... |          2 |          6.17 |              19 |               460 |           3.08 |            74.57 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | deepseek-coder-v2:16b | Write a short story about a ro... |          2 |          7.63 |              19 |               567 |           2.49 |            74.4  |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | codellama:7b          | Write a Python function to cal... |          1 |          4.43 |              33 |               155 |           7.45 |            35.01 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | codellama:7b          | Explain the difference between... |          1 |         10.28 |              33 |               507 |           3.21 |            49.31 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | codellama:7b          | What is the capital of France?... |          1 |          0.19 |              27 |                 9 |         139.96 |            46.65 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | codellama:7b          | Summarize the plot of the movi... |          1 |          8.39 |              31 |               418 |           3.7  |            49.84 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | codellama:7b          | Write a short story about a ro... |          1 |         10.89 |              32 |               536 |           2.94 |            49.25 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | codellama:7b          | Write a Python function to cal... |          2 |          2.7  |              33 |               140 |          12.25 |            51.97 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | codellama:7b          | Explain the difference between... |          2 |         11.67 |              33 |               574 |           2.83 |            49.21 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | codellama:7b          | What is the capital of France?... |          2 |          0.19 |              27 |                 9 |         142.37 |            47.46 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | codellama:7b          | Summarize the plot of the movi... |          2 |          8.14 |              31 |               405 |           3.81 |            49.76 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
  | codellama:7b          | Write a short story about a ro... |          2 |          8.86 |              32 |               437 |           3.61 |            49.36 |
  +-----------------------+-----------------------------------+------------+---------------+-----------------+-------------------+----------------+------------------+
