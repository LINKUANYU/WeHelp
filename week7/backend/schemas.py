from pydantic import BaseModel

class signUpIn(BaseModel):
    name: str
    email: str
    pw: str

class loginIn(BaseModel):
    email: str
    pw: str

class userOut(BaseModel):
    id: int
    name: str
    email: str