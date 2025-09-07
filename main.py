#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
WhatsApp Bulk Messenger Bot - Main Application

A professional tool for sending bulk messages through WhatsApp Web.
Designed for legitimate business and personal use cases.

Author: GitHub User
License: MIT
"""

import os
import sys
from whatsapp_bot import WhatsAppBot
from config import Config
import colorama
from colorama import Fore, Style

colorama.init()

def print_banner():
    """Print application banner"""
    banner = f"""
{Fore.CYAN}
╔══════════════════════════════════════════════════════════════╗
║                 WhatsApp Bulk Messenger Bot                  ║
║                                                              ║
║  ⚠️  This tool should only be used for legal purposes        ║
║  ⚠️  Use in compliance with WhatsApp's Terms of Service      ║
║  ⚠️  Do not spam and respect user privacy                    ║
╚══════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
"""
    print(banner)

def get_user_choice():
    """Get user's choice for message type"""
    print(f"{Fore.YELLOW}Select message type:{Style.RESET_ALL}")
    print("1. Custom message (write your own message)")
    print("2. Greeting message")
    print("3. Promotion message")
    print("4. Reminder message")
    
    while True:
        choice = input(f"{Fore.CYAN}Your choice (1-4): {Style.RESET_ALL}").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        print(f"{Fore.RED}Invalid choice! Please enter a number between 1-4.{Style.RESET_ALL}")

def get_custom_message():
    """Get custom message from user"""
    print(f"{Fore.YELLOW}Enter the message you want to send:{Style.RESET_ALL}")
    message = input(f"{Fore.CYAN}Message: {Style.RESET_ALL}").strip()
    return message

def get_reminder_message():
    """Get reminder message from user"""
    print(f"{Fore.YELLOW}Enter your reminder message:{Style.RESET_ALL}")
    reminder = input(f"{Fore.CYAN}Reminder: {Style.RESET_ALL}").strip()
    return reminder

def confirm_sending(contacts_count, message):
    """Ask user to confirm before sending"""
    print(f"\n{Fore.YELLOW}Sending Summary:{Style.RESET_ALL}")
    print(f"Number of contacts: {contacts_count}")
    print(f"Message: {message}")
    print(f"Delay between messages: {Config.MESSAGE_DELAY} seconds")
    print(f"Batch delay: {Config.BATCH_DELAY} seconds")
    
    while True:
        confirm = input(f"\n{Fore.CYAN}Are you sure you want to send the messages? (y/n): {Style.RESET_ALL}").strip().lower()
        if confirm in ['y', 'yes', 'e', 'evet']:
            return True
        elif confirm in ['n', 'no', 'h', 'hayır']:
            return False
        print(f"{Fore.RED}Please enter 'y' (yes) or 'n' (no).{Style.RESET_ALL}")

def main():
    """Main application function"""
    print_banner()
    
    # Check if contacts file exists
    if not os.path.exists(Config.CONTACTS_FILE):
        print(f"{Fore.RED}Error: {Config.CONTACTS_FILE} file not found!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please add your contact list to {Config.CONTACTS_FILE} file first.{Style.RESET_ALL}")
        return
    
    # Initialize bot
    try:
        bot = WhatsAppBot()
    except Exception as e:
        print(f"{Fore.RED}Failed to start bot: {str(e)}{Style.RESET_ALL}")
        return
    
    try:
        # Load contacts
        contacts = bot.load_contacts(Config.CONTACTS_FILE)
        if not contacts:
            print(f"{Fore.RED}Contact list is empty!{Style.RESET_ALL}")
            return
        
        # Get message type and content
        choice = get_user_choice()
        
        if choice == '1':  # Custom message
            message = get_custom_message()
            if not message:
                print(f"{Fore.RED}Message cannot be empty!{Style.RESET_ALL}")
                return
            template_type = "custom"
            
        elif choice == '2':  # Greeting
            message = ""
            template_type = "greeting"
            
        elif choice == '3':  # Promotion
            message = ""
            template_type = "promotion"
            
        elif choice == '4':  # Reminder
            reminder = get_reminder_message()
            if not reminder:
                print(f"{Fore.RED}Reminder message cannot be empty!{Style.RESET_ALL}")
                return
            message = reminder
            template_type = "reminder"
        
        # Confirm before sending
        if not confirm_sending(len(contacts), message or Config.MESSAGE_TEMPLATES.get(template_type, "")):
            print(f"{Fore.YELLOW}Operation cancelled.{Style.RESET_ALL}")
            return
        
        # Open WhatsApp Web
        if not bot.open_whatsapp():
            print(f"{Fore.RED}Could not connect to WhatsApp Web!{Style.RESET_ALL}")
            return
        
        # Send bulk messages
        bot.send_bulk_messages(contacts, message, template_type)
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Operation cancelled by user.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {str(e)}{Style.RESET_ALL}")
    finally:
        # Close browser
        bot.close()
        print(f"{Fore.GREEN}Program terminated.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
