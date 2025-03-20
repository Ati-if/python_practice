import streamlit as st
# Input fields for numbers
num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")


# Dropdown menu for operation selection
operation = st.selectbox('Choose an operation:', ["Add", "Subtract", "Multiply", "Divide"])
                         
 # Perform the calculation based on the select operation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2 
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

  # Display  the result
st.write("Result:" , result)                                   