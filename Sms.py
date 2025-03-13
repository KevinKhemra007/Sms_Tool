#!/usr/bin/env python3
"""
Created by Khemra

This script sends SMS messages using your purchased API key (Textbelt).
It prompts you to enter:
  - The SMS message you want to send,
  - The sender name (this will appear in the SMS),
  - The recipient phone number(s) (if multiple, separate by commas),
  - Your API key for authentication.

If the API key is incorrect, it will show a message directing users to
contact Telegram: t.me/hackisreal007 to buy a valid key.
"""

import requests
import time
import sys
import os
import platform

try:
    from colorama import init, Fore, Style
except ImportError:
    os.system("pip install colorama -q")
    from colorama import init, Fore, Style

# Initialize colorama for colored text output
init(autoreset=True)

# ASCII art banner with Telegram link
banner = f"""
{Fore.CYAN}{Style.BRIGHT}
  ____                 _       _    _            
 |  _ \  ___  ___ ___ | | __ _| |__| | ___ _ __  
 | | | |/ _ \/ __/ _ \| |/ _` |  __  |/ _ \ '__| 
 | |_| |  __/ (_| (_) | | (_| | |  | |  __/ |    
 |____/ \___|\___\___/|_|\__,_|_|  |_|\___|_|  
   
                    REAL HACK Khemra
        TiktOk :
  	https://www.tiktok.com/@raatechofficial
	Telegram Channel: https://t.me/hackisreal007
	Telegram Group: https://t.me/Nosecurity001
	
{Style.RESET_ALL}
"""

def send_sms(api_key, phone, message, sender):
    """
    Sends a single SMS using the provided API key.
    
    Parameters:
        api_key (str): User-provided API key.
        phone (str): The recipient phone number.
        message (str): The text message to send.
        sender (str): The sender name that will appear in the SMS.
    
    Returns:
        dict: The JSON response from the API.
    """
    url = "https://textbelt.com/text"
    full_message = f"{sender}: {message}"
    data = {
        'phone': phone,
        'message': full_message,
        'key': api_key
    }
    try:
        response = requests.post(url, data=data)
        return response.json()
    except Exception as e:
        return {"success": False, "error": str(e)}

def main():
    # Clear the console for a clean start
    os.system('cls' if platform.system().startswith("Windows") else 'clear')
    print(banner)

    # Prompt for API Key
    print(f"{Fore.YELLOW}Enter your SMS API Key (or buy from Telegram):{Style.RESET_ALL}")
    api_key = input("API Key: ").strip()

    # Prompt for SMS message
    print(f"{Fore.YELLOW}Enter the SMS message you want to send:{Style.RESET_ALL}")
    message = input("Message: ").strip()

    # Prompt for sender name
    print(f"{Fore.YELLOW}Enter the sender name (this will appear in the SMS):{Style.RESET_ALL}")
    sender = input("Sender Name: ").strip()

    # Prompt for recipient phone number(s)
    print(f"{Fore.YELLOW}Enter the phone number(s) (if multiple, separate by commas):{Style.RESET_ALL}")
    phones_input = input("Phone Number(s): ").strip()
    phones = [p.strip() for p in phones_input.split(',') if p.strip()]

    # Ensure inputs are valid
    if not api_key or not message or not phones:
        print(f"{Fore.RED}[X] Error: All fields are required! Please enter valid details.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"\n{Fore.YELLOW}Sending SMS messages...{Style.RESET_ALL}\n")

    # Loop through each phone number and send the SMS
    for phone in phones:
        result = send_sms(api_key, phone, message, sender)
        if result.get("success"):
            print(f"{Fore.GREEN}[✔] SMS sent successfully to {phone}")
        else:
            error_msg = result.get("error", "Unknown error")
            if "Invalid API Key" in error_msg or "not valid" in error_msg:
                print(f"\n{Fore.RED}[X] Invalid API Key! 🔑{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}💬 Contact me on Telegram to buy a valid API key:{Style.RESET_ALL}")
                print(f"{Fore.CYAN}👉 https://t.me/hackisreal007{Style.RESET_ALL}")
                sys.exit(1)  # Stop execution if API key is incorrect
            else:
                print(f"{Fore.RED}[X] Failed to send SMS to {phone}: {error_msg}")

        # Wait 2 seconds between messages to avoid API rate limits
        time.sleep(2)

    print(f"\n{Fore.CYAN}[INFO] SMS sending process completed.{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[INFO] Process interrupted by user. Exiting...{Style.RESET_ALL}")
        sys.exit(0)
