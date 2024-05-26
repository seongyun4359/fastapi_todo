from fastapi import FastAPI
from todo import todo_router # added
import uvicorn

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "msg" : "hello world?"
    }

app.include_router(todo_router)  # added

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
