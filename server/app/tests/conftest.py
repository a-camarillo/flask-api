import os
import pytest

from server import create_app
from server.models import Beer, Brand

@pytest.fixture(scope='module')
def new_beer():
    beer = Beer('Wahoo','Ballast Point',4.5)
    return beer