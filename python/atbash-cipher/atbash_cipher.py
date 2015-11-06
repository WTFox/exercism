# exercism.io atbash_cipher file

# http://stackoverflow.com/questions/31040525/insert-element-in-python-list-after-every-nth-element

def encode(msg):
    encodedMsg = ''
    cleansedMsg = [x for x in msg.lower().strip() if x.isalnum()]
    tmap = dict(zip("abcdefghijklmnopqrstuvwxyz",
                    "zyxwvutsrqponmlkjihgfedcba"))

    for index, letter in enumerate(cleansedMsg):
        print(index, letter)

        if letter.isalpha():
            encodedMsg += tmap[letter]
        elif letter.isdigit():
            encodedMsg += letter

    return encodedMsg


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


if __name__ == '__main__':
    print(encode("Truth is fiction."))
    print("gifgs rhurx grlm")
