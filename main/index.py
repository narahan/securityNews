


# flask 모듈에서 Flask 클래스 임포트
from flask import Flask, render_template
from sqlite3 import connect

from boannews import getBoanData
from dailysecu import getDailyData






# Flask 객체의 인스턴스를 만들고 'app'에 할당
app = Flask(__name__)




# # 보안뉴스 크롤링 데이터
boan_data = getBoanData()

# # 데일리시큐 크롤링 데이터
daily_data = getDailyData()


# 1. 현재 클릭한게 어떤 탭인지 알 수 있는 방법
# 2. 현재 클릭한 탭의 데이터 가져오기
# News.Vars.flag = 2

flag = 2

@app.route('/')
def index():
	if flag == 1:
		return render_template('index.html', data = boan_data)
	else:
		return render_template('index.html', data = daily_data)
	



# 배포판에서는 하단 삭제
if __name__ == '__main__':
	app.run(debug=True)

