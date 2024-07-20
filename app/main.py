from fastapi import FastAPI, Depends
import uvicorn

from app.router import router

app = FastAPI()

app.include_router(router.router, prefix='/api')

if __name__ == '__main__':
    uvicorn.run()
