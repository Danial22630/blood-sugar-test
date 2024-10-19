import streamlit as st

# Function to calculate HbA1c from average glucose
def calculate_hba1c(average_glucose):
    hba1c = (average_glucose + 46.7) / 28.7
    return round(hba1c, 2)

# Streamlit app
st.title("HbA1c Calculator")

st.write("""
This application estimates HbA1c based on average blood glucose levels.
""")

# Input for average glucose level
average_glucose = st.number_input("Enter your average blood glucose level (mg/dL):", min_value=0.0)

if st.button("Calculate HbA1c"):
    if average_glucose > 0:
        hba1c_result = calculate_hba1c(average_glucose)
        st.success(f"Estimated HbA1c: {hba1c_result}%")
    else:
        st.error("Please enter a valid average glucose level.")
