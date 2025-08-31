import time
import pandas as pd
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your ChromeDriver
CHROMEDRIVER_PATH = "chromedriver-mac-arm64/chromedriver"   # make sure path is correct

# Function to send WhatsApp messages
def send_whatsapp_messages(numbers, message):
    # Configure Chrome
    options = Options()
    options.add_experimental_option("detach", True)  # Keep browser open after script ends
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com")
    st.info("Please scan the QR code in the browser to log in to WhatsApp Web.")
    time.sleep(20)  # Give user time to scan QR

    for number in numbers:
        number = str(number).strip()
        if number == "" or number.lower() == "nan":
            continue

        try:
            # Go to chat with prefilled message
            url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
            driver.get(url)

            # Wait for message box
            input_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
            )

            # Press ENTER to send
            input_box.send_keys(Keys.ENTER)

            st.success(f"✅ Message sent to {number}")
            time.sleep(3)

        except Exception as e:
            st.error(f"❌ Could not send message to {number}: {e}")
            time.sleep(2)

    st.success("🎉 All messages processed!")
    driver.quit()


# ================== STREAMLIT UI ==================
st.title("📱 WhatsApp Bulk Messaging Bot")
st.write("Upload an Excel file with one column containing phone numbers (with country code).")

# File uploader
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

# Message input
message = st.text_area("Enter your message:")

# Process uploaded file
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Preview of uploaded numbers:")
    st.dataframe(df.head())

    if st.button("🚀 Send WhatsApp Messages"):
        if df.shape[1] != 1:
            st.error("The Excel file must have only one column with phone numbers.")
        else:
            numbers = df.iloc[:, 0].dropna().tolist()
            send_whatsapp_messages(numbers, message)