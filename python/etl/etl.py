def transform(seq):
    return {word.lower(): score for score, data in seq.items() for word in data}
