import pyautogui
import time
import smtplib
import ssl
import os
from email.message import EmailMessage

# --- USER CONFIGURATION ---
EMAIL_SENDER = 'sibgaturrahmanbros@gmail.com'
EMAIL_PASSWORD = 'xnac xrws iotd akke'  # App Password
EMAIL_RECEIVER = 'u2104101@student.cuet.ac.bd'
INTERVAL = 2     # Time between screenshots (e.g., 5 seconds)
BATCH_SIZE = 10    # Send email after collecting this many photos

def send_batch_email(image_list):
    msg = EmailMessage()
    msg['Subject'] = f'Batch Alert: {len(image_list)} Screenshots'
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg.set_content('Here is the latest batch of screenshots.')

    # 1. Attach files
    for image_path in image_list:
        with open(image_path, 'rb') as f:
            file_data = f.read()
            file_name = f.name
            msg.add_attachment(file_data, maintype='image', subtype='png', filename=file_name)

    context = ssl.create_default_context()
    
    # 2. Send Email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print(f"✅ Batch email sent with {len(image_list)} photos!")
            
            # 3. Cleanup: Delete files ONLY after successful send
            for image_path in image_list:
                os.remove(image_path)
            print("🗑️  Local files deleted.")
            
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        # Note: We do NOT delete files here, so we can try again later if we wanted to logic for that.

# --- MAIN LOOP ---
print(f"Monitor started... Collecting {BATCH_SIZE} photos before sending.")
pending_files = [] # The empty basket

while True:
    # 1. Capture Logic
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"ss-{timestamp}.png"
    
    pyautogui.screenshot(filename)
    print(f"📸 Captured: {filename}")
    
    # 2. Add to Basket
    pending_files.append(filename)

    # 3. Check if Basket is Full
    if len(pending_files) >= BATCH_SIZE:
        print("🚀 Basket full! Sending email...")
        send_batch_email(pending_files)
        pending_files = [] # Empty the basket for the next round
    
    # 4. Wait
    time.sleep(INTERVAL)
