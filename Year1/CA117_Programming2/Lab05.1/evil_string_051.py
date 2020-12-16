import sys

def match(word, evil_str):
    return [l for l in word if l in evil_str] == list(evil_str)

def main():
    words = [line.strip() for line in sys.stdin]
    evil_words = [w for w in words if match(w.lower(), "evil")]
    for word in evil_words:
        print(word)

if __name__ == '__main__':
    main()
