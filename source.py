import streamlit as st
import numpy as np 
from PIL import Image 
import cv2 
from io import BytesIO

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def pencilsketch(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return(final_img)


st.title("Sketch My Pic")
st.write("This Web App is to help convert your photos to realistic Pencil Sketches") 

file_image = st.file_uploader(label = "Take a pic of you to be sketched out")

if file_image:
    input_img = Image.open(file_image)
    final_sketch = pencilsketch(np.array(input_img))
    one, two = st.columns(2)
    with one:
        st.write("**Input Photo**")
        st.image(input_img, use_column_width=True)
    with two:
        st.write("**Output Pencil Sketch**")
        st.image(final_sketch, use_column_width=True)


    buf = BytesIO()
    sketch_pil = Image.fromarray(final_sketch.astype('uint8'), 'L')
    sketch_pil.save(buf, format="JPEG")
    byte_img = buf.getvalue()
    if st.download_button("Download Sketch Images", byte_img, file_name="sketch.jpg", mime="image/jpeg"):
        im_pil = Image.fromarray(final_sketch)
        im_pil.save('final_image.jpeg')
        st.write('Download completed')
   

else:
     st.write("You haven't uploaded any image file")
