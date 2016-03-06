import re


def abbreviate(sen):
    acronym = []
    match = re.findall(r'\w+', sen)
    for word in match:
        acronym.append(word[0].upper())
        if not word.isupper():
            inter_word_caps = re.findall(r'[A-Z]', word[1:-1])
            acronym.append(''.join(inter_word_caps))

    return ''.join(acronym)