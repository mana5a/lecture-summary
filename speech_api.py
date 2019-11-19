# import os
# import time
# from google.cloud import speech_v1

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vaulted-scholar-254612-9bbd50992c2e.json'


# def callback(operation_future):
# 	result = operation_future.result()
# 	progress = operation.metadata.progress_percent
# 	print(result)
# 	return (result,progress)

# def transcribe():
# 	client = speech.SpeechClient()
# 	audio = speech.types.RecognitionAudio(uri='gs://fruitvodka123/audio-file.flac')
# 	config = speech.types.RecognitionConfig(encoding=speech.enums.RecognitionConfig.AudioEncoding.FLAC,language_code='en-US', sample_rate_hertz=44100,enable_automatic_punctuation=True)
# 	operation = client.long_running_recognize(config=config, audio=audio)
# 	#op_result = operation.result()
# 	operation.add_done_callback(callback)
# 	print(operation)

# 	progress = 0

# 	while progress < 100:
# 		try:
# 			progress = operation.metadata.progress_percent
# 			print('Progress: {}%'.format(progress))
# 		except:
# 			pass
# 		finally:
# 			time.sleep(5)


# 	result_full_transcript=[]

# 	for result in operation.results:
# 		for alternative in result.alternatives:
# 			#print('=' * 20)
# 			#print(alternative.transcript)
# 			result_full_transcript.append(alternative.transcript)
			
# 	print('\n'.join(result_full_transcript))
# 	return result_full_transcript

# #transcribe()


import time
import os
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vaulted-scholar-254612-9bbd50992c2e.json'


# credentials = GoogleCredentials.get_application_default()


def transcribe():
	client = speech_v1.SpeechClient()
	encoding = enums.RecognitionConfig.AudioEncoding.FLAC
	sample_rate_hertz = 44100
	language_code = 'en-US'
	config = {'encoding': encoding, 'sample_rate_hertz': sample_rate_hertz, 'language_code': language_code}
	uri = 'gs://fruitvodka123/solarpanels1.flac'
	audio = {'uri': uri}
	#global res
	response = client.long_running_recognize(config, audio)
	

	def callback(operation_future):
		result = operation_future.result()
		progress = response.metadata.progress_percent
		print(result)
		result_full_transcript=[]
		for i in result.results:
			for alternative in i.alternatives:
				result_full_transcript.append(alternative.transcript)
		#return result_full_transcript
			

		

	response.add_done_callback(callback)
	#print(response)
	#print(response.metadata.progress_percent)
	return response


	# def callback(operation_future):
	# 	#global response
	# 	result = operation_future.result()
	# 	progress = response.metadata.progress_percent
	# 	print(result)
		
	# response.add_done_callback(callback)

	# progress = 0

	# while progress < 100:
	# 	try:
	# 		progress = response.metadata.progress_percent			
	# 		print('Progress: {}%'.format(progress))
	# 		return progress
	# 	except:
	# 		pass
	# 	finally:
	# 		time.sleep(2)