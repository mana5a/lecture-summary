import os
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vaulted-scholar-254612-a0766eabcf5e.json'


def transcribe():
	client = speech.SpeechClient()
	audio = speech.types.RecognitionAudio(uri='gs://fruitvodka123/audio-file.flac')
	config = speech.types.RecognitionConfig(encoding=speech.enums.RecognitionConfig.AudioEncoding.FLAC,language_code='en-US', sample_rate_hertz=44100,enable_automatic_punctuation=True)
	operation = client.long_running_recognize(config=config, audio=audio)
	op_result = operation.result()

	result_full_transcript=[]

	for result in op_result.results:
		for alternative in result.alternatives:
			#print('=' * 20)
			#print(alternative.transcript)
			result_full_transcript.append(alternative.transcript)
			
	print('\n'.join(result_full_transcript))
	return result_full_transcript

#transcribe()