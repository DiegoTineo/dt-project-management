from fastapi import Depends, FastAPI
from app.decorators.jwt import get_token_header, token_required
from app.routes.users import users_router
from app.routes.organizations import organizations_router
from app.routes.projects import projects_router
from app.routes.sprints import sprints_router
from app.routes.Tasks import task_router
from app.routes.subTasks import sub_task_router
from app.routes.taskStages import task_stage_router
from app.routes.userOrganizations import user_organization_router

app = FastAPI(
    title="FastAPI with SQLAlchemy and Fernet",
    description="This is a simple example of FastAPI with SQLAlchemy and Fernet",
    version="0.0.1",
    contact={
        "name": "Diego Tineo",
        "url": "https://example.com/contact",
        "email": "diegoatineoz@gmail.com",
    },
    openapi_tags=[
        {
            "name": "users",
            # "description": "Operations related to users",
        },
        {
            "name": "organizations",
        }
    ],
)

app.include_router(organizations_router)
app.include_router(projects_router)
app.include_router(sprints_router)
app.include_router(users_router)
app.include_router(task_router)
app.include_router(sub_task_router)
app.include_router(task_stage_router)
app.include_router(user_organization_router)


@app.get("/holaMiembros")
@token_required
def hola_miembros(token: str = Depends(get_token_header)):
    return {"message": "Access granted to protected route"}