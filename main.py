import cv2
import mediapipe as mp
import pyautogui


cam = cv2.VideoCapture(0) #open the webcam
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size() # To get the screen size


while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1) # to invert the webcam in y axis
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    #print(landmark_points)
    if landmark_points:
        landmarks = landmark_points[0].landmark
        x = int(landmarks[473].x * frame_w)
        y = int(landmarks[473].y * frame_h)
        screen_x = (((screen_w / frame_w * (x*1.4) - 475) - 720) * 2) + 720 #to get the ratio
        screen_y = (((screen_h / frame_h * (y*1.4) - 125) - 450) * 1.5) + 450
        pyautogui.moveTo(screen_x, screen_y) # to move the cursor
        right = [landmarks[474], landmarks[475]]
        left = [landmarks[145], landmarks[159]]

        if abs(left[0].y - left[1].y) < 0.02: #test if the the two yellow landmarks are close
            pyautogui.mouseDown() #to click
            #pyautogui.sleep(1)
        else:
            pyautogui.mouseUp() #to click
            #pyautogui.sleep(1)

        if abs(right[0].y - right[1].y) < 0.012: #test if the the two yellow landmarks are close
            pyautogui.rightClick() #to click




    cv2.imshow('Eyes Mouse AI', frame)
    cv2.waitKey(1)