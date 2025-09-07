# WhatsApp Bulk Messenger Bot

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.15.2-green.svg)](https://selenium.dev)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A professional Python automation tool for sending bulk messages through WhatsApp Web. This tool is designed for legitimate business and personal use cases with built-in anti-spam measures.

## ⚠️ Important Disclaimer

- **This tool should only be used for legal and ethical purposes**
- **Use in compliance with WhatsApp's Terms of Service**
- **Do not spam and respect user privacy**
- **Users are responsible for their actions and compliance with local laws**

## 🚀 Features

- ✅ **Bulk Messaging**: Send messages to multiple contacts efficiently
- ✅ **Message Templates**: Pre-built templates for common use cases
- ✅ **Anti-Spam Protection**: Built-in delays and batch processing
- ✅ **Error Handling**: Comprehensive error management and logging
- ✅ **User-Friendly Interface**: Colorful console interface with progress tracking
- ✅ **Contact Management**: Easy contact list management
- ✅ **Professional Logging**: Detailed activity logs for monitoring

## 📋 Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- WhatsApp Web account
- Active internet connection

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/whatsapp-bulk-messenger.git
cd whatsapp-bulk-messenger
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Contacts

Edit the `contacts.txt` file and add your contact names (one per line):

```
# WhatsApp Contact List
# Write one contact name per line
# Lines starting with # are treated as comments

John Doe
Jane Smith
Mike Johnson
Sarah Wilson
```

## 🎯 Usage

### Quick Start

```bash
python main.py
```

### Step-by-Step Guide

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Scan QR Code**: 
   - WhatsApp Web will open in your browser
   - Scan the QR code with your phone
   - Wait for successful login

3. **Select Message Type**:
   - Custom message (write your own)
   - Greeting message
   - Promotion message
   - Reminder message

4. **Enter Your Message** (if applicable)

5. **Confirm and Send**: Review the summary and confirm

## ⚙️ Configuration

Edit `config.py` to customize the bot behavior:

```python
class Config:
    # Message settings
    MESSAGE_DELAY = 2      # Delay between messages (seconds)
    BATCH_DELAY = 10       # Delay between batches (seconds)
    BATCH_SIZE = 5         # Number of messages per batch
    
    # Browser settings
    HEADLESS = False       # Run browser in background
    BROWSER_TIMEOUT = 30   # Browser operation timeout
```

## 📁 Project Structure

```
whatsapp-bulk-messenger/
├── main.py              # Main application entry point
├── whatsapp_bot.py      # Core WhatsApp automation class
├── config.py            # Configuration settings
├── contacts.txt         # Contact list (user-editable)
├── requirements.txt     # Python dependencies
├── setup.py            # Setup and installation script
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
└── README.md           # This file
```

## 🔧 Message Templates

### Greeting Template
```
Hello {name}! This is an automated message.
```

### Promotion Template
```
Would you like to learn about our special offer?
```

### Reminder Template
```
Reminder: {message}
```

## 🛡️ Anti-Spam Features

- **Message Delays**: Configurable delays between messages
- **Batch Processing**: Groups messages to avoid overwhelming the system
- **Rate Limiting**: Built-in rate limiting to prevent spam detection
- **Error Recovery**: Automatic retry mechanisms for failed messages

## 📊 Logging

All activities are logged to `whatsapp_bot.log` with timestamps and detailed information:

```
2024-01-15 10:30:15 - INFO - Chrome driver setup completed successfully
2024-01-15 10:30:45 - INFO - Successfully logged into WhatsApp Web!
2024-01-15 10:31:02 - INFO - Message sent to John Doe
```

## 🚨 Troubleshooting

### Common Issues

1. **ChromeDriver Error**:
   ```bash
   pip install --upgrade webdriver-manager
   ```

2. **QR Code Timeout**:
   - Ensure stable internet connection
   - Try refreshing the page
   - Check if WhatsApp Web is accessible

3. **Contact Not Found**:
   - Verify contact names in `contacts.txt`
   - Ensure contacts exist in your WhatsApp
   - Check for typos in contact names

### Error Codes

- `TimeoutException`: Browser operation timeout
- `NoSuchElementException`: Element not found on page
- `WebDriverException`: Chrome driver issues

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/whatsapp-bulk-messenger.git

# Install development dependencies
pip install -r requirements.txt

# Run tests (if available)
python -m pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚖️ Legal Notice

This software is provided for educational and legitimate business purposes only. Users are responsible for:

- Complying with WhatsApp's Terms of Service
- Following applicable local and international laws
- Respecting user privacy and consent
- Not engaging in spam or harassment

The authors and contributors are not responsible for any misuse of this software.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/eroniyom)
- **Discussions**: [GitHub Discussions](https://github.com/Eroniyom/Whatsapp-Auto-Spam)
- **Email**: your.email@example.com

## 🙏 Acknowledgments

- [Selenium](https://selenium.dev) for web automation
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager) for driver management
- [Colorama](https://github.com/tartley/colorama) for colored terminal output

## 📈 Roadmap

- [ ] GUI interface
- [ ] Message scheduling
- [ ] Contact import from CSV
- [ ] Message analytics
- [ ] Multi-language support
- [ ] API integration

---


**⭐ If you found this project helpful, please give it a star!**
