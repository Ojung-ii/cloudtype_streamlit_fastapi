import streamlit as st
import requests

st.title("Addition App using FastAPI Backend")

num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

if st.button("Add"):
    response = requests.post("http://127.0.0.1:8000/add", json={"num1": num1, "num2": num2})
    if response.status_code == 200:
        result = response.json()["sum"]
        st.success(f"The sum of {num1} and {num2} is {result}")
    else:
        st.error("Error in API call")
else:
    st.write("Press the above button to calculate the sum")


files_pdf = st.file_uploader(
    label="""Upload document here.""", 
    type=['pdf', 'doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'txt'], 
    accept_multiple_files=True
    )
        
        

if files_pdf : 
    files = [("files", (file.name, file.getvalue())) for file in files_pdf]

    # Send files to FastAPI for processing
    response = requests.post("http://127.0.0.1:8000/upload", files=files)
    
    if response.status_code == 200:
        st.success("Files uploaded and processed successfully!")
        st.write(response.json()["uploaded_files"])
    else:
        st.error("Error during file processing.")