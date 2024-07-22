from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"hello": "world"}

@app.get("/hy/")
async def hy1():
    return {"message" : "Hello"}

