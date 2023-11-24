import pytest
from constants import ROOT_PATH
from db.sqlite_pack.products_repo import ProductsRepo


@pytest.fixture()
def products_repo(env):
    return ProductsRepo(f"{ROOT_PATH}{env.dp.param['path']}")

