"""
DedSec core engine
"""

import asyncio
import time
from datetime import datetime
from typing import Any , Dict , Optional

class DedSecEngine:
    """
    The brain of DedSec every message goes through here
    """
    def __init__(self):
        self.session_id = datetime.now() .strftime("%y%m%d_%H%M%S")
        self.active = False
        self.mode = "assistant"
        self.context: Dict[str , Any] = {}
        self.start_time = None

    async def initialize(self):
        """Boot up DedSec systems"""
        self.active = True
        self.start_time = time.time()
        print("[*] DedSec engine online...")
        print(f" [*] Session ID: {self.session_id}")

    async def process(self , user_input: str) -> str:
        """
        Main agentic loop every input goes through here
        """
         # Store what user said
        self.context["last_input"] = user_input
        self.context["timestamp"] = time.time()

        #check for mode switch
        mode_response = self._check_mode(user_input)
        if mode_response:
            return mode_response
    
        #For now return acknowledgement
        #later this calls planner -> executor -> reflector
        return f"[DEDSEC] Processing: {user_input}"
    def _check_mode(self, text :str) -> Optional[str]:
        """Detect if the user wants to swtich mode"""
        text_lower = text.lower().strip()

        modes ={
            "pentest mode": "pentest",
            "recon mode": "recon",
            "exploit mode" : "exploit",
            "forensic mode": "forensic",
            "assistant mode" : "assistant",
            "red team mode" : "pentest"
        }

        for phrase, mode in modes.items():
            if phrase in text_lower:
                self.mode = mode
                return f"[DEDSEC] Mode switched to {mode.upper()}\n[*] systems adapted for {mode} opeartion"
            
        return None
    def get_status(self) -> Dict:
        """Return current engine status"""
        return {
            "active": self.active,
            "mode": self.mode,
            "session_id": self.session_id,
            "uptime": round(time.time() - self.start_time) if self.active else 0
        }