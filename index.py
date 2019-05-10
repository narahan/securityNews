


# flask 모듈에서 Flask 클래스 임포트
from flask import Flask, render_template
from data import Articles
import sqlite3

# Flask 객체의 인스턴스를 만들고 'app'에 할당	 
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html') 



if __name__ == '__main__':
	app.run(debug=True)

