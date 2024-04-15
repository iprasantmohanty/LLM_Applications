import streamlit as st

def main():
    st.title("Number Operations")

    # Initialize session state variables
    if 'result' not in st.session_state:
        st.session_state.result = 0

    # Text input for number n
    n = st.text_input("Enter a number n:", value="0", key='n_input')

    # Button to calculate square of n
    if st.button("Calculate Square"):
        try:
            n = int(n)
            st.session_state.result = n ** 2
            st.write(f"The square of {n} is: {st.session_state.result}")
        except ValueError:
            st.error("Please enter a valid number.")

    # Text input for number k
    k = st.text_input("Enter another number k:", value="0", key='k_input')

    # Button to calculate result of (n^2 + k)
    if st.button("Calculate Result"):
        try:
            k = int(k)
            result = st.session_state.result + k
            st.write(f"The result of (n^2 + k) is: {result}")
        except ValueError:
            st.error("Please enter a valid number.")

if __name__ == "__main__":
    main()
