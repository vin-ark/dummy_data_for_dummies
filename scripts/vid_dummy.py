import cv2

# Define the text, position, and animation properties
text = "Hello, World!"
pos = (10,250)
speed = 10

# Create the video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('hello_world.avi',fourcc, 20.0, (640,480))

# Create the text image
font = cv2.FONT_HERSHEY_SIMPLEX
img = np.zeros((480,640,3), dtype=np.uint8)

# Write the text on the image
cv2.putText(img,text, pos, font, 1, (255,255,255), 2, cv2.LINE_AA)

# Create the animation
for i in range(0, 640, speed):
    img_new = img.copy()
    img_new = img_new[:, i:i+640]
    out.write(img_new)

# Release the video writer
out.release()
