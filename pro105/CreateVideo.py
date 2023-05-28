import cv2
import os

img = "img/"

images = []

for file in os.listdir(img):
    name, ext = os.path.splitext(file)

    if ext in [".gif", '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = img+"/"+file
        print(file_name)
        images.append(file_name)

print(len(images))
count = len(images)

frame = cv2.imread(images[0])

hight, width, channel = frame.shape

size = (width, hight)
print(size)

out = cv2.VideoWriter("resultado.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0,count-1):
    frame = cv2.imread(images[i])
    cv2.imshow("Web cam", frame)
    out.write(frame)

out.release()    
print("concluído")