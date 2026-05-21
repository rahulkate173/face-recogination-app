# Face Detection System

## Overview
This project is a real-time face detection system built using:

- Python
- OpenCV
- Streamlit
- Haar Cascade Classifier

The application accesses your webcam, detects human faces in real time, and draws rectangles around detected faces.

---

# Features

- Real-time webcam face detection
- Streamlit web interface
- Start camera using **Capture** button
- Stop camera using **Stop** button
- Uses OpenCV Haar Cascade pretrained model

---

# Project Structure

```bash
face-recogination-system/
│
├── main.py
├── README.md
|___ recogination.py 
└── requirements.txt
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd face-recogination-system
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate environment:

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install streamlit opencv-python numpy
```

---

# Run the Project

```bash
streamlit run main.py
```

or using uv:

```bash
uv run streamlit run main.py
```

---

# How It Works

1. Streamlit creates the web interface.
2. OpenCV accesses the webcam.
3. Frames are converted to grayscale.
4. Haar Cascade detects faces.
5. Rectangles are drawn around detected faces.
6. Video stream is displayed live in Streamlit.

---

# Technologies Used

- Python
- OpenCV
- Streamlit
- NumPy

---

# Output

- Opens webcam
- Detects faces live
- Draws blue rectangles around faces

---

# Future Improvements

- Face recognition
- Multiple face tracking
- Face mask detection
- Attendance system
- Deep learning models (YOLO, Dlib, MTCNN)

---

# Author

Rahul

---

# License

This project is for educational purposes.