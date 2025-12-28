import cv2
import mediapipe as mp

# MediaPipe Face Mesh kurulumu
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1)

# Kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # OpenCV BGR -> MediaPipe RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Yüz işleme
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0]

        # Burun ucu (landmark 1)
        nose = face_landmarks.landmark[1]

        h, w, _ = frame.shape
        x = int(nose.x * w)
        y = int(nose.y * h)

        # Burun çiz
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

        # Baş yönü hesaplama
        center_x = w / 2
        margin = w * 0.1

        if x < center_x - margin:
            direction = "LEFT"
        elif x > center_x + margin:
            direction = "RIGHT"
        else:
            direction = "FORWARD"

        # Ekrana yaz
        cv2.putText(
            frame,
            direction,
            (30, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow("Face Direction Test", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
