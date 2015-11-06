
def encode(msg):
    msg = msg.lower().strip()
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"

    trans = maketrans(plain, cipher)
    return msg.translate(trans)


def decode(msg):
    msg.lower().strip()
    plain = "zyxwvutsrqponmlkjihgfedcba"
    cipher = "abcdefghijklmnopqrstuvwxyz"

    trans = maketrans(plain, cipher)
    return msg.lower().translate(trans)


if __name__ == '__main__':
    encode("Testing, 1 2 3, testing.")
