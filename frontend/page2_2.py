import streamlit as st




def page2_2():
    st.header("Detailed Attack Trees")
    detailed_attack_tree = st.session_state["attack_tree_result"]
    st.write(detailed_attack_tree)
    selected_options = st.session_state.get("selected_options", {})
    st.title("Attack Techniques and Steps")

    # Iterate through the main attack categories
    for category, attacks in detailed_attack_tree.items():
        st.header(category)  # Display the category as a header
        # Iterate through each attack in the category
        for attack_name, details in attacks.items():
            with st.expander(f"{attack_name} ({details['technique_id']})"):
                st.subheader(details["technique_name"])  # Display the technique name
                if "steps" in details:
                    st.markdown("**Steps to Perform the Attack:**")
                    for step in details["steps"]:
                        st.markdown(f"- {step}")  # Display each step as a bullet point
                if "description" in details:
                    st.markdown("**Description:**")
               	    st.write(details["description"])  # Display the description
    
    return False