import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

from app.core.paths import ProjectPaths
from app.dashboard.router import router as dashboard_router

def create_app() -> FastAPI:
    """
    (V7.1) App Factory: 允许在测试环境下动态重新挂载静态资源逻辑。
    """
    # 确保基础目录存在
    ProjectPaths.ensure_dirs()

    app = FastAPI(
        title="PersonaOps Console API",
        description="Operational Dashboard API for autonomous persona pipelines.",
        version="1.0.0"
    )

    # 允许跨域
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 动态挂载静态资源：始终使用当前 ProjectPaths.ASSETS
    if os.path.exists(ProjectPaths.ASSETS):
        app.mount("/assets", StaticFiles(directory=ProjectPaths.ASSETS), name="assets")

    # 注册 Dashboard 路由
    app.include_router(dashboard_router)

    @app.get("/", response_class=FileResponse)
    async def root():
        static_index = os.path.join(os.path.dirname(__file__), "app", "dashboard", "static", "index.html")
        if os.path.exists(static_index):
            return static_index
        return {"message": "PersonaOps Dashboard API is running. (UI missing)"}
    
    return app

# 为生产环境提供默认实例
app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print(f"🚀 Starting Dashboard Server on http://localhost:{port}")
    uvicorn.run("dashboard_main:app", host="0.0.0.0", port=port, reload=True)
