def count_filler_words(text):

    fillers = [
        "um",
        "uh",
        "like",
        "actually",
        "basically",
        "so"
    ]

    text = text.lower()

    count = 0

    for word in fillers:
        count += text.count(word)

    return count