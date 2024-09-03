from fastapi import FastAPI

# FastAPI 앱 생성
app = FastAPI()

# 요청 처리를 위한 엔드포인트
@app.get("/") # GET메서드로 / url을 호출할 수 있는 엔드포인트
def hello():
    return {"message:" "Hello FastAPI"} # JSON 형식으로 응답

# uvicorn main:app --reload