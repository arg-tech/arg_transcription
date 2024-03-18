# Audio Transcription Service

This application provides an API for transcribing audio files into text format using state-of-the-art speech recognition models. It leverages the Facebook Wav2Vec2 model for accurate transcription.

## Functionality

The service allows users to upload audio files and receive the transcription results in xAIF format.

## Endpoints

### /transcribe

- **Methods**: GET, POST
- **Description**: 
  - **POST**: Accepts an audio file upload and transcribes it into text format. Returns the transcription result in xAIF format.
  - **GET**: Provides information about the service and its usage.

## Usage

To transcribe an audio file, users can send a POST request to the `/transcribe` endpoint with the audio file attached. The service will process the audio file and return the transcription result in xAIF format.


## Dependencies

The service relies on the following components:
- `Flask`: For creating the RESTful API.
- `transformers`: For utilizing the Facebook Wav2Vec2 model for speech recognition.
- `src.audio`: AudioTranscriber class for audio transcription tasks.

## Example Usage

### POST Request

```bash
curl -X POST -F "file=@/path/to/audio_file.wav" http://localhost:5001/transcribe
