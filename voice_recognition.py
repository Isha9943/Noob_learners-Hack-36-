import speech_recognition as sr



def recognize_speech(recognizer, microphone):
    
    
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

   
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source)


    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        
        response["success"] = False
        response["error"] = "API unavailable/unresponsive"
    except sr.UnknownValueError:
        
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    recognizer = sr.Recognizer()
    while (True):
        mic = sr.Microphone(device_index=1)
        response = recognize_speech(recognizer, mic)
        print(response['transcription'])
    
    