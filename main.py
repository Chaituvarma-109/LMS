from fastapi import FastAPI

from api import users, sections, courses

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

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
