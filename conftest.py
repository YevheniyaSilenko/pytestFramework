import pytest
import json
from constants import ROOT_PATH  # Замініть 'your_project' на відповідний шлях у вашому проекті
from db.sqlite_pack.products_repo import ProductsRepo  # Замініть 'your_project' на відповідний шлях у вашому проекті

@pytest.fixture(scope='session')
def env(request):
    _env_name = request.config.getoption('--env')
    return _env_name


@pytest.fixture(scope='module')
def products_repo(env):
    return ProductsRepo(f"{ROOT_PATH}{env.db_param['path']}")

@pytest.fixture()
def products_repo_pg(env):
    return ProductsPG(env.postgres_db)

def fake_ware(fake):
    data = {
        "age": fake.pyint(18, 60),
        "address": fake.country(),
        "salary": float(fake.pyint(10000, 60000))
    }
    return data

@pytest.fixture(scope='session')
def env(request):
   _env_name = request.config.getoption('--env')
   with open(f'{ROOT_PATH}/configs/{_env_name}.json') as f:
        conf_dict = json.loads(f.read())
        return DictToClass(**conf_dict)


