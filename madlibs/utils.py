import re


def extract_words(text):
    words = []
    word = re.search(r"\[(.*?)\]", text)
    while word:
        words.append(re.sub(r"\]", "", re.sub(r"\[", "", word.group())))
        text = re.sub(r"\[.*?\]", "%s", text, count=1)
        word = re.search(r"\[(.*?)\]", text)
    return words


def convert_text(text):
    text = re.sub(r"\[.*?\]", "***", text)
    text = text.split("***")
    return text


def interpolate(record):
    words = record.story_words
    story_text = ""
    if len(record.story_text) > len(words):
        story_text += record.story_text[0]
    counter = 0
    for word in words:
        if counter > 0:
            story_text += record.story_text[counter]
        story_text += word
        counter += 1

    return story_text