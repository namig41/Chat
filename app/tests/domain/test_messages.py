from datetime import datetime
import pytest

from domain.events.messages import NewMessageReceivedEvent
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
    
def test_new_message_events():
    text = Text('Hello World')
    message = Message(text=text)
    
    title = Title('title')
    chat = Chat(title=title)
    
    chat.add_message(message)
    events = chat.pull_events()
    pulled_events = chat.pull_events()
    
    assert not pulled_events, pulled_events
    assert len(events) == 1, events
    
    new_event = events[0]
    
    assert isinstance(new_event, NewMessageReceivedEvent), new_event