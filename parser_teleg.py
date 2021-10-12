from telethon import TelegramClient
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon import functions, types

api_id = *******
api_hash = '31734c3****************58'
# phone = "+7*******6"

client = TelegramClient('anon', api_id, api_hash).start()



phone_numbers = open('C:/Users/User/Desktop/test.txt', 'r')
phones = open('C:/Users/User/Desktop/test.txt', 'a', encoding='utf8')
x = int(1)
for phone_number in phone_numbers:
    contact = InputPhoneContact(client_id=0, phone=phone_number, first_name=phone_number, last_name=phone_number)
    result = client(ImportContactsRequest([contact]))
    print(result.stringify())

with TelegramClient('anon', api_id, api_hash) as client:
    result = client(functions.contacts.GetContactsRequest(
        hash=0
    ))
    phones.write(result.stringify())