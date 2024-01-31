import os, cv2

# Setting path for the Images folder
path = 'Images/'

# Creating Images list
Images = []

# Checking each file in the folder
for img in os.listdir(path):
    name,ext = os.path.splitext(img)
    
    # Checking if the extension of the file matches with the image extension
    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path + '/' + img
        print(file_name)
        Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])
height,width,channels = frame.shape
size = (width,height)

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0, count-1):
    frame = cv2.imread(Images[i])
    out.write(frame)

out.release()
   
print('Done')

