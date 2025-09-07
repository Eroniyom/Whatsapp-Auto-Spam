#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
WhatsApp Bulk Messenger Bot - Setup Script

Automated setup script for the WhatsApp Bulk Messenger Bot.
Handles dependency installation and environment verification.

Author: GitHub User
License: MIT
"""

import os
import sys
import subprocess

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Package installation error: {e}")
        return False

def check_chrome():
    """Check if Chrome is installed"""
    print("Checking Chrome browser...")
    try:
        # Try to find Chrome executable
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            "/usr/bin/google-chrome",
            "/usr/bin/chromium-browser",
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        ]
        
        for path in chrome_paths:
            if os.path.exists(path):
                print("✅ Chrome browser found!")
                return True
                
        print("⚠️  Chrome browser not found!")
        print("Please install Google Chrome: https://www.google.com/chrome/")
        return False
        
    except Exception as e:
        print(f"❌ Chrome check error: {e}")
        return False

def create_sample_contacts():
    """Create sample contacts file if it doesn't exist"""
    if not os.path.exists("contacts.txt"):
        print("Creating sample contact list...")
        with open("contacts.txt", "w", encoding="utf-8") as f:
            f.write("""# WhatsApp Contact List
# Write one contact name per line
# Lines starting with # are treated as comments

# Example contacts:
# John Doe
# Jane Smith
# Mike Johnson
# Sarah Wilson
# David Brown
""")
        print("✅ Sample contact list created!")
    else:
        print("✅ Contact list already exists!")

def main():
    """Main setup function"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                 WhatsApp Bot Setup                          ║
╚══════════════════════════════════════════════════════════════╝
""")
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher required!")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} detected!")
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Check Chrome
    if not check_chrome():
        print("\n⚠️  Please install Chrome and run again!")
        sys.exit(1)
    
    # Create sample contacts
    create_sample_contacts()
    
    print("""
╔══════════════════════════════════════════════════════════════╗
║                    Setup Complete!                          ║
╚══════════════════════════════════════════════════════════════╝

📋 Next steps:
1. Edit contacts.txt file and add contact names
2. Run the program with: python main.py
3. Scan QR code in WhatsApp Web
4. Send your messages

⚠️  Important: This tool should only be used for legal purposes!
""")

if __name__ == "__main__":
    main()
