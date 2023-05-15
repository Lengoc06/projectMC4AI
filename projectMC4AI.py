import streamlit as st
import cv2

#filename = 'haarcascade_frontalface_default.xml'
#face_cascade = cv2.CascadeClassifier(filename)

def main():
    #Face detection App
    st.title("Face detection App")
    activities = ["Detection", "About"]
    choice = st.slidebar.selectbox("Select Activity", activities)

    #Detection
    '''if choice == "Detection":
        st.subheader("Face Detection")

        #Use Webcam
        run = st.checkbox('Run')
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
        else:
            st.write('Stopped')

    #About
    elif choice == "About":
        st.subheader("About this app")'''

if __name__ == __main__:
    main()
