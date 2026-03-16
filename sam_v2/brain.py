import requests
import json

class DedSecBrain:
       def __init__(self):
              self.url = "http://localhost:11434/api/generate"
              self.primary = "qwen2.5"
              self.shadow = "llama3.1"
       def query(self, user_input):
              
              #System prompt to keep AI in "Agentic mode"
            system_context = (
                  "You are SAM-V1, the DedSec system orchestrator. "
            "If the user wants to open an app, change volume, or check system status, "
            "reply ONLY with 'EXECUTE: [command_name]'. "
            "Available commands: open notepad, open calculator, open chrome, open vscode, "
            "shutdown, restart, lock, battery, volume up, volume down, mute, screenshot, "
            "joke, time, date, search for [topic], play [video]. "
            "If it's just a conversation, reply naturally."
            )

            payload = {
                  "model": self.primary,
                  "prompt": f"{system_context}\n\nuser: {user_input}" ,
                  "stream": False
            }

            try:
                  #Sentinel-v1: Monitor primary engine health
                  response = requests.post(self.url, json=payload ,timeout=5)
                  return response.json() ['response'], self.primary
            except:
                  #Aegis: Primary engine failed/timed out, switch to shadow
                  print("Sentinel : Primary Engine Timeout.Activating Aegis (Llama3.1)...")
                  payload["model"] = self.shadow
                  response = requests.post(self.url, json=payload)
                  return response.json()['response'], f"{self.shadow} (Aegis)"