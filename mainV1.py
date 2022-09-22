################ Basic code for getting frames from WEBCAM ################


import cv2     


cap = cv2.VideoCapture(0)       # create cap variable of Any type which stores frames from our 0th webcam

while True:                     # infinite loop
    _, frm = cap.read()         # read frames from cap 

    frm = cv2.flip(frm,1)       # [Q = flipping hui hi nahi?] flip the frame because mirror because inverted photos are coming PASS 1 for horizontal flipping

    cv2.imshow("window",frm)


    if cv2.waitKey(1) == 27:    # wait for 1 second if user press ESC(27) key 
        cv2.destroyAllWindows() # destroy window that is showing 
        cap.release()           # release camera
        break
