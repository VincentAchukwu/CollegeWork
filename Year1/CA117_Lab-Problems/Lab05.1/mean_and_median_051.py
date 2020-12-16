import sys

def main():
    nums = sorted([int(line.strip()) for line in sys.stdin])
    n = len(nums)
    mean = sum(nums) / n
    print("Mean: {:.1f}".format(mean))
    if n % 2:
        median = nums[n // 2]
    else:
        median = (nums[n // 2] + nums[n // 2 - 1]) / 2
    print("Median: {:.1f}".format(median))


if __name__ == '__main__':
    main()
