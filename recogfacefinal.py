import face_recognition
import numpy as np
from cv2 import cv2


video_capture = cv2.VideoCapture(0)


# Sample picture 1
khwaja_image = face_recognition.load_image_file("khwaja.jpg")
khwaja_face_encoding = face_recognition.face_encodings(khwaja_image)[0]


# Sample picture 2
ali_image = face_recognition.load_image_file("ali.jpg")
ali_face_encoding = face_recognition.face_encodings(ali_image)[0]


# Sample picture 3
purshotam_image = face_recognition.load_image_file("purshotam.jpg")
purshotam_face_encoding = face_recognition.face_encodings(purshotam_image)[0]

# Arrays create karo of known face encodings and their names
known_face_encodings = [
    khwaja_face_encoding,
    ali_face_encoding,
    purshotam_face_encoding
]
known_face_names = [
    "Khwaja",
    "Ali",
    "Our Sir"
]

# Initialize karo some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab krne ke liye a single frame of video
    ret, frame = video_capture.read()

    # Resize krne ke liye frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert krne ke liye image from BGR color to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find krne ke liye sab faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Dekhne ke liye if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Gibran"

            # # Agar match was found in known_face_encodings, just use the first one.
            # Aur if it is True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Box draw krne ke liye around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Label draw krne ke liye with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display krne ke liye the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()