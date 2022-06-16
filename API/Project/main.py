from fastapi import FastAPI
import uvicorn

from action import Action
a = Action

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_hard_ware3")
def get_hard_ware():
    data = a.gethard_ware3()
    return data


@app.get("/update_hard_ware3")
def update_hard_ware3(ID, status):
    data = a.updatehard_ware3(ID, status)
    return data

@app.get("/inserthard_ware3")
def inserthard_ware3(name, hw_name):
    data = a.inserthard_ware3(name, hw_name)
    return data
    
@app.get("/select_hard_ware3")
def select_hard_ware3(ID):
    data = a.selecthard_ware3(ID)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=80)