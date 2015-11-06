# exercism.io atbash_cipher file

# http://stackoverflow.com/questions/31040525/insert-element-in-python-list-after-every-nth-element

def encode(msg):
    encodedMsg = ''
    cleansedMsg = [x for x in msg.lower().strip() if x.isalnum()]
    tmap = dict(zip("abcdefghijklmnopqrstuvwxyz",
                    "zyxwvutsrqponmlkjihgfedcba"))

    for index, char in enumerate(cleansedMsg):
        if char.isalpha():
            encodedMsg += tmap[char]
        elif char.isdigit():
            encodedMsg += char

        if index % 5 == 4:
            encodedMsg += ' '

    return encodedMsg.strip()


def decode(msg):
    output = []
    tmap = dict(zip("zyxwvutsrqponmlkjihgfedcba",
                    "abcdefghijklmnopqrstuvwxyz"))

    for x in msg.lower().strip():
        if x.isalpha():
            output.append(tmap[x])
        elif x.isdigit():
            output.append(x)

    return ''.join(output).strip()
