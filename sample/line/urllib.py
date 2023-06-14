def parse(text):
    encoded_text = text.encode('utf-8')
    result = ''
    for char in encoded_text:
        if char < 128:
            result += chr(char)
        else:
            result += '%' + hex(char)[2:].upper()
    return result
