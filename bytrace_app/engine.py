def text_to_binary(text):
    try:
        return " ".join(
            format(ord(char), "08b")
            for char in text
        )
    except (TypeError, ValueError):
        return "Invalid input. Please enter valid text."


def binary_to_text(binary):
    try:
        return "".join(
            chr(int(binary_value, 2))
            for binary_value in binary.split()
        )
    except (TypeError, ValueError, OverflowError):
        return "Invalid input. Please enter valid binary values."


def text_to_ascii(text):
    try:
        return " ".join(
            str(ord(char))
            for char in text
        )
    except (TypeError, ValueError):
        return "Invalid input. Please enter valid text."


def ascii_to_text(ascii_values):
    try:
        return "".join(
            chr(int(value))
            for value in ascii_values.split()
        )
    except (TypeError, ValueError, OverflowError):
        return "Invalid input. Please enter valid ASCII values."


def ascii_to_binary(ascii_values):
    try:
        return " ".join(
            format(int(value), "08b")
            for value in ascii_values.split()
        )
    except (TypeError, ValueError):
        return "Invalid input. Please enter valid ASCII numbers."


def binary_to_ascii(binary):
    try:
        return " ".join(
            str(int(binary_value, 2))
            for binary_value in binary.split()
        )
    except (TypeError, ValueError):
        return "Invalid input. Please enter valid binary values."


def convert(value, converter_type):

    if not isinstance(value, str):
        return "Invalid input. Please enter a valid string."

    if not value.strip():
        return "Please enter a value to convert."

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