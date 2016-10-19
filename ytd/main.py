from flask import Flask ,render_template, request, url_for
import pafy

app = Flask(__name__)

@app.route('/')
def data():
	return render_template('index.html')
	
	

@app.route('/home',methods=['GET', 'POST'])
def main():
	if request.method=='POST':
		url= request.form['u']
		video = pafy.new(url)
		streams = video.streams
		return render_template('home.html', a1 = streams, video = video)
	else:
		return "errorr"
	
		

if __name__ == "__main__":
	app.run(debug=True)
