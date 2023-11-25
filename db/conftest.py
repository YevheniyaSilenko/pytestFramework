import pytest
from constants import ROOT_PATH
from db.sqlite_pack.products_repo import ProductsRepo

@pytest.fixture(scope='module')
def products_repo(env):
    return ProductsRepo(f"{ROOT_PATH}{env.db_param['path']}")



@pytest.fixture()
def products_repo_pg(env):
    return ProductsPG(env.postgres_db)


@pytest.fixture()
def fake_employee(fake):
    data = {
        "user_id": fake.pyint(1000, 1000000),
        "name": fake.first_name(),
        "age": fake.pyint(18, 60),
        "address": fake.country(),
        "salary": float(fake.pyint(10000, 60000))
    }
    return data

