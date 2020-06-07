import pytest
import requests





url='http://localhost:5000/'

def test_testing():
    data=requests.get(url)
    print(data)
    assert data.status_code==200


