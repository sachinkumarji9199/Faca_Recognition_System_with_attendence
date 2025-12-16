import cv2
import numpy as np
from deepface import DeepFace

# Load pre-trained MobileNet SSD model and class labels for person detection
net = cv2.dnn.readNetFromCaffe(
    'deploy.prototxt',  # Path to the Caffe model configuration file
    'mobilenet_iter_73000.caffemodel'  # Path to the Caffe pre-trained model weights
)

# Define the class labels for the MobileNet SSD model
CLASS_LABELS = ['background', 'person']

# Initialize video capture
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam, or replace with a video file path

while True:
    ret, frame = cap.read()
    if not ret:
        break

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    detections = net.forward()

    # Loop over the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Confidence threshold
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

            # Crop the detected person's face
            face = frame[startY:endY, startX:endX]
            if face.size != 0:
                # Gender prediction
                try:
                    result = DeepFace.analyze(face, actions=['gender'], enforce_detection=False)
                    gender = result[0]['gender']
                    label = f"Gender: {gender}"
                    cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                except Exception as e:
                    print(f"Error in gender detection: {e}")

    # Display the resulting frame
    cv2.imshow('Person and Gender Detection', frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
