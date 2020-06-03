import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'D:\\Installed Softwares\\Tesseract-OCR\\tesseract.exe'

configuration = r'--oem 3 --psm 6 outputbase digits'

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hImg, wImg, _ = frame.shape
    boxes = pytesseract.image_to_data(frame, config=configuration)
    # boxes = pytesseract.image_to_boxes(frame, config=configuration)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            print(b)
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(frame, (x, y), (w + x, h + y), (0, 0, 255), 1)
                cv2.putText(frame, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.4, (50, 50, 255), 1)

    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()