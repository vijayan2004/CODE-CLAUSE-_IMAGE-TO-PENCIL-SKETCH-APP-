import streamlit as st

import cv2
import matplotlib.pyplot as plt
plt.style.use('seaborn')

img = st.file_uploader("Select a Image",type=['jpg','png','webp'])

if st.button('Submit'):
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  img_invert = cv2.bitwise_not(img_gray)
  img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
  final = cv2.divide(img_gray, 255 - img_smoothing, scale=255)
  plt.figure(figsize=(8,8))
  plt.imshow(final,cmap="gray")
  plt.axis("off")
  plt.title("Final Sketch Image")
  st.pyplot(plt.show())


#img = cv2.imread("C:\\Users\\GF LAB\\Pictures\\1025273-capts.webp")

#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#plt.figure(figsize=(8,8))
#plt.imshow(img)
#plt.axis("off")
#plt.title("Original Image")
#plt.show()

