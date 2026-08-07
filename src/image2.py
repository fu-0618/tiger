import cv2
import numpy as np
from sklearn.cluster import DBSCAN

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

    temp= np.where(binary==255)                   #座標付与
    points = np.column_stack((temp[1], temp[0]))  #密集している座標を探す
    db = DBSCAN( eps=5, min_samples=20 ) 
    labels = db.fit_predict(points)
    valid_labels = labels[labels != -1]           #コーンのラベルだけ残す
    unique, counts = np.unique(valid_labels, return_counts=True)
    cone_label = unique[np.argmax(counts)]
    cone_points = points[labels == cone_label]

detect_target("C:/Users/delic/Downloads/200cm.jpg")    