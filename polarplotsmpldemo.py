import polarplotsmpl as ppm
import functions


def main():

    print("--------------------")
    print("| codedrome.com    |")
    print("| Polar Plots with |")
    print("| Matplotlib       |")
    print("--------------------\n")

    # ppm.plot("circle", 120, 0, 360, functions.circle, "#008000")
    # ppm.plot("cardioid", 75, 0, 360, functions.cardioid, "#000080")
    # ppm.plot("spiral", 100, 0, 2880, functions.spiral, "#FF8000")
    ppm.plot("rose", 150, 0, 360, functions.rose, "#FF0080")


if __name__ == "__main__":

    main()