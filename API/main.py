from fastapi import FastAPI
import uvicorn

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

@app.get("/input_name2")
def input_name2(name,last_name):
    data = "{} {}".format(name,last_name)
    return data

@app.get("/physics")
def physics(s,t):
    v= float(s)/float(t)
    data = "v= {:.2f}".format(v)
    return data

@app.get("/resistance_parallel_series")
def resistance_parallel_series(R1,R2,R3):
    parallel= float(R1)+float(R2)+float(R3),
    series = float(1/R1)+float(1/R2)+float(1/R3)**-1
    Rt = parallel,series
    data = "Rt= {:.2f}".format(Rt)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="172.20.10.3", port=8080)
