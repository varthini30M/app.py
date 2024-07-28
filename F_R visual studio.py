import cv2
import face_recognition

known_face_encodings=[]
known_face_names=[]

known_person1_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Vishnuvarthini.jpg')
known_person2_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Sonali.jpg')
known_person3_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Saravanan.jpeg')
known_person4_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Surya Kalyan.jpeg')
known_person5_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Ganga Shri.JPG')
known_person6_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Yuvashri.jpg')
known_person7_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Manoj Kumar.jpg')
known_person8_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Jothika.jpg')
known_person9_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Guru Kanishka.jpg')
known_person10_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Kanishka Shri.jpg')
known_person11_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Naresh.jpg')
known_person12_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Santhosh.jpg')
known_person13_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Dhilip.jpg')
known_person14_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Jeya Deepan.jpg')
known_person15_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Harini.jpg')
known_person16_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Yuvarajan.jpg')
known_person17_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Sharukkannan.jpg')
known_person18_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Venkat Raman.jpg')
known_person19_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Hari Krishnan.jpg')
known_person20_image=face_recognition.load_image_file('C:/Face Recognition/Data Science/Aysha.JPG')

known_person1_encodings=face_recognition.face_encodings(known_person1_image)[0]
known_person2_encodings=face_recognition.face_encodings(known_person2_image)[0]
known_person3_encodings=face_recognition.face_encodings(known_person3_image)[0]
known_person4_encodings=face_recognition.face_encodings(known_person4_image)[0]
known_person5_encodings=face_recognition.face_encodings(known_person5_image)[0]
known_person6_encodings=face_recognition.face_encodings(known_person6_image)[0]
known_person7_encodings=face_recognition.face_encodings(known_person7_image)[0]
known_person8_encodings=face_recognition.face_encodings(known_person8_image)[0]
known_person9_encodings=face_recognition.face_encodings(known_person9_image)[0]
known_person10_encodings=face_recognition.face_encodings(known_person10_image)[0]
known_person11_encodings=face_recognition.face_encodings(known_person11_image)[0]
known_person12_encodings=face_recognition.face_encodings(known_person12_image)[0]
known_person13_encodings=face_recognition.face_encodings(known_person13_image)[0]
known_person14_encodings=face_recognition.face_encodings(known_person14_image)[0]
known_person15_encodings=face_recognition.face_encodings(known_person15_image)[0]
known_person16_encodings=face_recognition.face_encodings(known_person16_image)[0]
known_person17_encodings=face_recognition.face_encodings(known_person17_image)[0]
known_person18_encodings=face_recognition.face_encodings(known_person18_image)[0]
known_person19_encodings=face_recognition.face_encodings(known_person19_image)[0]
known_person20_encodings=face_recognition.face_encodings(known_person20_image)[0]

known_face_encodings.append(known_person1_encodings)
known_face_encodings.append(known_person2_encodings)
known_face_encodings.append(known_person3_encodings)
known_face_encodings.append(known_person4_encodings)
known_face_encodings.append(known_person4_encodings)
known_face_encodings.append(known_person6_encodings)
known_face_encodings.append(known_person7_encodings)
known_face_encodings.append(known_person8_encodings)
known_face_encodings.append(known_person9_encodings)
known_face_encodings.append(known_person10_encodings)
known_face_encodings.append(known_person11_encodings)
known_face_encodings.append(known_person12_encodings)
known_face_encodings.append(known_person13_encodings)
known_face_encodings.append(known_person14_encodings)
known_face_encodings.append(known_person15_encodings)
known_face_encodings.append(known_person16_encodings)
known_face_encodings.append(known_person17_encodings)
known_face_encodings.append(known_person18_encodings)
known_face_encodings.append(known_person19_encodings)
known_face_encodings.append(known_person20_encodings)


known_face_names.append('Vishnuvarthini ')
known_face_names.append('Sonali')
known_face_names.append('Saravanan')
known_face_names.append('Surya Kalyan')
known_face_names.append('Ganga Shri')
known_face_names.append('Yuvashri')
known_face_names.append('Manoj Kumar HOD(CS Dept)')
known_face_names.append('Jothika')
known_face_names.append('Guru Kanishka')
known_face_names.append('Kanishka')
known_face_names.append('Naresh')
known_face_names.append('Santhosh')
known_face_names.append('Dhilip')
known_face_names.append('Jeya Deepan')
known_face_names.append('Harini')
known_face_names.append('Yuvarajan')
known_face_names.append('Sharukkanan')
known_face_names.append('Venkat Raman')
known_face_names.append('Hari Krishnan')
known_face_names.append('Aysha Deesan Banu')


#Initialize webcam
video_capture=cv2.VideoCapture(0)

while True:
    #Capture frame -by- frame
    ret, frame=video_capture.read()

    #find all face location in the current frame
    face_locations=face_recognition.face_locations(frame)
    face_encodings=face_recognition.face_encodings(frame, face_locations)

    #Loop through each face found in the frame
    for(top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
        #Check if the face matchers any known faces
        matches=face_recognition.compare_faces(known_face_encodings, face_encodings)
        name='Unknown'

        if True in matches:
            first_match_index=matches.index(True)
            name=known_face_names[first_match_index]

        #Draw a box around the face and label with the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 0, 255), 2)
    
    #Display the resulting frame
    cv2.imshow('Video', frame)

    #Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#Release the webcam and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
