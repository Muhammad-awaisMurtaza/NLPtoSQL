from fastapi import APIRouter
from interactors import chat_interactor

router = APIRouter()

@router.post('/NLPtoSQL')
def chat(query: str):
  return chat_interactor.chat(query)
