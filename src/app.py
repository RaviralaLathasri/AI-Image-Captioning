import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parents[1] / "assets" / "images"
IMAGE_FILE = ASSETS_DIR / "peacock.jpg"


def render_sidebar() -> str:
    st.sidebar.title("Navigation")
    return st.sidebar.selectbox("Choose Page", ["Home", "Prediction"])


def render_input_form() -> dict:
    name = st.text_input("Enter Customer Name")
    age = st.number_input("Enter Age", min_value=0, max_value=100)
    salary = st.slider("Select salary", min_value=10000, max_value=100000, value=25000)
    gender = st.selectbox("Select Gender", ["Male", "Female"])
    education = st.radio("Education Level", ["UG", "PG", "PHD"])
    agree = st.checkbox("I agree to terms")
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])

    return {
        "name": name,
        "age": age,
        "salary": salary,
        "gender": gender,
        "education": education,
        "agree": agree,
        "uploaded_file": uploaded_file,
    }


def render_demo_card() -> None:
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    st.dataframe(df)

    appointment = st.date_input("Select the appointment date")
    st.write("Appointment Date:", appointment)

    time = st.time_input("Select Appointment time")
    st.write("Appointment Time:", time)

    st.metric("Accuracy", "92%", "+2")

    if IMAGE_FILE.exists():
        st.image(IMAGE_FILE, caption="Peacock")


def render_chart() -> None:
    rand = np.random.normal(1, 2, size=20)
    fig, ax = plt.subplots()
    ax.hist(rand, bins=15)
    st.pyplot(fig)


def render_table() -> None:
    data = {
        "Name": ["Abdul Aziz", "Anna", "Bob", "Peter"],
        "Age": [28, 24, 35, 32],
        "City": ["Hyderabad", "Mumbai", "Kolkata", "Bhopal"],
    }
    data_df = pd.DataFrame(data)
    st.dataframe(data_df)


def main() -> None:
    st.set_page_config(page_title="AI Image Captioning", page_icon="🖼️", layout="wide")
    st.title("AI Image Captioning")
    st.header("Vision-Language Caption Generator")
    st.subheader("Upload an image and generate a caption")
    st.write("This app demonstrates an image captioning workflow built with a pretrained BLIP model.")

    selected_page = render_sidebar()
    user_inputs = render_input_form()

    if selected_page == "Prediction":
        st.info("Prediction page selected.")

    if st.button("Predict"):
        st.success("Predict Successful")
        st.warning("Warning")
        st.error("Error, enter valid input")

    render_demo_card()

    col1, col2 = st.columns(2)
    with col1:
        st.write("Left")
    with col2:
        st.write("Right")

    with st.spinner("Preprocessing..."):
        st.progress(50)

    render_table()
    render_chart()


if __name__ == "__main__":
    main()
