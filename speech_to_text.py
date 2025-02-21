import speech_recognition as sr

def speech_to_text():
     r = sr.Recognizer()
     with sr.Microphone() as source:
         audio = r.listen(source)
         print("Listening...")
     try:
         voice_data = ""
         voice_data = r.recognize_google(audio)
         print(voice_data)
         return voice_data
     except sr.UnknownValueError:
        #  print("Error")        
         return "Sorry, I did not understand."
     except sr.RequestError:
        #  print("Request Error")
         return "Sorry, there was an issue with the request."  
            
# speech_to_text()  






               
            
# import speech_recognition as sr

# def get_voice_command():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening for a command...")
#         audio = recognizer.listen(source)
    
#     try:
#         command = recognizer.recognize_google(audio)
#         print("You said:", command)
#         return command
#     except sr.UnknownValueError:
#         print("Sorry, I could not understand the audio.")
#         return None
#     except sr.RequestError:
#         print("Could not request results from Google Speech Recognition service.")
#         return None
            


