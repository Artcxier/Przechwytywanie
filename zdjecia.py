import cv2
#TLS socket configuration
vc = cv2.VideoCapture(0)
cv2.nameWindow("WebCam", cv2.WINDOW_NORMAL)


 #Send a frame over an encrypted TCP connection one at a time
while vc.isOpened():
    status, frame = vc.read()
    cv2.imshow("WebCam", frame)
    print(frame)

   
    #Wait 20s before reading the frame again
    key = cv2.waitKey(20)

    #close if esc key is pressed
    if key == 27:
        break

vc.relase()
cv2.destroyWindow("WebCam")
    