"""
WhatsApp Bulk Messenger Bot

A Python automation tool for sending bulk messages through WhatsApp Web.
This tool is designed for legitimate business and personal use cases.

Author: GitHub User
License: MIT
"""

import time
import logging
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import Config
import colorama
from colorama import Fore, Style

colorama.init()

class WhatsAppBot:
    def __init__(self):
        """Initialize the WhatsApp Bot with driver and logging setup"""
        self.driver = None
        self.wait = None
        self.setup_logging()
        self.setup_driver()
        
    def setup_logging(self):
        """Setup logging configuration for the bot"""
        logging.basicConfig(
            level=getattr(logging, Config.LOG_LEVEL),
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(Config.LOG_FILE),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def setup_driver(self):
        """Setup Chrome driver with anti-detection options"""
        try:
            chrome_options = Options()
            if Config.HEADLESS:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            self.wait = WebDriverWait(self.driver, Config.BROWSER_TIMEOUT)
            self.logger.info("Chrome driver setup completed successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to setup driver: {str(e)}")
            raise
            
    def open_whatsapp(self):
        """Open WhatsApp Web and wait for QR code scan"""
        try:
            print(f"{Fore.CYAN}Opening WhatsApp Web...{Style.RESET_ALL}")
            self.driver.get(Config.WHATSAPP_URL)
            
            # Wait for QR code to be scanned
            print(f"{Fore.YELLOW}Please scan the QR code and login to WhatsApp Web...{Style.RESET_ALL}")
            
            # Wait for the main chat interface to load
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="chat-list"]')))
            print(f"{Fore.GREEN}Successfully logged into WhatsApp Web!{Style.RESET_ALL}")
            return True
            
        except TimeoutException:
            print(f"{Fore.RED}QR code scan timeout. Please try again.{Style.RESET_ALL}")
            return False
        except Exception as e:
            self.logger.error(f"Failed to open WhatsApp: {str(e)}")
            return False
            
    def search_contact(self, contact_name):
        """Search for a contact in WhatsApp"""
        try:
            # Click on search box
            search_box = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="chat-list-search"]')))
            search_box.clear()
            search_box.send_keys(contact_name)
            
            # Wait for search results
            time.sleep(2)
            
            # Click on the first result
            contact_element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[title="{contact_name}"]')))
            contact_element.click()
            
            return True
            
        except TimeoutException:
            self.logger.warning(f"Contact '{contact_name}' not found or not clickable")
            return False
        except Exception as e:
            self.logger.error(f"Error searching for contact '{contact_name}': {str(e)}")
            return False
            
    def send_message(self, message):
        """Send a message to the current chat"""
        try:
            # Find message input box
            message_box = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="conversation-compose-box-input"]')))
            message_box.click()
            message_box.clear()
            message_box.send_keys(message)
            
            # Send message
            send_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="send"]')))
            send_button.click()
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error sending message: {str(e)}")
            return False
            
    def load_contacts(self, contacts_file):
        """Load contacts from file"""
        try:
            with open(contacts_file, 'r', encoding='utf-8') as f:
                contacts = [line.strip() for line in f.readlines() if line.strip()]
            self.logger.info(f"Loaded {len(contacts)} contacts from {contacts_file}")
            return contacts
        except FileNotFoundError:
            self.logger.error(f"Contacts file '{contacts_file}' not found")
            return []
        except Exception as e:
            self.logger.error(f"Error loading contacts: {str(e)}")
            return []
            
    def send_bulk_messages(self, contacts, message, template_type="custom"):
        """Send messages to multiple contacts with delays"""
        if not contacts:
            print(f"{Fore.RED}No contacts found!{Style.RESET_ALL}")
            return
            
        # Prepare message
        if template_type in Config.MESSAGE_TEMPLATES and template_type != "custom":
            final_message = Config.MESSAGE_TEMPLATES[template_type]
        else:
            final_message = message
            
        print(f"{Fore.CYAN}Bulk messaging starting...{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Message: {final_message}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Number of contacts: {len(contacts)}{Style.RESET_ALL}")
        
        successful_sends = 0
        failed_sends = 0
        
        for i, contact in enumerate(contacts, 1):
            try:
                print(f"{Fore.YELLOW}[{i}/{len(contacts)}] Sending message to {contact}...{Style.RESET_ALL}")
                
                # Search for contact
                if not self.search_contact(contact):
                    print(f"{Fore.RED}❌ {contact} not found{Style.RESET_ALL}")
                    failed_sends += 1
                    continue
                    
                # Send message
                if self.send_message(final_message):
                    print(f"{Fore.GREEN}✅ Message sent to {contact}{Style.RESET_ALL}")
                    successful_sends += 1
                else:
                    print(f"{Fore.RED}❌ Failed to send message to {contact}{Style.RESET_ALL}")
                    failed_sends += 1
                    
                # Add delay between messages
                if i < len(contacts):
                    print(f"{Fore.BLUE}⏳ Waiting {Config.MESSAGE_DELAY} seconds...{Style.RESET_ALL}")
                    time.sleep(Config.MESSAGE_DELAY)
                    
                # Add batch delay
                if i % Config.BATCH_SIZE == 0 and i < len(contacts):
                    print(f"{Fore.BLUE}⏳ Batch completed, waiting {Config.BATCH_DELAY} seconds...{Style.RESET_ALL}")
                    time.sleep(Config.BATCH_DELAY)
                    
            except Exception as e:
                self.logger.error(f"Error sending message to {contact}: {str(e)}")
                failed_sends += 1
                
        print(f"\n{Fore.GREEN}Bulk messaging completed!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Successful: {successful_sends}{Style.RESET_ALL}")
        print(f"{Fore.RED}Failed: {failed_sends}{Style.RESET_ALL}")
        
    def close(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()
            self.logger.info("Browser closed")
