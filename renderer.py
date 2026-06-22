import textwrap

def speech_bubble(text):
    lines = textwrap.wrap(text, width=20)
    width = max(len(line) for line in lines)
    border = " " + "-" * (width + 2)
    output = [border]
    for line in lines:
        output.append(f"< {line.ljust(width)} >")
    output.append(border)
    return "\n".join(output)