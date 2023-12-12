import cv2

# 顔検出分類機
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 対象動画
video = cv2.VideoCapture('videos/demo3.mp4')

# 出力動画
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out_video = cv2.VideoWriter('output.mp4', fourcc, 30.0, (int(video.get(3)), int(video.get(4))))

# 動画のフレームに対して処理を行う
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    # 顔検出
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # 顔の領域にモザイクを適用
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        # モザイク加工（例：8x8ピクセルのブロックにする）
        face = cv2.resize(face, (8, 8), interpolation=cv2.INTER_LINEAR)
        face = cv2.resize(face, (w, h), interpolation=cv2.INTER_NEAREST)
        frame[y:y+h, x:x+w] = face

    # 加工済みのフレームを書き込む
    out_video.write(frame)

# リソースの解放
video.release()
out_video.release()
cv2.destroyAllWindows()