import sys

def qnou(l):
    return [w for w in l if w.lower().count("q") > w.lower().count("qu")]

words = []
def main():
    for line in sys.stdin:
        words.append(line.strip())
    print("Words with q but no u:", qnou(words))

if __name__ == '__main__':
    main()
