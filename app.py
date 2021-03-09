from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template('add_user.html')
    if request.method == 'POST':
        print(request.values['name'])
        print(request.values['password'])
        return 'post获取到' + request.values['name']


@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return render_template('user.html')
    if request.values['send'] == "allData":
        return jsonify([
            {
                "id": 1,
                "name": "燕怡楠",
                "role": "管理员",
                "password": "123"
            },
            {
                "id": 2,
                "name": "韦永剑",
                "role": "操作员",
                "password": "123"
            },
            {
                "id": 3,
                "name": "王梦圆",
                "role": "操作员",
                "password": "123"
            }
        ])


@app.route('/grant', methods=['GET', 'POST'])
def grant():
    if request.method == 'GET':
        return render_template('grant.html')
    if request.method == 'POST':
        print(request.values['role'])
        print(request.values['role'])
        return 'post获取到' + request.values['role']


@app.route('/distribution', methods=['GET', 'POST'])
def distribution():
    if request.method == 'GET':
        return render_template('distribution.html')
    if request.values['send'] == "allData":
        return jsonify([
            {
                "id": 1,
                "name": "没有王八的世界",
                "time": "2020/12/1",
                "countersign": ["派特三石", "五虎上将"],
                "approval": ["派特三石", "五虎上将"],
                "sign": ["派特三石", "五虎上将"]
            },
            {
                "id": 2,
                "name": "没有派特三石的世界",
                "time": "2020/12/2",
                "countersign": ["王八", "五虎上将"],
                "approval": ["王八", "五虎上将"],
                "sign": ["王八", "五虎上将"]
            },
            {
                "id": 3,
                "name": "没有五虎上将的世界",
                "time": "2020/12/3",
                "countersign": ["王八", "五虎上将"],
                "approval": ["王八", "五虎上将"],
                "sign": ["王八", "五虎上将"]
            }
        ])


@app.route('/distribution_user', methods=['GET', 'POST'])
def distribution_user():
    if request.method == 'GET':
        return render_template('distribution_user.html')
    if request.values['send'] == "allData":
        return jsonify([
            {
                "name": "没有王八的世界",
                "countersign": ["派特三石", "五虎上将"],
                "approval": ["派特三石", "五虎上将"],
                "sign": ["派特三石", "五虎上将"]
            },
            {
                "name": "没有派特三石的世界",
                "countersign": ["王八", "五虎上将"],
                "approval": ["王八", "五虎上将"],
                "sign": ["王八", "五虎上将"]
            },
            {
                "name": "没有五虎上将的世界",
                "countersign": ["王八", "五虎上将"],
                "approval": ["王八", "五虎上将"],
                "sign": ["王八", "五虎上将"]
            }
        ])


@app.route('/modify_user', methods=['GET', 'POST'])
def modify_user():
    if request.method == 'GET':
        return render_template('modify_user.html')


if __name__ == '__main__':
    app.run()
