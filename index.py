


# flask 모듈에서 Flask 클래스 임포트
from flask import Flask, render_template
from boannews import getData




# Flask 객체의 인스턴스를 만들고 'app'에 할당
app = Flask(__name__)



# 보안뉴스 크롤링 데이터
boan_data = getData()



@app.route('/')
def index():
	return render_template('index.html', data = boan_data) 


if __name__ == '__main__':
	app.run(debug=True)

