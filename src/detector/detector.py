import cv2

# MACROS
THRESHOLD_VALUE = 25
MAX_BINARY_VALUE = 255
DILATION_ITERATIONS = 2
MIN_CONTOUR_AREA = 500

# the detector component
class Detector:
    def __init__(self):
        self.prev_frame = None

    def analyze_frame(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if self.prev_frame is None:
            self.prev_frame = gray_frame
            return frame, None 
        else:
            diff = cv2.absdiff(gray_frame, self.prev_frame)
            thresh = cv2.threshold(diff, THRESHOLD_VALUE, MAX_BINARY_VALUE, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=DILATION_ITERATIONS)
            contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            self.prev_frame = gray_frame
            
            # Draw
            for contour in contours:
                if cv2.contourArea(contour) > MIN_CONTOUR_AREA:
                    (x, y, w, h) = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            return frame, contours