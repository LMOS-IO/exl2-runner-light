from contextlib import asynccontextmanager

from lmos_config import config

@asynccontextmanager
async def lifespan(app):

    await config.load_config_data()

    #################################
    yield
    #################################
