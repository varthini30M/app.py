import streamlit as st
import face_recognition
import cv2
import numpy as np
from PIL import Image

# Load known faces and their encodings
def load_known_faces():
    known_face_encodings = []
    known_face_names = []

    # Add your face encodings and names here
    known_faces = [
        ('C:/Face Recognition/Data Science/Vishnuvarthini.jpg', 'Vishnuvarthini'),
        ('C:/Face Recognition/Data Science/Sonali.jpg', 'Sonali'),
        ('C:/Face Recognition/Data Science/Saravanan.jpeg', 'Saravanan'),
        ('C:/Face Recognition/Data Science/Surya Kalyan.jpeg', 'Surya Kalyan'),
        ('C:/Face Recognition/Data Science/Ganga Shri.jpg', 'Ganga Shri'),
        ('C:/Face Recognition/Data Science/Yuvashri.jpg', 'Yuvashri'),
        ('C:/Face Recognition/Data Science/Manoj Kumar.jpg', 'Manoj Kumar HOD(CS Dept)'),
        ('C:/Face Recognition/Data Science/Jothika.jpg', 'Jothika'),
        ('C:/Face Recognition/Data Science/Guru Kanishka.jpg', 'Guru Kanishka'),
        ('C:/Face Recognition/Data Science/Kanishka Shri.jpg', 'Kanishka'),
        ('C:/Face Recognition/Data Science/Naresh.jpg', 'Naresh'),
        ('C:/Face Recognition/Data Science/Santhosh.jpg', 'Santhosh'),
        ('C:/Face Recognition/Data Science/Dhilip.jpg', 'Dhilip'),
        ('C:/Face Recognition/Data Science/Jeya Deepan.jpg', 'Jeya Deepan'),
        ('C:/Face Recognition/Data Science/Harini.jpg', 'Harini'),
        ('C:/Face Recognition/Data Science/Yuvarajan.jpg', 'Yuvarajan'),
        ('C:/Face Recognition/Data Science/Sharukkannan.jpg', 'Sharukkanan'),
        ('C:/Face Recognition/Data Science/Venkat Raman.jpg', 'Venkat Raman'),
        ('C:/Face Recognition/Data Science/Hari Krishnan.jpg', 'Hari Krishnan')
    ]

    for face_path, name in known_faces:
        image = face_recognition.load_image_file(face_path)
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(name)

    return known_face_encodings, known_face_names

known_face_encodings, known_face_names = load_known_faces()

st.title("Face Recognition App")
st.write("Upload an image to see the face recognition results.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the uploaded image
    image = np.array(Image.open(uploaded_file))
    
    # Detect faces in the image
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # Annotate the image with boxes around faces and names
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
        # Draw a label with a name below the face
        cv2.putText(image, name, (left, top - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)

    # Display the result
    st.image(image, caption="Processed Image", use_column_width=True)
