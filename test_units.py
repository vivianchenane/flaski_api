from app import app

def test_login_page():
    print("testing if login page is loading")
    test_page_load = app.test_client()
    response = test_page_load.get('/loginn')
    assert response.status_code ==404

def test_login_page_pass():
    print("testing if login page is loading")
    test_page_load = app.test_client()
    response = test_page_load.get('/login')
    assert response.status_code == 405

def test_login_correct_login_details(): 
    print("testing if login page is loading") 
    test_login = app.test_client()
    response = test_login.post('/login' ,data = {'username': 'user', 'password': 'user'})
    print(response)
    assert response.status_code == 200