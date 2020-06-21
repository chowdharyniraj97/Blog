import requests





url='http://flask-sample:5000/'

def test_home():
    data=requests.get(url)
    print(data)
    assert data.status_code==200

def test_login():
    data={
        'email':'chowdharyniraj97@gmail.com',
        'password':'12345678'
    }
    response=requests.post(url+'login',json=data)
    print(response)
    assert response.status_code==200

def test_failed_login():
    data={
        'email':'chowdharyniraj97@gmail.com',
        'password':'123456789075'
    }
    response=requests.post(url+'login',json=data)
    assert response.status_code==404

def test_reset_password():
    data={
        'email':'chowdharyniraj97@gmail.com' #add your email id if you want to test
    }
    response=requests.post(url+'reset_password',json=data)
    assert response.status_code==200

def test_add_post():
    data={
        'email':'chowdharyniraj97@gmail.com',
        'title':'Testing',
        'content':'sending content from pytest'
    }
    response=requests.post(url+'post/new',json=data)
    assert response.status_code==200



