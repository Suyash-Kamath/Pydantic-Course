from fastapi import FastAPI
import uvicorn


def main():
    print("Hi Suyash")
    uvicorn.run(app,host="0.0.0.0",port = 8000)


app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hi From VS Code"}

if __name__=="__main__":
    main()