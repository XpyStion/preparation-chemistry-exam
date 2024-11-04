from pydantic import BaseModel
from datetime import datetime


class PostIamTokenModel(BaseModel):
    iamToken: str
    expiresAt: datetime


class Message(BaseModel):
    role: str
    text: str


class Alternative(BaseModel):
    message: Message
    status: str


class Usage(BaseModel):
    inputTextTokens: str
    completionTokens: str
    totalTokens: str


class Result(BaseModel):
    alternatives: list[Alternative]
    usage: Usage
    modelVersion: str


class PostFoundationModelsV1CompletionModel(BaseModel):
    result: Result
