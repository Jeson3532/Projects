from fastapi import FastAPI
import uvicorn

from src.api.routers import routers
app = FastAPI(title="PC Club API")

for router in routers:
    app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)