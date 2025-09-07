import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration settings for WhatsApp Bulk Messenger Bot"""
    
    # WhatsApp Web settings
    WHATSAPP_URL = "https://web.whatsapp.com"
    
    # Message settings
    MESSAGE_DELAY = 2  # Delay between messages in seconds
    BATCH_DELAY = 10   # Delay between batches in seconds
    BATCH_SIZE = 5     # Number of messages per batch
    
    # Browser settings
    HEADLESS = False   # Set to True to run browser in background
    BROWSER_TIMEOUT = 30  # Timeout for browser operations
    
    # Contact list file
    CONTACTS_FILE = "contacts.txt"
    
    # Message templates
    MESSAGE_TEMPLATES = {
        "greeting": "Hello {name}! This is an automated message.",
        "promotion": "Would you like to learn about our special offer?",
        "reminder": "Reminder: {message}",
        "custom": ""  # Custom message will be set by user
    }
    
    # Logging
    LOG_FILE = "whatsapp_bot.log"
    LOG_LEVEL = "INFO"
