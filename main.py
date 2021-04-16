from playsound import playsound
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

print("running...")
authenticator = IAMAuthenticator('oyiANbf6-ThDJWtdXYBb0mwcjRQ-hs4g0mVewXBtf2Px')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/a3d56947-b80d-4b9b-bd3d-b86866b82ab7')

with open('text.mp3','wb') as audio_file:
    audio_file.write(text_to_speech.synthesize('hello world', voice='en-GB_CharlotteV3Voice', accept='audio/mp3').get_result().content)

playsound('text.mp3')

