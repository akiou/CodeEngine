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

@app.get("/parroting_back")
async def parroting_back_get(request: Request, json_data: dict):
    logger.info("parroting_back GET API is invoked.")
    headers = request.headers
    logger.info(f"{headers=}")
    logger.info(f"{json_data=}")
    return json_data

@app.post("/parroting_back")
async def parroting_back_post(request: Request, json_data: dict):
    logger.info("parroting_back POST API is invoked.")
    headers = request.headers
    logger.info(f"{headers=}")
    logger.info(f"{json_data=}")
    return json_data
