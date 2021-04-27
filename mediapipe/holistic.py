import cv2
import mediapipe as mp
import csv
import datetime
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use "break" instead of "continue".
            continue

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        
        image_height, image_width, _ = image.shape
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = holistic.process(image)
        
        # Store left and right index coordinates into csv files
        left_index_row = []
        right_index_row = []
        if results.pose_landmarks:
            left_index_row.append(datetime.datetime.now().timestamp())
            left_index_row.append(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_INDEX].x * image_width)
            left_index_row.append(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_INDEX].y * image_height)
            left_index_row.append(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_INDEX].visibility)
            
            right_index_row.append(datetime.datetime.now().timestamp())
            right_index_row.append(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_INDEX].x * image_width)
            right_index_row.append(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_INDEX].y * image_height)
            right_index_row.append(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_INDEX].visibility)
        # Open the file in the write mode
        with open("../data/left_index.csv", "a") as f:
            # Create the csv writer
            writer = csv.writer(f)
            # Write a row to the csv file
            writer.writerow(left_index_row)
        # Open the file in the write mode
        with open("../data/right_index.csv", "a") as f:
            # Create the csv writer
            writer = csv.writer(f)
            # Write a row to the csv file
            writer.writerow(right_index_row)
        
        # Draw landmark annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
        mp_drawing.draw_landmarks(
            image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(
            image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(
            image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        cv2.imshow("MediaPipe Holistic", image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
