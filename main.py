from playsound import playsound
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

print("running...")
authenticator = IAMAuthenticator('API KEY')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('URL')

with open('text.mp3','wb') as audio_file:
    audio_file.write(text_to_speech.synthesize('hello world', voice='en-GB_CharlotteV3Voice', accept='audio/mp3').get_result().content)

playsound('text.mp3')

