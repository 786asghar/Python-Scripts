import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for two numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Dropdown to select the operation
operation = st.selectbox("Select an operation", ["Add + ", "Subtract - ", "Multiply * ", "Divide / "])

# Perform the calculation based on the selected operation
num3 = None
if st.button("Calculate"):
    if operation == "Add + ":
        num3 = num1 + num2
    elif operation == "Subtract - ":
        num3 = num1 - num2
    elif operation == "Multiply * ":
        num3 = num1 * num2
    elif operation == "Divide / ":
        if num2 != 0:
            num3 = num1 / num2
        else:
            st.error("Division by zero is not allowed!")

# Display the result
if num3 is not None:
    st.success(f"Result: {num3}")