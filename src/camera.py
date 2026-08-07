from picamera2 import Picamera2
from datetime import datetime

def capture(height, width, cnt):

    picam2 = Picamera2()

    config = picam2.create_still_configuration(main={"size": (width, height)})
    picam2.configure(config)

    picam2.start()

    filename=f"{cnt}_{datetime.now().strftime('%Y%m%d_%H%M%S%f')[:-4]}.jpg"

    picam2.capture_file(filename)

    picam2.close()
if __name__=="__main__":
    for cnt in range(1,4):
 capture(1080,1920,cnt)