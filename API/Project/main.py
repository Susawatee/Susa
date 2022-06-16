from fastapi import FastAPI
import uvicorn

from action import Action
a = Action

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/my_name")
def my_name():
    data = "Susawatee Sama-ae"
    return data


@app.get("/input_name")
def input_name(name):
    data = name
    return data


@app.get("/input_name")
def input_name(name, last_name):
    data = "{} {}".format(name, last_name)
    return data


@app.get("/physics")
def physics(s, t):
    v = float(s) / float(t)
    data = "v = {:.2f}".format(v)
    return data


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

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.0.105", port=80)