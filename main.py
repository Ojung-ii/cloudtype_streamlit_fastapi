from fastapi import FastAPI, HTTPException, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware  # 이 부분을 추가하세요.
from pydantic import BaseModel
from typing import List


app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://192.168.50.98:8503"],  # Streamlit 앱의 주소를 명시하세요.
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/add")
def add_numbers(numbers: Numbers):
    return {"sum": numbers.num1 + numbers.num2}



@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    file_infos = []

    for file in files:
        # 파일 처리
        file_contents = await file.read()
        with open(file.filename, "wb") as f:
            f.write(file_contents)

        # 임베딩 처리 (예시)
        # 여기서 file_contents를 사용하여 필요한 임베딩 처리를 진행합니다.
        # 예를 들어, 이미지 파일의 경우, 여기에서 이미지 임베딩 처리를 할 수 있습니다.
        
        # 파일 정보 저장
        file_infos.append({"filename": file.filename, "content_type": file.content_type})

    return {"uploaded_files": file_infos}