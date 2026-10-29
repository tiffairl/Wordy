"""To evaluate simple math word problems."""

operations = {
    "plus": (2, lambda a, b: a + b),
    "minus": (2, lambda a, b: a - b),
    "multiplied": (3, lambda a, b: a * b),
    "divided": (3, lambda a, b: a // b),
}


def answer(question):
    """The answer will be an integer."""

    if not question.endswith("?"):
        raise ValueError("unknown operation")

    if question == "What is?":
        raise ValueError("syntax error")

    if not question.startswith("What is "):
        raise ValueError("unknown operation")

    words = question[8:-1].split()

    try:
        result = int(words[0])
    except ValueError as exc:
        raise ValueError("syntax error") from exc

    item = 1

    while item < len(words):
        if words[item] not in operations:
            if words[item].lstrip("-").isdigit():
                raise ValueError("syntax error")
            raise ValueError("unknown operation")

        step, operation = operations[words[item]]

        if item + step - 1 >= len(words):
            raise ValueError("syntax error")

        if step == 3 and words[item + 1] != "by":
            raise ValueError("syntax error")

        try:
            number = int(words[item + step - 1])
        except ValueError as exc:
            raise ValueError("syntax error") from exc

        result = operation(result, number)
        item += step

    return result