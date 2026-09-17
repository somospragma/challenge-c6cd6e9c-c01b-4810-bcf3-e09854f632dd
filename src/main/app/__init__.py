from.core import get_db
from.api import router

app = FastAPI()

app.include_router(router)