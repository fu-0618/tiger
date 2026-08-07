import cv2
import numpy as np

low_color1=np.array([0,50,50])
high_color1=np.array([6,255,255]) #赤色指定１
low_color2=np.array([174,50,50])
high_color2=np.array([180,255,255]) #赤色指定２
coordinates_x = {}
coordinates_y = {}
height = 1080
width = 1920

def detect_target(filepass):
    filepass="C:/Users/delic/Downloads/200cm.jpg"
    img=cv2.imread(filepass)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask1=cv2.inRange(hsv,low_color1,high_color1)
    mask2=cv2.inRange(hsv,low_color2,high_color2)
    mask=mask1+mask2                              #マスク作成
    masked_img=cv2.bitwise_and(img,img,mask=mask)

    gray=cv2.cvtColor(masked_img,cv2.COLOR_BGR2GRAY)
    _,binary=cv2.threshold(gray,0,255,cv2.THRESH_OTSU)

    temp = np.where(binary==255)                  #座標取得
    coordinates_x["top"] = temp[1][0]
    coordinates_y["top"] = temp[0][0]
    binary = cv2.rotate(binary,cv2.ROTATE_90_CLOCKWISE)

    temp = np.where(binary==255)
    coordinates_x["left"] = temp[0][0]
    coordinates_y["left"] = abs(height-temp[1][0])
    binary = cv2.rotate(binary,cv2.ROTATE_90_CLOCKWISE)
    binary = cv2.rotate(binary,cv2.ROTATE_90_CLOCKWISE)

    temp = np.where(binary==255)
    coordinates_x["right"] = abs(width-temp[0][0])
    coordinates_y["right"] = temp[1][0]

    cv2.line(img,(coordinates_x["top"],coordinates_y["top"]),(coordinates_x["right"],coordinates_y["right"]),(100,0,0),thickness=10,lineType=cv2.LINE_8,shift=0)
    cv2.line(img,(coordinates_x["right"],coordinates_y["right"]),(coordinates_x["left"],coordinates_y["left"]),(100,0,0),thickness=10,lineType=cv2.LINE_8,shift=0)
    cv2.line(img,(coordinates_x["left"],coordinates_y["left"]),(coordinates_x["top"],coordinates_y["top"]),(100,0,0),thickness=10,lineType=cv2.LINE_8,shift=0)
    
    cv2.imwrite("result.jpg",img)

detect_target("C:/Users/delic/Downloads/200cm.jpg")