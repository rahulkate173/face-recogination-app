import streamlit as st
import numpy as np
import cv2

st.title("Face Detection App")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

frame_placeholder = st.empty()

start = st.button("Capture", key="start_button")
stop = st.button("Stop", key="stop_button")

if start:

    cap = cv2.VideoCapture(0)  # to take the host laptop video

    if not cap.isOpened():
        raise ValueError("video capture is not opened")

    while True:

        if stop:
            break

        ret, frame = cap.read()

        if not ret:
            st.write("frames are not coming")
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        frame_placeholder.image(frame_rgb, channels="RGB")

    cap.release()
    cv2.destroyAllWindows()