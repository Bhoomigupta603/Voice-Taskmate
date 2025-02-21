#https://www.google.com/search?q=weather+dehradhun
# user agent -  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

#   span id = wob_tm 


# from requests_html import HTMLSession  
    

# def weather():
#     s = HTMLSession()
#     query = "dehradhun"
#     url = f'https://www.google.com/search?q=weather+{query}'
#     r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'})
#     temp = r.html.find('span#wob_tm', first= True).text
#     unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first= True).text
#     desc = r.html.find('span#wob_dc', first= True).text
#     return temp+" " + unit+" " + desc


import requests

def get_weather(city="Dehradun"):
    try:
        # Your API key from OpenWeatherMap
        api_key = "f437daab07595640229b19c8e81d8eb8"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        # Make the API call
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Parse the weather data
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            feels_like = data['main']['feels_like']

            # Formatted weather info
            weather_info = (f"The current temperature in {city} is {temp}°C, "
                            f"it feels like {feels_like}°C, "
                            f"with {description}.")
            return weather_info
        else:
            # Handle errors in API response
            error_message = data.get("message", "Unable to fetch weather information.")
            return f"Error: {error_message}"

    except Exception as e:
        # Handle any unexpected errors
        return f"Unable to fetch weather data. Error: {str(e)}"












# from requests_html import HTMLSession
# import speech_to_text


# def weather():
#     s = HTMLSession()
#     query = "Dehradhun"
#     url = f'https://www.google.com/search?q=weather+{query}'
#     r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'})
#     temp = r.html.find('span#wob_tm', first= True).text 
#     print(temp)
#     unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first= True).text
#     print(unit)
#     desc = r.html.find('span#wob_dc', first= True).text
#     print(desc)
#     return temp+" "+ unit+" "+ desc

# import requests

# def weather():
#     api_key = "f437daab07595640229b19c8e81d8eb8"  # Replace with your OpenWeatherMap API key
#     query = "Dehradun"
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}&units=metric"
    
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
        
#         # Extract necessary weather information
#         temp = data["main"]["temp"]
#         unit = "°C"
#         desc = data["weather"][0]["description"]
        
#         # Print or return the weather information
#         print(f"Temperature: {temp}{unit}")
#         print(f"Description: {desc}")
#     else:
#         print("Could not retrieve weather data")

# weather()


# import requests
# # import speech_recognition as sr  # Import speech_recognition directly
# import speech_to_text

# def weather(city):
#     api_key = "f437daab07595640229b19c8e81d8eb8"  # Replace with your OpenWeatherMap API key
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
        
#         # Extract necessary weather information
#         temp = data["main"]["temp"]
#         unit = "°C"
#         desc = data["weather"][0]["description"]
        
#         # Print the weather information
#         print(f"Temperature: {temp}{unit}")
#         print(f"Description: {desc}")
#     else:
#         print("Could not retrieve weather data")

# def weather():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Please say the city name...")
#         audio = recognizer.listen(source)
        
#         try:
#             # Convert speech to text
#             city = recognizer.recognize_google(audio)
#             print(f"You said: {city}")
            
#             # Get weather information for the spoken city
#             weather(city)
            
#         except sr.UnknownValueError:
#             print("Sorry, I could not understand the audio.")
#         except sr.RequestError:
#             print("Could not request results from the speech recognition service.")

# # Run the weather function
# weather()
