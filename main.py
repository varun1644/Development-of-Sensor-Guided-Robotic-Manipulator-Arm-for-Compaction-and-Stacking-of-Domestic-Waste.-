import cv2
import time

from ultralytics import YOLO

import ik
from config import CAMERA_INDEX, PLACE_XY_MM

# Load YOLO model
model = YOLO("best.pt")

# Start camera
cap = cv2.VideoCapture(CAMERA_INDEX)

ik.setup()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    for r in results:
        boxes = r.boxes

        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]

            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

            # Convert pixels to mm (example scaling)
            target_x = cx * 0.5
            target_y = cy * 0.5

            try:
                ik.pick_at(target_x, target_y)

                px, py = PLACE_XY_MM
                ik.place_at(px, py)

                time.sleep(1)

            except Exception as e:
                print(e)

    cv2.imshow("Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

ik.cleanup()
