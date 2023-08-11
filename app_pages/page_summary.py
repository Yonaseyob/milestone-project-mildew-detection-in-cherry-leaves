import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease that affects many plant species "
        f"The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew."
        f"To save time an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 2104 out of +4 thousand images"
        f"sample images of cherry leaves taken from client contain "
        f"powdery mildew and healthy leaves.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Yonaseyob/milestone-project-mildew-detection-in-cherry-leaves/blob/main/README.md).")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew. "
        f"a powdery mildew and healthy leaf visually.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
    )
