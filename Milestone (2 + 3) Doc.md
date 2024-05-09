# Expression Parser
!(![Screenshot (677)](https://github.com/sar137/lab_project/assets/133651258/cd1afe82-c392-4f26-9ca0-83117b83a4a6)

Expression Parser is a Python project that provides a graphical user interface (GUI) built using Streamlit for parsing mathematical expressions. It includes a parser module for tokenizing and parsing expressions.
## Features
* Graphical user interface (GUI) for inputting and parsing mathematical expressions.
* Tokenization of input expressions.
* Parsing of tokenized expressions to evaluate mathematical operations.
* Error handling for invalid expressions.
# Installation
**1. Clone the repository:**
```
git clone https://github.com/yourusername/your-repository.git

```
**2. Install the required dependencies::**
```
pip install -r requirements.txt

```
# Usage
**Downloading the Streamlit GUI**
To run the Streamlit GUI, execute the following command:
```
pip install streamlit

```
**Running the Streamlit GUI**
To run the Streamlit GUI, execute the following command:
```
streamlit run gui.py

```
This command starts a local server and opens the GUI in your default web browser. You can input mathematical expressions in the provided field and click the "Parse" button to see the result.
# Using the Parser Module
The parser module provides functions for tokenizing and parsing mathematical expressions. You can use it in your Python scripts by importing it as follows:
```
from parser import tokenize_input, Parser

```
# Tokenization
To tokenize an input expression, use the **tokenize_input** function:
```
expression = "2 * (3 + 4)"
tokens = tokenize_input(expression)
print(tokens)
```

# Parsing
To parse the tokenized expression, use the **Parser** class::
```
parser = Parser(tokens)
result = parser.parse()
print(result)

```
# Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request.
