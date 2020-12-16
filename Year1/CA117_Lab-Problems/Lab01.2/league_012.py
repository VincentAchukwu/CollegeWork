import sys

def main():
    h1 = "POS"
    h2 = "CLUB"
    h3 = "P"
    h4 = "W"
    h5 = "D"
    h6 = "L"
    h7 = "GF"
    h8 = "GA"
    h9 = "GD"
    h10 = "PTS"
    longest = 0
    lines = []
    a = []
    for line in sys.stdin:
        a.append(line.strip())
        tokens = line.strip().split()
        clubs = " ".join(tokens[1:-8])
        if len(clubs) > longest:
            longest = len(clubs)
    k = "{:<s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}".format(h1, h2, longest, h3, h4, h5, h6, h7, h8, h9, h10)

    for p in a:
        p = p.split()
        pos = p[0]
        club = " ".join(p[1:-8])
        a, b, c, d, e, f, g, h = p[-8:]
        lines.append("{:>{}s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}".format(pos, len(h1), club, longest, a, b, c, d, e, f, g, h))

    print(k)
    for l in lines:
        print(l)

if __name__ == '__main__':
    main()
