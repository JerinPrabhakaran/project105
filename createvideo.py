import os
import cv2

path = "C:/Users/sjeri/OneDrive/Documents/coding/Python/project 105/Images"

images = []
image = os.listdir(path)
for x in image :
    name,ext = os.path.splitext(x)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.bmp']:
        file_name = path+'/'+x
        # print(file_name)
        images.append(file_name)

count = len(images)
print(count)   

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
print(size)

video = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(count-1,1,-1):
     frame1 = cv2.imread(images[i])
     video.write(frame1)

video.release()
     
