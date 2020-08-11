import pytest
import json
from tasks.setUpDriver import Initiate


@pytest.fixture(scope="class", autouse=True)
def driver_init(request):

    with open("configuartionFiles/config.json") as config_file:
        data = json.load(config_file)

    if data['browser'] == "Chrome":
        url = data["url"]
        driver = Initiate.tear_up(url)
        request.cls.driver = driver
    else:
        print("select a browser")

    yield driver
    Initiate.tear_down(request.cls.driver)

