#  pip install opencv-python

import cv2

#  Carrega modelo
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#  Carrega imagem
img = cv2.imread('mia.jpg')

#  Converte para escala de cinza
gray = cv2.cvtcolor(img, cv2.COLOR_BGR2GRAY)

#  Detecta rostos
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#  Desenha retangulo no rosto detectado
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

#  Mostra resultado
cv2.imshow('img', img)
cv2.waitKey()