import cv2
import face_recognition
import streamlit as st
import numpy as np
from PIL import Image

# Initialize known face encodings and names
known_face_encodings = []
known_face_names = []

# Load images and get face encodings
image_files = [
    ('C:/Face Recognition/Data Science/Vishnuvarthini.jpg', 'Vishnuvarthini'),
    ('C:/Face Recognition/Data Science/Sonali.jpg', 'Sonali'),
    ('C:/Face Recognition/Data Science/Saravanan.jpeg', 'Saravanan'),
    ('C:/Face Recognition/Data Science/Surya Kalyan.jpeg', 'Surya Kalyan'),
    ('C:/Face Recognition/Data Science/Ganga Shri.JPG', 'Ganga Shri'),
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
    ('C:/Face Recognition/Data Science/Sharukkannan.jpg', 'Sharukkannan'),
    ('C:/Face Recognition/Data Science/Venkat Raman.jpg', 'Venkat Raman'),
    ('C:/Face Recognition/Data Science/Hari Krishnan.jpg', 'Hari Krishnan'),
    ('C:/Face Recognition/Data Science/Aysha.JPG', 'Aysha Deesan Banu')
]

for file, name in image_files:
    image = face_recognition.load_image_file(file)
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(name)

# Streamlit app
st.title("Face Recognition App")

# Upload an image file
image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if image_file is not None:
    # Read the image file
    image = np.array(Image.open(image_file))

    # Find all face locations and face encodings in the image
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # Loop through each face found in the image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face and label with the name
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(image, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the resulting image
    st.image(image, channels="BGR")

st.write("Upload an image to see the face recognition in action.")

