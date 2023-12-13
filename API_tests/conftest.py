import random
import pytest
from faker import Faker


@pytest.fixture()
def get_fake_user_payload(fake):
    return {
        "name": fake.name(),
        "email": fake.email(),
        "gender": random.choice(["male", "female"]),
        "status": random.choice(["active", "inactive"])
    }


@pytest.fixture
def fake():
    fake = Faker()
    return fake
