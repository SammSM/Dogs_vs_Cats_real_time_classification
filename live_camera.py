import numpy as np
import cv2

import img_classiciation

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_pred = img_classiciation.pred_img(frame)
    cv2.putText(frame, f'{frame_pred}', (25, 25), cv2.FONT_HERSHEY_COMPLEX, 
                1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Webcam Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()