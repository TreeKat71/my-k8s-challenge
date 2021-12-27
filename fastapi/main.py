import sys
import socket
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger

ERROR_DICT = {0: ImportError, 1: SyntaxError, 2: TypeError}

app = FastAPI()
fmt = '{time:YYYY-MM-DD HH:mm:ss.SSS}|{level}|{name}:{function}:{line}-{message}'
# logger.add("/log/spam.log", level="DEBUG", format=fmt)
logger.add(sys.stderr, level="ERROR", format=fmt)


class Message(BaseModel):
    from_: str
    content: Optional[str] = None


@app.get('/')
async def hello_world():
    return "Hello World"


@app.get('/error')
async def error(num: int):
    mod = num % 3
    try:
        raise ERROR_DICT[mod]
    except Exception as e:
        error_type = e.__class__.__name__
        logger.error(error_type)
        return {"type": error_type}


@app.post('/leave_message/')
async def leave_message(message: Message):
    visitor = message.dict()['from_']
    text = message.dict()['content'] or "Says Nothing"
    node_name = socket.gethostname()
    logger.info(f'{visitor} visited {node_name} left message: "{text}"')
    return f'Hi {visitor}!, you visited {node_name}'
