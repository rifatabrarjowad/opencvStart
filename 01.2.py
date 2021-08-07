import cv2

framHeight = 480
framWidth = 640
cap = cv2.VideoCapture(0)
cap.set(3,framWidth)
cap.set(4,framHeight)
while True:
    sucess, img = cap.read()
    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break