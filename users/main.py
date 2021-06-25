from fastapi import FastAPI
import models,user_routers,auth_routers,remote_routers
from database import engine

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(user_routers.router)
app.include_router(auth_routers.router)
app.include_router(remote_routers.router)



