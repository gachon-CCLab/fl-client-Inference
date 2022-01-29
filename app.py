from typing import Optional
from pydantic.main import BaseModel
import uvicorn
from fastapi import FastAPI

app = FastAPI()


class inference_status(BaseModel):
    infer_online:bool = True
    running: bool = False
    updating: bool = False


status = inference_status()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/start")
def get_start():
    global status
    status.running = True
    return status


@app.get("/update")
def get_update():
    global status
    status.updating = True
    return status

@app.get('/online')
def get_info():
    status.running = True
    return status


if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=8001, reload=True)
