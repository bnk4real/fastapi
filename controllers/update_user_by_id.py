from fastapi import HTTPException
from services import get_user_by_id

def get_user_by_id_controller(user_id):
    # handle requests
    # handle response
    getUserById = get_user_by_id.GetUserById(user_id)
    if getUserById is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return getUserById