from flask import Flask, request, send_file
from src.utility import get_file
from src.audio import  AudioTranscriber
import logging


#logging configuration
logging.basicConfig(datefmt='%H:%M:%S',
                    level=logging.DEBUG)

app = Flask(__name__)	
@app.route('/transcribe', methods = ['GET', 'POST'])
def get_transcription():
	if request.method == 'POST':
		file_obj = request.files['file']
		f_name = get_file(file_obj)
		transcriber = AudioTranscriber()
		return transcriber.audio_transcribe(f_name)
	if request.method == 'GET':
		info = """Takes audio file, transcribe and retun the result in xAIF format"""
		return info	
	
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5001"), debug=False)	  
