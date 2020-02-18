import cv2

cap = cv2.VideoCapture(0)
i=0
while(True):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.imwrite('../Faces/image.jpg', frame)
        break
    
cap.release()
cv2.destroyAllWindows()