from fastapi import FastAPI, APIRouter
from lmos_openai_types import CreateChatCompletionRequest, CreateCompletionRequest
from lifespan import lifespan


__all__ = [
    "app",
]

app = FastAPI(
    title="exl2 runner lite",
    lifespan=lifespan,
)

router = APIRouter(prefix="/v1")


@router.post("/completions")
async def completions(data: CreateCompletionRequest):
    pass


@router.post("/chat/completions")
async def chat_completion(data: CreateChatCompletionRequest):
    pass


app.include_router(router)
