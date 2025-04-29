import streamlit as st
from page1 import page1
from page2 import page2
from page2_2 import page2_2
from page3 import page3
from page4 import page4
import base64

import time

import os

def user_in():
    print("Input")
    print(os.getcwd())
    page1()
    if st.button("Next"):
        st.session_state.current_page = "Shortlist"
        st.rerun()

def shortlist():
    print("Top Susceptible Attacks ")
    # with st.spinner('Identifying Vulnerabilities ...'):
    #     time.sleep(5)  # Simulate a delay for processing
    page2()
    if st.button("Generate Attack Trees"):
        st.session_state.current_page = "Attack Trees"
        st.rerun()

def attack_trees():
    print("Detailed Attack Trees")
    page2_2()
    if st.button("Generate Mitigations"):
        st.session_state.current_page = "Suggestions"
        st.rerun()
    

def suggestions():
    print("Recommendations")
    page3()
    if st.button("Generate IAG Controls Rec"):
        st.session_state.current_page = "Controls"
        st.rerun()
    
def controls():
    print("Recommended Controls")
    page4()
        
# Define a function to navigate between pages
def main():
    st.set_page_config(
        layout="wide",
        )
    
    with st.sidebar:
        ##################################### styling ########################################
        st.markdown(
                    """
                    <style>
                    .stApp {
                        max-width: 1200px; /* Adjust the maximum width as needed */
                        margin: left;
                    }
                    .stButton {
                        display: flex;
                        flex-direction: column;
                        align-items: flex-start; /* Align text to the left */
                    }
                    div.stButton > button {
                        width: 30%;
                        height: 50px; /* Adjust the height as needed */
                        margin-bottom: 10px; /* Add margin between buttons if needed */
                        text-align: left; /* Align text to the left within the button */
                        padding-left: 10px; /* Add left padding to the button text */
        
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )
        # Add custom CSS for the sidebar and buttons ##f5f5f5; old grey 
        st.sidebar.markdown(
                        """
                        <style>
                        .sidebar .sidebar-content {
                            background-color: #ffff9f; 
                            padding: 1rem;
                        }
                        .stButton, .stRadio, .stCheckbox {
                            margin-bottom: 1rem;
                        }
                        </style>
                        """,
                        unsafe_allow_html=True,
                    )

        # Set the title and subheading of the sidebar using HTML
        st.markdown('<h1 style="text-align: left; font-size: 40px;">'
                    '<span style="color: #ffd300;">Sec</span>'
                    '<span style="color: #4e008e;">Arch </span></h1>', unsafe_allow_html=True)
        st.markdown(
                    '<h3 style="text-align: left; color: #555; font-size: 14px;"> Secure by Design | AI First </h3>',
                    unsafe_allow_html=True)
         ##################################### styling ends ########################################

   
        
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Architect Inputs"

    pages = {
        "Architect Inputs":user_in,
        "Shortlist":shortlist,
        "Attack Trees" : attack_trees,
        "Suggestions" : suggestions,
        "Controls" : controls
    }
    
    pages[st.session_state.current_page]()

    for page_name in pages.keys():
            if page_name == st.session_state.current_page:
                st.sidebar.markdown(f'<div style="background-color: #fff394; color: black; padding: 0.5rem; border-radius: 5px;"><b>{page_name}</b></div>',
                    unsafe_allow_html=True)
            else:
                st.sidebar.markdown(f'<div style="color: black; padding: 0.5rem;">{page_name}</div>',
                    unsafe_allow_html=True)

    with open("IAG_logo.png", "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
        st.sidebar.markdown(
            f"""
            <div style="
            position:absolute;
            top: 20px;
            right: 10px;">
                <img src="data:image/png;base64,{data}" width="50">
            </div>
            """,
            unsafe_allow_html=True,
        )
        
                
if __name__ == "__main__":
    main()