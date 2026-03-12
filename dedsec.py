#!/usr/bin/env python3
"""
DEDSEC - WE ARE MANY WE ARE DEDSEC
AGENTIC AI SYSTEM - CYBERSECURITY EDITION
"""
import os
import sys
import asyncio

ASCII_BANNER="""
╔══════════════════════════════════════════════════════╗
║  ██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗   ║
║  ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝   ║
║  ██║  ██║█████╗  ██║  ██║███████╗█████╗  ██║        ║
║  ██║  ██║██╔══╝  ██║  ██║╚════██║██╔══╝  ██║        ║
║  ██████╔╝███████╗██████╔╝███████║███████╗╚██████╗   ║
║  ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝   ║
║                                                      ║
║         We Are Many. We Are DedSec.                  ║
║      [ Agentic | Adaptive | Autonomous ]             ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
"""

async def main():
    print(ASCII_BANNER)
    print("[*] Initializing the Dedsec core Engine...")
    print("[*] loading cybersecurity modules...")
    print("[*] Memory and adaption online")
    print("[*] Agentic task planner ready...\n")
    print("Type 'help' for commands | 'agents' for agent list | 'exit' to quit\n")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n[DEDSEC] going dark. We are many")
        sys.exit(0)
