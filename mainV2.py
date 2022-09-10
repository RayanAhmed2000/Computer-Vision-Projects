################ Detecting frames using Mediapipe library ################



import cv2                      # import cv2 library
import mediapipe as mp          # import mediapipe library


drawing = mp.solutions.drawing_utils        # for drawing keypoints on hands
hands = mp.solutions.hands                  # [Q = Ye nhi samajh aya? 3:30 ]reference of hands
hand_obj = hands.Hands(max_num_hands = 1)  # [q = Ye nhi samjh aya ? ]


cap = cv2.VideoCapture(0)       # create cap object of VideoCapture to read frames from our 0th webcam

while True:                     # infinite loop
    _, frm = cap.read()         # Q = WHAT'S THE MEANING OF _,?
    cv2.imshow("window",frm)

    frm = cv2.flip(frm,1)       # [Q = flipping hui hi nahi?] flip the frame because mirror because inverted photos are coming PASS 1 for horizontal flipping

    res = hand_obj.process(cv2.cvtColor(frm,cv2.COLOR_BGR2RGB))    # we will send frames (frm) to hands object and store result in res variable
                                                                   # We have to pass frm in RGB format but OpenCV reads VGA format so we will explicitely convert cv2.cvtColor(frm,cv2.COLOR_BGR2RGB)



    # Now it will not always be the case that there are hands in the frame

    if res.multi_hand_landmarks:        # this will return the number of hands detected in frame so if this count os greater than 0 then we will enter this block
        drawing.draw_landmarks(frm,res.multi_hand_landmarks[0])



    if cv2.waitKey(1) == 27:    # wait for 1 second if user press ESC(27) key 
        cv2.destroyAllWindows() # destroy window that is showing 
        cap.release()           # release camera
        break
