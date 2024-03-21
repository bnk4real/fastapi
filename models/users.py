from pydantic import BaseModel
# from typing import Dict

class User(BaseModel):
    userid: int
    uuid: str
    email: str
    username: str
    password: str
    firstname: str
    lastname: str
    
# db: Dict[int, User] = {}