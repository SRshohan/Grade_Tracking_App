import cv2
from PIL import Image
import pytesseract

def capPicture():
# def ocr_integration():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Convert to Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        # Apply a median blur to reduce noise
        processed = cv2.medianBlur(thresh, 3)

        # Use Tessecret to do OCR on the frame
        text = pytesseract.image_to_string(processed)

        cv2.imshow('Camera feed', frame)
        print("Detected text: ", text)

        # Break 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    None

