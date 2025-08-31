📱## WhatsApp Bulk Messaging Bot

A simple Python + Streamlit tool that allows you to send WhatsApp messages in bulk using an Excel file of phone numbers. Built with Selenium for WhatsApp Web automation.

⸻

##Features
	•	Upload an Excel file containing phone numbers (with country code).
	•	Type a custom message to send.
	•	Automatically open WhatsApp Web, log in via QR code, and send messages to all contacts.
	•	Works with a single-column Excel file.
	•	Streamlit interface for easy usage.

⸻

##Demo
<img width="1680" height="836" alt="image" src="https://github.com/user-attachments/assets/032040c7-d9e3-4605-bf42-bf849ab31c25" />
<img width="1680" height="840" alt="image" src="https://github.com/user-attachments/assets/5537514e-0a83-46b5-8f32-f06caa9f990b" />
<img width="1680" height="908" alt="image" src="https://github.com/user-attachments/assets/93fde3cb-f515-4dc3-8d03-db91e530f247" />

Requirements
	•	Python 3.10+
	•	Google Chrome installed on your system
	•	ChromeDriver (matching your Chrome version)
	•	Python packages:
      pip install selenium streamlit pandas openpyxl

##Setup
	1.	Clone the repository:
        git clone https://github.com/yourusername/wpbot.git
        cd wpbot
  2.	Download ChromeDriver and place it in your project folder:

##Usage
	1.	Run the Streamlit app locally:
         streamlit run main.py
  2.	Open the link provided by Streamlit (usually http://localhost:8501) in your browser.
	3.	Upload your Excel file with one column of phone numbers.
	4.	Type the message you want to send.
	5.	Click Send WhatsApp Messages.
	6.	Scan the QR code in WhatsApp Web if prompted. Messages will be sent automatically.

##Excel Format

Your Excel file should have:
  Numbers
919876543210
918765432109
917123456789

	•	Include country code for all numbers.
	•	Only one column is required.

##Notes
	•	Must run locally; Selenium + ChromeDriver cannot run on Streamlit Cloud or other restricted cloud platforms.
	•	Make sure your ChromeDriver version matches your installed Chrome version.
	•	Avoid sending too many messages at once to prevent being flagged by WhatsApp.

 ##License

  MIT License © 2025 piyushpandey955



