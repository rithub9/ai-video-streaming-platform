import requests

def test_login():
    response = requests.post("http://localhost:8001/login", json={"username": "test", "password": "test"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_upload_video():
    files = {'file': open('sample.mp4', 'rb')}
    response = requests.post("http://localhost:8002/upload", files=files)
    assert response.status_code == 200
    assert "File uploaded successfully" in response.text

test_login()
test_upload_video()
