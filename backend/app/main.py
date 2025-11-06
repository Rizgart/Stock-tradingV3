from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import alerts, recommendations, reporting, watchlists
from .core.logging import configure_logging
from .core.settings import Settings


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or Settings()
    configure_logging(settings)

    app = FastAPI(title="Stock Trading Backend", version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(recommendations.router, prefix="/api")
    app.include_router(watchlists.router, prefix="/api")
    app.include_router(alerts.router, prefix="/api")
    app.include_router(reporting.router, prefix="/api")

    @app.get("/health", tags=["health"])
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
