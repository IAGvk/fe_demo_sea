import streamlit as st
import requests
import json
from PIL import Image
import io
import base64

def page1():
    st.title("Input")
    st.subheader("Enter the following details for the architecture under security review.")
    
    col1, col2 = st.columns(2)

    with col1:
        uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        question1 = st.radio("Is this an Internet facing application?", ("Yes", "No"))
        question2 = st.selectbox("What is the sensitivity of data involved?", ["PUBLIC", "INTERNAL", "PROTECTED", "HIGHLY PROTECTED"])
        question3a = st.text_input("What are the existing components of this architecture from review standpoint?")
        question3b = st.text_input("What are the new components being added for review in this architecture?")
        question4 = st.text_input("What are the hosting attributes for this architecture? (e.g. SaaS, IaaS, Containerised, AI project etc)", help="If left blank, the model infers this from the architecture diagram")

    with col2:
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            st.image(image, caption="Uploaded Architecture", use_container_width=True)

    if st.button("Submit"):
        if not question3a and not question3b:
            st.error("Please fill in at least one of the questions regarding the existing or new components.")
        else:
            if uploaded_image is not None:
                image = Image.open(uploaded_image)
                image_bytes = io.BytesIO()
                image.save(image_bytes, format='PNG')
                image_bytes = image_bytes.getvalue()
                image_base64 = base64.b64encode(image_bytes).decode('utf-8')
            else:
                image_base64 = None
        
        
        data = {
            "image": image_base64,
            "questions": [question1, question2, question3a, question3b, question4]
        }
        # for FE testing
        description = "Generated description based on image and questions"
        options = ["Attack 1", "Attack 2", "Attack 3"]
        result = {"description": description, "options": options}
        response = requests.post("http://backend:8000/generate_description", json=data)
        result = response.json()
        st.write(result)
        print(type(result["description"]))
        # changed to /app/input/ after mounting volumes in docker compose
        # changed to input/ during FE testing with venv
        with open("/app/input/data.json", "w") as f:
            json.dump(data, f)
        st.session_state["options"] = result["options"]
        st.session_state["identified_json"] = result["description"]
        st.success("Data submitted successfully!")
        return True
    return False
