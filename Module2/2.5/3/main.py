import sys
import re


def decrypt(message: str) -> str:
    pattern = r"[A-Za-zА-Яа-я0-9-]\.{2}"

    while True:
        finds = re.findall(pattern=pattern, string=message)
        if finds:
            for find in finds:
                message = message.replace(find, "")
        else:
            message = message.replace('.', "")
            break

    return message


if __name__ == "__main__":
    cipher = sys.stdin.read()

    decipher = decrypt(message=cipher)
    print(f"Сообщение: {decipher}")
