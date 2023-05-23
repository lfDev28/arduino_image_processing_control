import numpy as np
import cv2

low_H = 0  # blue
low_S = 0
low_V = 0

# a= "Right"
# b="left"
# c="middle"

high_H = 255
high_S = 255
high_V = 255

# kernel = np.ones((5,5),np.uint8)
# closekernel = np.ones((45,45),np.uint8)

# cap = cv2.VideoCapture(0)


class ImageProcessing:
    def __init__(self):
        self.low_H = low_H
        self.low_S = low_S
        self.low_V = low_V
        self.high_H = high_H
        self.high_S = high_S
        self.high_V = high_V

        self.kernel = np.ones((5, 5), np.uint8)
        self.closekernel = np.ones((45, 45), np.uint8)

        self.cap = cv2.VideoCapture(0)

    def do_capture(self):
        while (True):
            ret, frame = self.cap.read()

            frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            framethreshold = cv2.inRange(
                frameHSV, (self.low_H, self.low_S, self.low_V), (self.high_H, self.high_S, self.high_V))

            opening = cv2.morphologyEx(
                framethreshold, cv2.MORPH_OPEN, self.kernel)
            closed = cv2.morphologyEx(
                opening, cv2.MORPH_CLOSE, self.closekernel)
            opening = cv2.morphologyEx(
                framethreshold, cv2.MORPH_OPEN, self.kernel)
            closed = cv2.morphologyEx(
                opening, cv2.MORPH_CLOSE, self.closekernel)

            contours, hierarchy = cv2.findContours(
                opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            if (len(contours) > 0):

                cnt = contours[0]
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 1)
                cv2.putText(frame, str(x)+', '+str(y), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))

                if x > 400:
                    return 400  # RIGHT
                elif x < 200:
                    return -400  # LEFT
                else:
                    return 0  # MIDDLE

            cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
