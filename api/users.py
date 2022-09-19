from typing import Optional

import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@router.get('/users', response_model=list[User])
async def get_users():
    return users


@router.post('/users')
async def create_users(user: User):
    users.append(user)
    return {'message': f'Hello {user.email}'}


@router.get('/users/{id_}')
async def get_items(id_: int):
    return {"user": users[id_]}
