from database.database import connection
# from fastapi import HTTPException
from repositories.repositories import GetAllUsers
import json

def GetUsers():
    # Example: Fetch item from MySQL database
    
    getUsers = GetAllUsers()
    
    return json.loads(json.dumps(getUsers))