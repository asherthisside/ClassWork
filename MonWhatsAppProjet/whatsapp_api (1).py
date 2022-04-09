from whatsapp import WhatsApp
import time
value=True
while(value):
    whatsapp = WhatsApp(100, session="mysession")
    user_names = whatsapp.unread_usernames()
    for name in user_names:
        messages = whatsapp.get_last_message_for(name)
    time.sleep(30)
    whatsapp.browser.close()