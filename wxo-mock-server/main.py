from logging import getLogger

from fastapi import FastAPI, Request


logger = getLogger("uvicorn.app")
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/callback/{correlation_id}")
async def callback_test_mock(request: Request, correlation_id: str, json_data: dict):
    logger.info("callback_test_mock API is invoked.")
    headers = request.headers
    logger.info(f"{correlation_id=}")
    logger.info(f"{headers=}")
    logger.info(f"{json_data=}")
    return {"success": True}
