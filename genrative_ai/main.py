from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"hello": "world"}

@app.get("/hy/")
async def hy1():
    return {"message" : "Hello"}

@app.get("/how/")
async def hy2():
    return {"message" : "How are you?"}

@app.get("/bye/")
async def hy3():
    return {"message" : "Good Bye"}
