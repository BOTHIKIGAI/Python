from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello world</h1>"


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    response = make_response()
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response


@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"


@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'{number1} + {number2} = {number1 + number2}'


@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return 'Some parameters are missing'


@app.route('/length/<int:data>')
def get_data(data):
    try:
        if data > 0:
            return {'message': f'Your number is {data}'}
        else:
            return {'message': 'Data is empy'}, 500
    except NameError:
        return {'message': 'Data not found'}, 404


if __name__ == '__main__':
    app.run('127.0.0.1', port=5555, debug=True)
