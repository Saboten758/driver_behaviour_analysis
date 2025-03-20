import cv2
import dlib
from scipy.spatial import distance
import numpy as np
# Initialize
face_detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Eye aspect ratio
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# Mouth aspect ratio
def mouth_aspect_ratio(mouth):
    A = distance.euclidean(mouth[13], mouth[19])
    B = distance.euclidean(mouth[14], mouth[18])
    C = distance.euclidean(mouth[12], mouth[16])
    D = distance.euclidean(mouth[11], mouth[17])
    return (A + B + C) / (3.0 * D)

# Constants
EYE_AR_THRESH = 0.25
MOUTH_AR_THRESH = 0.7
DROWSY_FLAG = 0
YAWN_FLAG = 0
MAX_FLAG = 6

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray, 0)

    for face in faces:
        shape = predictor(gray, face)

        # Landmark points
        try:
            left_eye = [(shape.part(n).x, shape.part(n).y) for n in range(36, 42)]
            right_eye = [(shape.part(n).x, shape.part(n).y) for n in range(42, 48)]
            mouth = [(shape.part(n).x, shape.part(n).y) for n in range(48, 68)]

            # Check if points are too close to image boundaries
            def valid_points(points):
                for (x, y) in points:
                    if x < 0 or y < 0 or x >= frame.shape[1] or y >= frame.shape[0]:
                        return False
                return True

            # Compute Eye Aspect Ratio if eyes are visible
            if valid_points(left_eye) and valid_points(right_eye):
                ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2.0
                ear = round(ear, 2)

                if ear < EYE_AR_THRESH:
                    DROWSY_FLAG += 1
                    if DROWSY_FLAG >= MAX_FLAG:
                        cv2.putText(frame, "DROWSINESS DETECTED", (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                        cv2.putText(frame, "ALERT!!!", (30, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                else:
                    DROWSY_FLAG = 0

                # Optionally draw eyes
                cv2.polylines(frame, [cv2.convexHull(np.array(left_eye))], True, (255, 255, 0), 1)
                cv2.polylines(frame, [cv2.convexHull(np.array(right_eye))], True, (0, 255, 0), 1)

            # Compute Mouth Aspect Ratio if mouth is visible
            if valid_points(mouth):
                mar = mouth_aspect_ratio(mouth)
                mar = round(mar, 2)

                if mar > MOUTH_AR_THRESH:
                    YAWN_FLAG += 1
                    if YAWN_FLAG >= MAX_FLAG:
                        cv2.putText(frame, "YAWNING DETECTED", (30, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
                        cv2.putText(frame, "ALERT!!!", (30, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
                else:
                    YAWN_FLAG = 0

                # Optionally draw mouth
                cv2.polylines(frame, [cv2.convexHull(np.array(mouth))], True, (0, 255, 255), 1)

        except Exception as e:
            print("Face landmarks not fully visible:", e)
            continue

    cv2.imshow("Driver Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()