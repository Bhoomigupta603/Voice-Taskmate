import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather
import os
import wikipedia
import pyjokes
import requests
import pytz
from datetime import datetime

# For storing reminders and to-do lists
reminders = []
to_do_list = []

def Action(data):
   user_data = speech_to_text.speech_to_text()

   if "what is your name" in user_data:
       text_to_speech.text_to_speech("My name is Voice Taskmate")
       return "My name is Voice Taskmate"     
     
   elif "hello" in user_data or "hye" in user_data:
       text_to_speech.text_to_speech("hey, ma'am How can I help you")
       return "hey, ma'am How can I help you"
   
   elif "good morning" in user_data:
       text_to_speech.text_to_speech("good morning ma'am, Rise and shine; new beginnings await.") 
       return "good morning ma'am, Rise and shine; new beginnings await."
  
   elif "good afternoon" in user_data:
       text_to_speech.text_to_speech("good afternoon ma'am,Keep going; the day is yours.") 
       return "good afternoon ma'am, Keep going; the day is yours."
  
   elif "good evening" in user_data:
       text_to_speech.text_to_speech("good evening ma'am, Reflect and recharge for tomorrow.") 
       return "good evening ma'am, Reflect and recharge for tomorrow." 
   
   elif "good night" in user_data:
       text_to_speech.text_to_speech("good night ma'am, Rest well; dreams fuel success.") 
       return "good night ma'am, Rest well; dreams fuel success."


   elif "time now" in user_data:        
        ist_timezone = pytz.timezone('Asia/Kolkata')    
        current_time = datetime.now(ist_timezone)            
        hour = current_time.hour % 12  # Convert hour to 12-hour format
        hour = 12 if hour == 0 else hour  # Handle midnight case (0 hour becomes 12)
        minute = current_time.minute
        am_pm = "AM" if current_time.hour < 12 else "PM"  # Determine AM/PM           
        Time = f"{hour} Hour : {minute} Minute {am_pm}"             
        text_to_speech.text_to_speech(Time)
        return Time 
   
   elif "play music" in user_data:
    # Open JioSaavn in the browser
    webbrowser.open("https://www.jiosaavn.com/")
    text_to_speech.text_to_speech("JioSaavn.com is now ready for you. Which genre would you like to play?")

    # Get user choice for the genre
    genres = ["Pop", "Rock", "Classical", "Bollywood"]
    genre = None
    while not genre:
        genre_choice = speech_to_text.speech_to_text().lower()
        for g in genres:
            if g.lower() in genre_choice:
                genre = g
                break
        if not genre:
            text_to_speech.text_to_speech("Please choose a genre from Pop, Rock, Classical, or Bollywood.")
    
    text_to_speech.text_to_speech(f"Okay, {genre}. Which musician would you like to listen to?")
    
    # Sample musicians (can be customized for each genre)
    musicians = {
        "Pop": ["Taylor Swift", "Ed Sheeran", "Adele", "Bruno Mars", "Billie Eilish", "Sabrina Carpenter", "Olivia Rodrigo", "Dua Lipa", "Rihanna", "Lana Del Rey", "Bruno Mars", "Lady Gaga", "Beyonce", "Shakira", "BTS", "Justin Bieber"],
        "Rock": ["Linkin Park", "Queen", "Nirvana", "The Beatles", "Red Hot Chili Peppers", "Pearl Jam"],
        "Classical": ["Lata Mangeshkar", "Kishore Kumar", "Beethoven", "Mozart"],
        "Bollywood": ["Arijit Singh", "Shreya Ghoshal", "A.R. Rahman", "Badshah", "Monali Thakur", "Adnan Sami", "Amit Mishra", "Sachet Tandon", "Mohit Chauhan", "Yo-Yo Honey Singh", "Vijay Prakash", "Jubin Nautiyal", "Javed Ali", "Sonu Nigam", "Neha Kakkar", "Sunidhi Chauhan", "Dhvani Bhanushali", "Asees Kaur", "Tulsi Kumar", "Palak Muchhal", "Fateh Ali Khan", "Anuv Jain", "Darshan Rawal", "Vishal Mishra"]
    }
    
    musician = None
    while not musician:
        musician_choice = speech_to_text.speech_to_text().lower()
        for m in musicians[genre]:
            if m.lower() in musician_choice:
                musician = m
                break
        if not musician:
            text_to_speech.text_to_speech(f"Please choose a musician from {', '.join(musicians[genre])}.")
    
    # Now, directly open the musician's page on JioSaavn
    text_to_speech.text_to_speech(f"Opening {musician}'s page. Enjoy the music!")
    
    # Construct the search URL for the selected musician
    search_query = f"{musician}"
    musician_url = f"https://www.jiosaavn.com/artist/{search_query.replace(' ', '%20')}/songs"
    webbrowser.open(musician_url)  # This will open the musician's page
    
    return f"Opening {musician}'s page on JioSaavn."     
   
            

   elif "open YouTube" in user_data:
       webbrowser.open("https://www.youtube.com/")
       text_to_speech.text_to_speech("youtube.com is now ready for you ") 
       return "youtube.com is now ready for you "
          
   elif "open Google" in user_data:
       webbrowser.open("https://www.google.com/")
       text_to_speech.text_to_speech("google.com is now ready for you ") 
       return "google.com is now ready for you "  
  
   elif "weather" in user_data:
       text_to_speech.text_to_speech("Please tell me the city name.")
       city = speech_to_text.speech_to_text()
       weather_info = weather.get_weather(city)
       text_to_speech.text_to_speech(weather_info)
       return weather_info
    
   elif "set reminder" in user_data:
        text_to_speech.text_to_speech("What should I remind you about?")
        reminder = speech_to_text.speech_to_text()
        reminders.append(reminder)
        text_to_speech.text_to_speech(f"I've added the reminder: {reminder}")
        return f"Reminder set: {reminder}"
    
   elif "show reminders" in user_data:
        if reminders:
            text_to_speech.text_to_speech("Here are your reminders")
            return " | ".join(reminders)
        else:
            text_to_speech.text_to_speech("You have no reminders")
            return "No reminders set"
        
   elif "search Wikipedia" in user_data:
        text_to_speech.text_to_speech("What do you want to search?")
        query = speech_to_text.speech_to_text()
        result = wikipedia.summary(query, sentences=2)
        text_to_speech.text_to_speech(result)
        return result 
   
   elif "news" in user_data:
        url = "https://gnews.io/api/v4/top-headlines?country=in&token=aa269df9c20d9b64d7e0e0b3544d5415"
        response = requests.get(url)
        data = response.json()

        # Check if 'articles' key exists in the response
        if 'articles' in data and data['articles']:
            headlines = [article['title'] for article in data['articles'][:5]]  # Get top 5 headlines
            news = "\n".join(headlines)
            text_to_speech.text_to_speech("Here are the top news headlines for India today:")
            return news
        else:
            text_to_speech.text_to_speech("Sorry, I couldn't fetch the news.")
            return "Error fetching news."
    
#    elif "news" in user_data:
#         url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=13a5d842d58c4a91a779e70fbdb5ace2"
#         response = requests.get(url)
#         data = response.json()
#         headlines = [article['title'] for article in data['articles'][:5]]
#         news = "\n".join(headlines)
#         text_to_speech.text_to_speech("Here are the top news headlines")
#         return news 
    
   elif "tell me a joke" in user_data:
        joke = pyjokes.get_joke()
        text_to_speech.text_to_speech(joke)
        return joke
    
   elif "add to do list" in user_data:
        text_to_speech.text_to_speech("What task should I add?")
        task = speech_to_text.speech_to_text()
        to_do_list.append(task)
        text_to_speech.text_to_speech(f"I've added the task: {task}")
        return f"Task added: {task},{task}............{task}" 
   
   elif "show to do list" in user_data:
        if to_do_list:
            tasks = "\n".join(to_do_list)
            text_to_speech.text_to_speech("Here are your tasks")
            return tasks
        else:
            text_to_speech.text_to_speech("Your to-do list is empty, try to fill it!")
            return "To-do list is empty, try to fill it!"

   elif "open calculator" in user_data:
        os.system("calc")
        text_to_speech.text_to_speech("Calculator is now open, use it as for calculations!")
        return "Calculator is now open, use it as for calculations!"

   elif "open Notepad" in user_data:
        os.system("notepad")
        text_to_speech.text_to_speech("Notepad is now open, write to remember!")
        return "Notepad is now open,  write to remember!" 
   
   elif "open Microsoft Word" in user_data:
        os.system("start winword")
        text_to_speech.text_to_speech("Microsoft Word is now open, ready for writing!")
        return "Microsoft Word is now open,  ready for writing!"

   elif "open Microsoft PowerPoint" in user_data:
        os.system("start powerpnt")
        text_to_speech.text_to_speech("Microsoft PowerPoint is now open, make something presentable!")
        return "Microsoft PowerPoint is now open, make something presentable!"

#    elif "open PyCharm" in user_data:
#         os.system("start pycharm")
#         text_to_speech.text_to_speech("PyCharm is now open")
#         return "PyCharm is now open"

#    elif "open idle" in user_data:
#         os.system("start idle")
#         text_to_speech.text_to_speech("Python IDLE is now open")
#         return "Python IDLE is now open"

   elif "open lead code" in user_data:
        webbrowser.open("https://leetcode.com/problemset/")
        text_to_speech.text_to_speech("LeetCode is now open, Go for your coding practice!")
        return "LeetCode is now open,  Go for your coding practice!"

   elif "open hackerrank" in user_data:
        webbrowser.open("https://www.hackerrank.com/")
        text_to_speech.text_to_speech("HackerRank is now open for you, it's time to code!")
        return "HackerRank is now open for you, it's time to code!"

   elif "open w3school" in user_data:
        webbrowser.open("https://www.w3schools.com/")
        text_to_speech.text_to_speech("W3Schools is now open. Ready to study!")
        return "W3Schools is now open, Ready to study!"

#    elif "open Javatpoint" in user_data:
#         webbrowser.open("https://www.javatpoint.com/")
#         text_to_speech.text_to_speech("JavaTpoint is now open")
#         return "JavaTpoint is now open"

   elif "open exam videos" in user_data:
       webbrowser.open("https://www.youtube.com/results?search_query=exam+preparation+videos")
       text_to_speech.text_to_speech("Exam preparation videos are now ready for you, Go for it.You can do it!")
       return "Exam preparation videos are now ready for you, Go for it.You can do it!"

   
   elif "motivate me" in user_data:
        url = "https://api.quotable.io/random"
        response = requests.get(url, verify=False).json()  # Disable SSL verification
        quote = f"{response['content']} - {response['author']}"
        text_to_speech.text_to_speech(quote)
        return quote 
   
   elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok ma'am, It was nice to connect with you!")  
        return "ok ma'am, It was nice to connect with you!"
   
   
   else:
       text_to_speech.text_to_speech("Could you please repeat again? I'm not able to understand.") 
       return "I'm not able to understand"                                                                      
    


#    elif "volume up" in user_data:
#         os.system("nircmd.exe changesysvolume 5000")
#         text_to_speech.text_to_speech("Volume increased")
#         return "Volume increased"

#    elif "volume down" in user_data:
#         os.system("nircmd.exe changesysvolume -5000")
#         text_to_speech.text_to_speech("Volume decreased")
#         return "Volume decreased"      
 
 
   