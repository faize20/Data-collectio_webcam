#data collection
#make sure to create a folder named 'A' inside a folder named 'Data' before running the code

#--DATA
# |
#  -A
# |
#  -B
# |
#  -C

import cv2
import time

cap = cv2.VideoCapture(1)

folder = "Data/A"
counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("image", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        counter += 1
        cv2.imwrite(f"{folder}/image_{time.time()}.jpg", frame)
        print(counter)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
