import sys

num2words1 = {"0": 'Zero', "1": 'One', "2": 'Two', "3": 'Three', "4": 'Four', "5": 'Five', "6": 'Six', "7": 'Seven', "8": 'Eight', "9": 'Nine', "10": 'Ten', "11": 'Eleven', "12": 'Twelve', "13": 'Thirteen', "14": 'Fourteen', "15": 'Fifteen', "16": 'Sixteen', "17": 'Seventeen', "18": 'Eighteen', "19": 'Nineteen'}
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

def n2w(number):
    if 0 <= number <= 19:
        return num2words1[str(number)]
    elif number < 100 and number % 10 == 0:
        tens = divmod(number, 10)[0]
        return num2words2[tens - 2]
    elif 20 <= number <= 99:
        tens, below_ten = divmod(number, 10)
        return num2words2[tens - 2] + '-' + num2words1[str(below_ten)]
    else:
        return "one hundred"

def main():
    for line in sys.stdin:
        s = ""
        numbers = line.strip().split()
        for n in numbers:
            s = s + " " + n2w(int(n))
        print(s.strip().lower())

if __name__ == "__main__":
    main()
