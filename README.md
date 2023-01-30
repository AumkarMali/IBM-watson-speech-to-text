


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


# IBM watson speech to text

Utilizes IBM watson's API to convert microphone detected speech into text.
 
  
## Deployment

Get API key at 

- shorturl.at/dknuP

Download python packages

```bash
    pip install playsound
    pip install ibm-watson
```

Replace 'API KEY' with your api-key. Replace "hello world" with desired text. Run following code with "python main.py." text.mp3 will contain the spoken text.

```bash
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
```
## Links

➊ Github: https://github.com/AumkarMali/

➋ Youtube: https://www.youtube.com/channel/UC7rhCKur9bF01lV0pNJNkvA
## Demo

https://www.youtube.com/watch?v=fAG7JvjMMmk

## Documentation

[Documentation](https://cloud.ibm.com/developer/watson/documentation)


## Authors

- [@AumkarMali](https://www.github.com/AumkarMali)

