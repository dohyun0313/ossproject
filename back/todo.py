from fastapi import APIRouter, Path
from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel):
    id: str
    item: str
    timestamp: datetime = None  # 타임스탬프 필드 추가, 기본값은 None

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo.timestamp = datetime.now()  # 현재 시간으로 타임스탬프 설정
    todo_list.append(todo)
    return {
        "msg": "todo가 성공적으로 추가되었습니다."
    }

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todos": todo_list
    }

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: str = Path(..., title="조회할 todo의 ID")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"msg": "제공된 ID의 todo가 존재하지 않습니다."}

@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: str = Path(..., title="삭제할 todo의 ID")) -> dict:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            del todo_list[index]
            return {"msg": f"ID가 {todo_id}인 todo가 성공적으로 삭제되었습니다."}
    return {"msg": "제공된 ID의 todo가 존재하지 않습니다."}
