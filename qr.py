import qrcode
import cv2
img = qrcode.make("https://yamate-casino.github.io/artclass/qr.html")
img.save("qr.png")
img2 = cv2.imread("qr.png")
cv2.imshow("Image",img2)
cv2.waitKey()
