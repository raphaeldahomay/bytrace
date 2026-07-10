def text_to_binary(text):
    return " ".join(format(ord(char), "08b") for char in text)


def binary_to_text(binary):
    return "".join(
        chr(int(binary_value, 2))
        for binary_value in binary.split()
    )


def text_to_ascii(text):
    return " ".join(str(ord(char)) for char in text)


def ascii_to_text(ascii_values):
    return "".join(
        chr(int(value))
        for value in ascii_values.split()
    )


def ascii_to_binary(ascii_values):
    return " ".join(
        format(int(value), "08b")
        for value in ascii_values.split()
    )


def binary_to_ascii(binary):
    return " ".join(
        str(int(binary_value, 2))
        for binary_value in binary.split()
    )


def convert(value, converter_type):

    if converter_type == "text_to_binary":
        return text_to_binary(value)

    elif converter_type == "binary_to_text":
        return binary_to_text(value)

    elif converter_type == "text_to_ascii":
        return text_to_ascii(value)

    elif converter_type == "ascii_to_text":
        return ascii_to_text(value)

    elif converter_type == "ascii_to_binary":
        return ascii_to_binary(value)

    elif converter_type == "binary_to_ascii":
        return binary_to_ascii(value)

    else:
        return "Unknown converter"