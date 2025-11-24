from pydantic import BaseModel

class signUp(BaseModel):
    name: str
    email: str
    pw: str
