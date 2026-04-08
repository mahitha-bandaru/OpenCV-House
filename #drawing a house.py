#drawing a house using opencv
import cv2
import numpy as np

black = np.ones((500, 500, 3), dtype=np.uint8) * 255
black[:] = (255, 200, 100)   # light sky blue

cv2.rectangle(black, (0, 400), (500, 500), (0, 180, 0), -1)

# Draw the base of the house
cv2.rectangle(black, (100, 300), (400, 500), (49,49,255), -1)

# Draw the roof of the house
cv2.line(black, (100, 300), (250, 150), (30, 30, 150), 5)
cv2.line(black, (400, 300), (250, 150), (30, 30, 150), 5)
pts = np.array([[100, 300], [400, 300], [250, 150]], np.int32)
cv2.fillPoly(black, [pts], (30, 30, 150))

# Draw the door of the house
cv2.rectangle(black, (220, 400), (280, 500), (14, 38, 110), -1)

# Draw the windows of the house
cv2.rectangle(black, (150, 350), (200, 400), (255, 255, 200), -1)
cv2.rectangle(black, (300, 350), (350, 400), (255, 255, 200), -1)

# Left window panes
cv2.line(black, (150, 375), (200, 375), (0, 0, 0), 2)
cv2.line(black, (175, 350), (175, 400), (0, 0, 0), 2)

# Right window panes
cv2.line(black, (300, 375), (350, 375), (0, 0, 0), 2)
cv2.line(black, (325, 350), (325, 400), (0, 0, 0), 2)

#Draw the sun
cv2.circle(black, (400, 100), 50, (0, 255, 255), -1)
for angle in range(0, 360, 30):
    x = int(400 + 70 * np.cos(np.radians(angle)))
    y = int(100 + 70 * np.sin(np.radians(angle)))
    cv2.line(black, (400, 100), (x, y), (0, 255, 255), 2)

#Draw the clouds
cv2.circle(black, (80, 100), 20, (255,255,255), -1)
cv2.circle(black, (100, 90), 25, (255,255,255), -1)
cv2.circle(black, (120, 100), 20, (255,255,255), -1)

cv2.circle(black, (250, 120), 20, (255,255,255), -1)
cv2.circle(black, (270, 110), 25, (255,255,255), -1)
cv2.circle(black, (290, 120), 20, (255,255,255), -1)

#Draw the tree
# trunk
cv2.rectangle(black, (50, 350), (70, 450), (19, 69, 139), -1)
# leaves
cv2.circle(black, (40, 330), 25, (0, 150, 0), -1)
cv2.circle(black, (80, 330), 25, (0, 150, 0), -1)
cv2.circle(black, (60, 300), 30, (0, 170, 0), -1)

#adding borders

#left window border
cv2.rectangle(black, (100, 300), (400, 500), (0, 0, 0), 2)
cv2.rectangle(black, (150, 350), (200, 400), (0, 0, 0), 2)
# Right window border
cv2.rectangle(black, (300, 350), (350, 400), (0, 0, 0), 2)
# House border
cv2.rectangle(black, (100, 300), (400, 500), (0, 0, 0), 2)
# Door border
cv2.rectangle(black, (220, 400), (280, 500), (0, 0, 0), 2)

# Display the image
cv2.imshow('House', black)
cv2.waitKey(0)
cv2.destroyAllWindows()