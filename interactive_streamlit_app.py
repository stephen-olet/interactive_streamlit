import streamlit as st
import pandas as pd
import numpy as np

# App Title
st.title("Interactive Streamlit App")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a Page:", ["Home", "Data Insights", "About"])

# Home Page
if page == "Home":
    st.header("Welcome to the Interactive Streamlit App!")
    st.write("Explore the functionality of Streamlit through this example app.")

    # User Input: Name
    user_name = st.text_input("Enter your name:", placeholder="Type your name here")
    if user_name:
        st.write(f"Hello, {user_name}! Welcome! 🎉")

    # User Input: Favorite Number
    favorite_number = st.number_input("Pick a number between 1 and 100:", min_value=1, max_value=100)
    st.write(f"You selected the number {favorite_number}.")

# Data Insights Page
elif page == "Data Insights":
    st.header("Explore Data Insights")

    # Generate Random Data
    data = {
        "Category": ["A", "B", "C", "D"],
        "Values": np.random.randint(10, 100, 4)
    }
    df = pd.DataFrame(data)

    # Display Dataset
    st.write("Sample Dataset:")
    st.dataframe(df)

    # Data Visualizations
    st.subheader("Visualizations")

    # Bar Chart
    st.write("### Bar Chart")
    st.bar_chart(df.set_index("Category"))

    # Line Chart
    st.write("### Line Chart")
    line_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A", "B", "C"]
    )
    st.line_chart(line_data)

# About Page
elif page == "About":
    st.header("About This App")
    st.write("""
        This app is a demonstration of building a simple interactive application using Streamlit. 
        Streamlit allows you to create web applications for data visualization and user interaction quickly and easily.
    """)
    st.info("Developed by Stephen Olet.")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Built with ❤️ using Streamlit.")
