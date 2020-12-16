import sys

def main():
    try:
        s = sys.argv[1]
        students = []
        marks = []
        with open(s, "r") as f:
            for line in f:
                try:
                    tokens = line.strip().split()
                    students.append(" ".join(tokens[1:]))
                    marks.append(int(tokens[0]))
                except ValueError:
                    print("Invalid mark {:s} encountered. Skipping.".format(tokens[0]))
        topstudents = []
        largest = 0
        for i in marks:
            if i > largest:
                largest = i
        for i in range(0, len(marks)):
            if marks[i] == largest:
                topstudents.append(students[i])
        me = ", ".join(topstudents)
        print("Best student(s): {:s}".format(me))
        print("Best mark: {:d}".format(largest))
    except FileNotFoundError:
        print("The file {:s} could not be opened".format(s))


if __name__ == '__main__':
    main()
