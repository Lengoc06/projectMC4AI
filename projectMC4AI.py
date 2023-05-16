from types import GeneratorType
import streamlit as st
import cv2
import numpy as np

filename = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(filename)

@st.cache
def load_image(img):
    im = Image.open(img)
    return im

def detect_faces(our_image):
    new_img = np.array(our_image.convert('RBG'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = clf.detecMultiScale(gray,1.1,4)
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)
    return img, faces

def main():
    #Face detection App
    st.title("Face detection App")
    activities = ["Detection", "About"]
    choice = st.slidebar.selectbox("Select Activity", activities)

    #Detection
    if choice == "Detection":
        st.subheader("Face Detection")

        #Use Webcam

        '''run = st.checkbox('Run')
        FRAME_WINDOW = st.image([])
        camera = cv2.VideoCapture(0)
        while run:
            _, frame = camera.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = clf.detecMultiScale(
                gray,
                scaleFactor = 1.1,
                minNeighbors = 5,
                minSize = (30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
            )
            for (x, y, width, height) in faces:
                cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)
            cv2.imshow("Faces", frame)
        '''
        #Upload img
        image_file = st.uploader("Upload Image", type = ['jpg', 'png', 'jpeg'])
        if st.button("Process"):
            if image_file is not None:
                our_image = Image.open(image_file)
                st.("This Is Your Image")
                st.image(our_image)
                result_img, result_faces = detect_faces(our_image)
                st.image(result_img)
                st.success("Found {} faces".format(len(result_faces)))

            else: st.write("You haven't upload any image file")
    #About
    elif choice == "About":
        st.subheader("About this app")

main()
