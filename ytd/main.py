from flask import Flask ,render_template, request
import pafy

app = Flask(__name__)

@app.route('/')
def data():
	return render_template('index.html')
	
	

@app.route('/home',methods=['POST', 'GET'])
def main():
	if request.method=='POST':
		url= request.form['u']
		video = pafy.new(url)
		streams = video.streams
		return render_template('home.html', a1 = streams)

	# url = "https://youtu.be/r9aE5gNSXxA"
	
		

if __name__ == "__main__":
	app.run(debug=True)