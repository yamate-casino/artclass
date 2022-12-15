import qrcode
import cv2
import os
img = qrcode.make("hello")
img.save("qr.png")
print(img)
img2 = cv2.imread("qr.png")
cv2.imshow("Image",img2)
cv2.waitKey()
os.remove("/Documents/FoodShare/qr.png")