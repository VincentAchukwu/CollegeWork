import sys

#1 = Hearts
#2 = Spades
#3 = Diamonds
#4 = Clubs
name = ["nothing", "one pair", "two pairs", "three of a kind", "a straight", "a flush", "a full house", "four of a kind", "a straight flush", "a royal flush"]

def poker(ranks, total):
    i = 0
    for value in ranks:
        probability = (value / total) * 100
        print("The probability of {:s} is {:.4f}%".format(name[i], probability))
        i += 1


def main():
    totalhands = 0
    rankprob = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in sys.stdin:
        rank = line.strip()[-1]
        totalhands += 1
        rankprob[int(rank)] += 1
    poker(rankprob, totalhands)

if __name__ == '__main__':
    main()
