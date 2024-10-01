from domain.entities.messages import Chat, Message

def convert_message_to_document(message: Message) -> dict:
    return {
        'oid': message.oid,
        'text': message.text.as_generic_type(),
    }

def convert_chat_entity_to_document(chat: Chat) -> dict:
    return {
        'oid': chat.oid,
        'title': chat.title.as_generic_type(),
        'create_at': chat.create_at,
        'message': [
            convert_message_to_document(message) for message in chat.messages
        ],
    }