import cv2

# 顔検出分類機
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 対象動画
cap = cv2.VideoCapture(0)


while True:

    ret, frame = cap.read()

    # 顔検出
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    thresh_value, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

    # 顔の領域にモザイクを適用
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        # モザイク加工
        face = cv2.resize(face, (10, 10), interpolation=cv2.INTER_LINEAR)
        face = cv2.resize(face, (w, h), interpolation=cv2.INTER_NEAREST)
        frame[y:y+h, x:x+w] = face

    # 加工済みのフレームを書き込む

    cv2.imshow('camera', frame)
    cv2.imshow('gray', gray)
    cv2.imshow('Otsu', otsu)
    print(thresh_value)

    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()