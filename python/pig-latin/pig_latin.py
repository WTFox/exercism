def translate(phrase):
    translated = []
    vowels = 'a e i o u x yt'.split()
    special_cases = 'qu ch sq'.split()

    for word in phrase.split():
        if word[0] in vowels:
            translated.append("{}{}".format(word, "ay"))
        elif word[:2] in special_cases:
            translated.append("{}{}{}".format(word[2:], word[:2], "ay"))
        else:
            translated.append("{}{}{}".format(word[1:], word[0], "ay"))

    return ' '.join(translated)

translate('apple')
