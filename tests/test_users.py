from app import schemas

import pytest
from jose import jwt
from app.config import settings

 





#def test_root(client):
 #   res = client.get("/")
  #  print(res.json().get('messsage'))
   # assert res.status_code == 200
   
   
def test_create_user(client):
    res = client.post(
        "/users/", json={"email":"hello123@gmail.com", "password":"password123"})
    new_user = schemas.UserOut(**res.json())
    assert res.status_code==201
    
def test_login_user(client, test_user):
    res = client.post(
        "/login", data ={"username":test_user['email'], "password":test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key,algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type =="bearer"
    assert res.staus_code == 200
    
@pytest.mark.parametrize("email, password, status_code", [
    ('ann@gmail.com', 'Maria9598', 403),
    ('core@gmail.com','akinnto', 403),
    ('ann@gmail.com','akint,',403),
    (None, 'Maria9598',422),
    ('core@gmail.com',None, 422)
])   
def test_incorrect_login(test_user, client):
    res = client.post("/login",data={"username":test_user['email'],"password":"wongp0"})
    assert res.status_code == 403
    assert res.json().get('detail')== 'Invalid Credntials'
    