from fastapi import FastAPI
import uvicorn

from action import Action
a = Action

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_hard_ware")
def get_hard_ware():
    data = a.gethard_ware()
    return data


@app.get("/update_hard_ware")
def update_hard_ware(ID, status):
    data = a.updatehard_ware(ID, status)
    return data

@app.get("/inserthard_ware")
def inserthard_ware(name, hw_name):
    data = a.inserthard_ware(name, hw_name)
    return data
    
@app.get("/select_hard_ware")
def select_hard_ware(ID):
    data = a.select_hard_ware(ID)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)