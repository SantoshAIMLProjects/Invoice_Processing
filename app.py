import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from extract_img import *
from PIL import Image

data = pd.read_csv("output1.csv")
st.title("Invoice Processing")
#roi = [[(1073, 95), (1199, 115), 'Text', 'Company_Name'],
 #      [(109, 350), (207, 378), 'Text', 'Invoice_Date'],
  #     [(994, 350), (1091, 378), 'Text', 'Invoice_Number'], 
   #    [(1000, 230), (1141, 246), 'Text', 'Mobile_Number']]

roi= [[(84, 74), (269, 92), 'Text', 'Company_Name'],
      [(89, 226), (252, 258), 'Text', 'Invoice_Number'],
      [(694, 226), (882, 257), 'Text', 'Invoice_Date'],
      [(133, 118), (225, 134), 'Text', 'Mobile_Number']]




def main():
    st.header("AI Invoice Processing")
    #st.write("Main function")
    
    nav = st.sidebar.radio("Navigation",['Home','Extract','Analytics'])
    if nav == 'Home':

        st.write("We are processing invoices and extracting some fileds and storing in Database.Also we verify with source system")

    elif nav == 'Extract':

        input_img = st.file_uploader("Please upload image file.....")
        if input_img is not None:

            img = Image.open(input_img)
            img_arr = np.array(img)
        
            img_gray = cv2.cvtColor(img_arr,cv2.COLOR_BGR2GRAY)
            threshold_img = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            #img = input_img.copy()
            #st.write(type(img_arr))
            st.image(img_arr,caption='Input Invoice')
            st.image(img_gray,caption='Gray Invoice')
            st.image(threshold_img,caption ='Threshold Image')

        #preprocess_img= preprocess_image(img_gray)
        #st.image(preprocess_img,caption='Pre-Processed Invoice')
        #st.image(preprocess_image(input_img))
            extract_img(threshold_img,roi)
        print("Data extraction completed")


    #path = st.file_uploader("Input the file path")
        option = st.selectbox("Please select one",("Eng_To_Eng","Eng_To_Ara","Ara_To_Ara","Ara_To_Eng"))
        if st.checkbox("Show Data"):
            st.table(data)
    elif nav == 'Analytics':
        st.write("We show analytics of our app")


    
    
if __name__ == '__main__':
    main()


