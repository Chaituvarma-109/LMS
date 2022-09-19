from typing import Optional

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title='Fast API LMS',
    description='LMS for managing students and courses',
    version='0.0.1',
    contact={
        'name': 'Gwe',
        'email': 'me@email.com',
    },
    license_info={
        'name': 'MIT',
    },
)

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get('/users', response_model=list[User])
async def get_users():
    return users


@app.post('/users')
async def create_users(user: User):
    users.append(user)
    return {'message': f'Hello {user.email}'}


@app.get('/users/{id_}')
async def get_items(
        id_: int = Path(..., description="The ID of the user you want to retrieve.", gt=2),
        q: str = Query(None, max_length=5)
):
    return {"user": users[id_], "query": q}
