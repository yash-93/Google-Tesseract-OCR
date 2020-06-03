import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'D:\\Installed Softwares\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('alpha_num.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))

# DETECT CHARACTERS
hImg, wImg, _ = img.shape
configuration = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img, config=configuration)
for b in boxes.splitlines():
    b = b.split(' ')
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x,hImg-y),(w,hImg-h), (0,0,255), 1)
    cv2.putText(img, b[0], (x,hImg-y), cv2.FONT_HERSHEY_COMPLEX, 0.3, (50, 50, 255), 1)

#DETECT WORDS
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x,y),(w+x,h+y), (0,0,255), 1)
            cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.4, (50,50,255),1)

#DETECT DIGITS
hImg, wImg, _ = img.shape
configuration = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(img, config=configuration)
for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 1)
            cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.4, (50, 50, 255), 1)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 1000, 600)
cv2.imshow('image', img)
cv2.waitKey(0)