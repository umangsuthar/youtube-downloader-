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
		vstreams = video.streams

		astreams = video.audiostreams

		return render_template('home.html', video = vstreams, videodet = video, audio = astreams)
	else:
		return "errorr"
	
		

if __name__ == "__main__":
	app.run(debug=True)
