import streamlit as st
import cv2

st.title("Face detection App")
activities = ["Detection", "About"]
choice = st.slidebar.selectbox("Select Activity", activities)
