import random
import pytest
from faker import Faker

fake = Faker()


@pytest.fixture
def get_fake_user_payload(fake):
    return {
        "name": fake.name(),
        "email": fake.email(),
        "gender": fake.random_element(elements=('male', 'female')),
        "status": fake.random_element(elements=('active', 'inactive'))
    }


@pytest.fixture
def fake():
    fake = Faker()
    return fake


@pytest.fixture
def user_id_to_delete():
    return 1830492
