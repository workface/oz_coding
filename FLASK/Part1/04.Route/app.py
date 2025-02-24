from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, This is main page!"

@app.route('/about')
def about():
    return "Hello, This is about page!"

#동적으로 URL 파라미터 값을 받아서 처리해 준다.
#http://127.0.0.1:5000/user/soomin
@app.route('/user/<username>')
def user_profile(username):

    return f'UserName : {username}'

@app.route('/number/<int:number>')
def number(number):

    return f'Number : {number}'

# post요청 날리는법
# (1) postman
# (2) requests
import requests

@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url, data=data)
    
    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)
    
    if request.method == 'GET':
        print('GET method')
    if request.method == 'POST':
        print('*** POST method ***', request.data)

    return Response('successfully submitted', status=200)

if __name__=="__main__":
    app.run()