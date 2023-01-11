def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'hi!'

    return 'I am a new bot and still learning! Try typing "!help".'

