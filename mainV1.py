################ Basic code for getting frames from WEBCAM ################


import cv2      #import cv2 library


cap = cv2.VideoCapture(0)       # create cap object of VideoCapture to read frames from our 0th webcam

while True:                     # infinite loop
    _, frm = cap.read()         # Q = WHAT'S THE MEANING OF _,?
    cv2.imshow("window",frm)

    frm = cv2.flip(frm,1)       # [Q = flipping hui hi nahi?] flip the frame because mirror because inverted photos are coming PASS 1 for horizontal flipping

    if cv2.waitKey(1) == 27:    # wait for 1 second if user press ESC(27) key 
        cv2.destroyAllWindows() # destroy window that is showing 
        cap.release()           # release camera
        break
