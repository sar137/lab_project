import streamlit as st
from parser import tokenize_input, Parser

def main():
    st.title("Expression Parser")

    expression = st.text_input("Enter an expression:")

    if st.button("Parse"):
        try:
            tokens = tokenize_input(expression)
            parser = Parser(tokens)
            result = parser.parse()
            st.write("Parse Result:", result)
        except ValueError as e:
            st.error(str(e))

if __name__ == "__main__":
    main()
