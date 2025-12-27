from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = '12331212312123123123fds'

@app.route('/')
def index():
    
    first = input('Введите первый текст')
    second = input('Введите второй текст')
    
    return render_template('index.html', first=first, second=second)

if __name__ == '__main__':
    app.run(port=5500)