from fastapi import FastAPI

from api import users, courses, sections
from db.db_setup import engine
from db.models import course, user

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses",
    version="0.0.1",
    contact={
        "name": "Warui",
        "email": "#@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)


app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
