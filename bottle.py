from bottle import route, run, template

#@route('/hello/<name>')
#def index(name):
#	return template('<b> Test Bottle </b>', name=name)

@route('/http://localhost:8080/webCrawler')
@route('/Users/hannara/Desktop/CodingStudy/webCrawler/index')
def index():
	return 'test bottle'

run(host='localhost', port=8080)


