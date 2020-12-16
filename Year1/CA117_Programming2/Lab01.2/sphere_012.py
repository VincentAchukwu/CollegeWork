import sys
import math
#volume = 4/3 * pi * r ** 2
#area = 4 * pi * r ** 2
def main():
    start_r = float(sys.argv[1])
    inc_r = float(sys.argv[2])
    end_r = float(sys.argv[3])

    h1 = 'Radius (m)'
    h4 = '-' * len(h1)
    h2 = 'Area (m^2)'
    h5 = '-' * len(h2)
    h3 = 'Volume (m^3)'
    h6 = '-' * len(h3)

    print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3))
    print('{:>s} {:>15s} {:>15s}'.format(h4, h5, h6))
    while start_r <= end_r:
        area = 4 * math.pi * start_r ** 2
        volume = 4 / 3 * math.pi * start_r ** 3
        print('{:{}.1f} {:>{}.2f} {:>{}.2f}'.format(start_r, len(h1), area, 15, volume, 15))
        start_r = start_r + inc_r


if __name__ == '__main__':
    main()
