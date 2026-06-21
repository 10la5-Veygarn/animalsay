def speech_bubble(text):
    border = "-" * (len(text) + 2)
    return f" {border}\n< {text} >\n {border}\n"