from fastapi import APIRouter, HTTPException
from controllers import get_user_ctrl
from controllers import update_user_by_id

router = APIRouter()

@router.get("/users/")
def read_all_users():
    return get_user_ctrl.get_user_controller()

# TODO
@router.post("/users/{user_id}")
def get_user_by_id(user_id):
    updated_user = update_user_by_id.get_user_by_id_controller(user_id)
    return updated_user