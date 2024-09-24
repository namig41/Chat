from datetime import datetime
import pytest

from domain.exceptions.message import TitleTooLongException
from domain.values.messages import Text, Title
from domain.entities.messages import Chat, Message 

def test_create_message_success():
    text = Text('Hello world')
    message = Message(text=text)
    
    assert message.text == text
    assert message.create_at.date() == datetime.today().date()
    
def test_create_message_text_too_long():
    text = Text('a' * 400)
    message = Message(text=text)
    
    assert message.text == text
    assert message.create_at.date() == datetime.today().date()
    
def test_create_chat_success():
    with pytest.raises(TitleTooLongException):
        Title('title' * 200)    

def test_add_chat_to_message():
    text = Text('Hello world')
    message = Message(text=text)

    title = Title('title')
    chat = Chat(title=title)

    chat.add_message(message)

    assert message in chat.messages