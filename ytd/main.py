from flask import Flask ,render_template
import pafy

app = Flask(__name__)

@app.route('/')
def main():
	a = []
	url = "https://youtu.be/A4KYoQKAnoE"
	video = pafy.new(url)
	streams = video.streams
	
	return render_template('home.html', a1 = streams)

if __name__ == "__main__":
	app.run(debug=True)