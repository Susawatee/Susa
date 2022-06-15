from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/resistance_parallel_series")
def resistance_parallel_series(R1:float,R2:float,R3:float):
    parallel= "paralel {:.2f}".format((1/R1)+(1/R2)+(1/R3)**-1)
    series = "series {:.2f}".format((R1)+(R2)+(R3))
    return parallel,series

if __name__ == "__main__":
    uvicorn.run(app, host="172.20.10.3", port=8080)