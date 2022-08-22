import os

from dotenv import load_dotenv
from fastapi import FastAPI
from skpy import Skype

load_dotenv()  # take environment variables from .env.
app = FastAPI()


@app.post("/")
def send_message(name:str,message:str):
    skype = Skype(os.environ["SKYPE_NAME"],os.environ["SKYPE_PASSWORD"])
    
    contactId = None
    contacts = skype.contacts

    for contact in contacts:
        if name.lower() in str(contact.name).lower():
            contactId = str(contact.id)
            break
    
    if contactId is None:
        return {"message": f"No user found with {name}."}

    skype.contacts[contactId].chat.sendMsg(message)

    return {"message": f"Sent message to {name}"}
