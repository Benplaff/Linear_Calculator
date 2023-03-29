#! /usr/bin/env python3

from process_temps import process_temps
import sys

input_temps = sys.argv[1]

"""
After process_temps function organizes the temperatures and times into lists, 
calculate the linear interpolation between each point, using the formulas
m = (y0-y1)/(x0-x1) and y1 = b + mx1
"""
def linear_interpolation():
    core_0_data = []
    core_1_data = []
    core_2_data = []
    core_3_data = []

    process_temps(input_temps, core_0_data, core_1_data, core_2_data, core_3_data)

    # calculate and print interpolations for core 0
    with open("interpolation-core-0.txt", "w") as output_file:
        length = len(core_0_data) - 1
        i = 0
        for i in range(length):
            x0 = core_0_data[i][0]
            x1 = core_0_data[i+1][0]
            y0 = core_0_data[i][1]
            y1 = core_0_data[i+1][1]
            m = ((y0 - y1)/(x0 - x1))
            
            output_file.write(str(x0) + "\t<= x <\t" + str(x1) + ";\t\t\ty_" + str(i) + "\t\t=\t" + str(y0) + " +\t" + str('%.4f' % m) + "x;\tinterpolation\n")

    # calculate and print interpolations for core 1
    with open("interpolation-core-1.txt", "w") as output_file:
        length = len(core_1_data) - 1
        i = 0
        for i in range(length):
            x0 = core_1_data[i][0]
            x1 = core_1_data[i+1][0]
            y0 = core_1_data[i][1]
            y1 = core_1_data[i+1][1]
            m = ((y0 - y1)/(x0 - x1))
            
            output_file.write(str(x0) + "\t<= x <\t" + str(x1) + ";\t\t\ty_" + str(i) + "\t\t=\t" + str(y0) + " +\t" + str('%.4f' % m) + "x;\tinterpolation\n")
                
    # calculate and print interpolations for core 2
    with open("interpolation-core-2.txt", "w") as output_file:
        length = len(core_2_data) - 1
        i = 0
        for i in range(length):
            x0 = core_2_data[i][0]
            x1 = core_2_data[i+1][0]
            y0 = core_2_data[i][1]
            y1 = core_2_data[i+1][1]
            m = ((y0 - y1)/(x0 - x1))
            
            output_file.write(str(x0) + "\t<= x <\t" + str(x1) + ";\t\t\ty_" + str(i) + "\t\t=\t" + str(y0) + " +\t" + str('%.4f' % m) + "x;\tinterpolation\n")
    
    # calculate and print interpolations for core 3
    with open("interpolation-core-3.txt", "w") as output_file:
        length = len(core_3_data) - 1
        i = 0
        for i in range(length):
            x0 = core_3_data[i][0]
            x1 = core_3_data[i+1][0]
            y0 = core_3_data[i][1]
            y1 = core_3_data[i+1][1]
            m = ((y0 - y1)/(x0 - x1))
            
            output_file.write(str(x0) + "\t<= x <\t" + str(x1) + ";\t\t\ty_" + str(i) + "\t\t=\t" + str(y0) + " +\t" + str('%.4f' % m) + "x;\tinterpolation\n")

def main():
    linear_interpolation()

if __name__ == "__main__":

    main()