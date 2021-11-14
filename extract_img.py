import cv2
import numpy as np
import pytesseract
import os
from PIL import Image
import streamlit as st

#*************************************************************************
per = 25
#roi = [[(1073, 95), (1199, 115), 'Text', 'Company_Name'],
 #      [(109, 350), (207, 378), 'Text', 'Invoice_Date'],
  #     [(994, 350), (1091, 378), 'Text', 'Invoice_Number'], 
   #    [(1000, 230), (1141, 246), 'Text', 'Mobile_Number']]

path= 'F1_invoices_AR1.JPG'
#img=cv2.imread(path)
myData =[]
configuration = ("-l eng --oem 3 --psm 12")

#*********************** Image Pre-Processing ****************************
def preprocess_image(img):
    print("Image Pre processing")
    img1=cv2.imread(img)
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #cv2.imwrite('processed_sample.jpg', threshold_img)
    return(threshold_img)

#************************ Data Extraction from Image ***********************

def extract_img(processed_img,roi):
    st.write("Data Extraction from Image")
    imgShow = processed_img.copy()
    st.image(imgShow)
    for x,r in enumerate(roi):
        cv2.rectangle(imgShow,((r[0][0]),r[0][1]),((r[1][0]),r[1][1]),(0,255,0),cv2.FILLED)
        #imgShow = cv2.addWeighted(imgShow,0.99,img,0.1,0)
        imgCrop = imgShow[r[0][1]:r[1][1],r[0][0]:r[1][0]]
        #cv2.imshow(str(x),imgCrop)
        if r[2] =='Text':
            print(f'{r[3]}:{pytesseract.image_to_string(imgCrop)}')
            myData.append(pytesseract.image_to_string(imgCrop))
        #cv2.putText(imgShow,str(myData[x]),(r[0][0],r[0][1]),cv2.FONT_HERSHEY_PLAIN,2.5,(0,0,255),4)

with open('DataOutput.csv','a+')as f:

    
    for data in myData:
        f.write((str(data)+ ','+'\t'))
    f.write('\n')
    
#cv2.imshow("Final Output",imgShow)
print(myData)



    