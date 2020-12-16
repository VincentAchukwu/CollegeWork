import sys

def seconds(t):
    minutes, secs = t.split(":")
    total = int(minutes) * 60 + int(secs)
    return total

def sort_on(t):
    return seconds(t[1])

def main():
    d = {}
    for line in sys.stdin:
        try:
            tokens = line.strip().split()
            d[tokens[0]] = min(tokens[1:], key=seconds)
        except ValueError:
            continue
    winner = min(d.items(), key=sort_on)
    print("{} : {}".format(winner[0], winner[1]))

if __name__ == '__main__':
    main()
