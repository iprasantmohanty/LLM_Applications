import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() #loading all environment variables
from  PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,image):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None: #check if the file uploaded
        bytes_data=uploaded_file.getvalue() #read the file into bytes

        image_parts=[
            {
                "mime_type":uploaded_file.type, #get the mime type of uploaded file
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

##streamlit app front-end
st.set_page_config(page_title="Calories Count APP")
#input=st.text_input("Input Prompt: ",key="input")
st.header("Calories Count APP")
uploaded_file=st.file_uploader("Choose a food (thali) image ",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Food",use_column_width=True)

submit=st.button("Count my total Calories")

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
Finally, you can also mention wheather the food is healthy or not and also mention percentage split of the ratio of 
carbohydrate, fats, protine, fiber, sugarand other important things required for my diet.

"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.header("The Response is")
    st.write(response)