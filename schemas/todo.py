from pydantic import BaseModel, Field
from typing import Optional

# Todo 아이템을 저장할 리스트
todos = []

# pydantic 스키마 생성
class Todo(BaseModel):
    id: Optional[int] = Field(None, json_schema_extra={
        "example": 1
    })
    title: str = Field(..., json_schema_extra={
        "example": "집에 가다가 마트에서 재료 사기"
    })
    done: bool = Field(False, json_schema_extra={
        "example": False
    })
    # 한꺼번에도 가능
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "집에 가다가 마트에서 재료 사기",
                "done": False
            }
        }
