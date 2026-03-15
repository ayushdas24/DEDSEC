from modules import voice, apps, system, web, fun  

voice.speak("All systems online, sir. How may I assist?")  

while True:  
    command = voice.listen(timeout=15)  

    if command is None:    
        voice.speak("I didn't hear anything. Can you say that again")    
        continue    

    if "exit" in command or "quit" in command:    
        voice.speak("Goodbye! stay safe sir.")    
        break    

    if apps.handle_apps(command): continue    
    if "shutdown" in command: system.shutdown(); continue    
    if "restart" in command: system.restart(); continue    
    if "lock" in command: system.lock_system(); continue    
    if "battery" in command or "status" in command: system.system_status(); continue    
    if "volume up" in command: system.volume_up(); continue    
    if "volume down" in command: system.volume_down(); continue    
    if "mute" in command: system.mute_volume(); continue    
    if "search for" in command or "look up" in command: web.search_web(command); continue    
    if "play" in command: web.youtube_play(command); continue    
    if "search" in command: web.google_search(command); continue    
    if "screenshot" in command: fun.take_screenshot(); continue    
    if "joke" in command or "joker" in command: fun.tell_jokes(); continue    
    if "time" in command: fun.tell_time(); continue    
    if "date" in command: fun.tell_date(); continue    

    voice.speak("Sorry, I couldn't do that.")
