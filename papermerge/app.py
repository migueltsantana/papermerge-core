from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from papermerge.core.features.users.router import router as usr_router
from papermerge.core.features.tags.router import router as tags_router
from papermerge.core.features.groups.router import router as groups_router
from papermerge.core.features.document_types.router import router as dt_router
from papermerge.core.features.custom_fields.router import router as cf_router
from papermerge.core.features.nodes.router import router as nodes_router
from papermerge.core.features.nodes.router_folders import router as folders_router
from papermerge.core.features.nodes.router_thumbnails import router as thumbnails_router
from papermerge.core.features.document.router import router as document_router
from papermerge.search.routers.search import router as search_router

from papermerge.core.version import __version__
from papermerge.core.config import get_settings


config = get_settings()
prefix = config.papermerge__main__api_prefix
app = FastAPI(title="Papermerge DMS REST API", version=__version__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nodes_router, prefix=prefix)
app.include_router(folders_router, prefix=prefix)
app.include_router(thumbnails_router, prefix=prefix)
app.include_router(document_router, prefix=prefix)
app.include_router(dt_router, prefix=prefix)
app.include_router(cf_router, prefix=prefix)
app.include_router(usr_router, prefix=prefix)
app.include_router(tags_router, prefix=prefix)
app.include_router(groups_router, prefix=prefix)

if config.papermerge__search__url:
    app.include_router(search_router, prefix=prefix)