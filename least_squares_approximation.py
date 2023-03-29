#! /usr/bin/env python3

from process_temps import process_temps
import sys

input_temps = sys.argv[1]

def least_squares_approximation(core_data, core_output_file=str):
   
    # :param core_data              core_data lists contain a list of lists in the form [time][temperature]
    #                               e.g., core_data[0][0] refers to the time of the 0th element, core_data[0][1] refers
    #                               to the temperature of the 0th element
    # :param core_output_file       file to which results should be written


    # calculate and print global linear least squares approximation (c_0 and c_1) for each core,
    # and display it in the form 0 <= x <= length, y = c_0 + c_1x; least-squares
    # ***NOTE: all answers are rounded to 6 decimal places to achieve readability while maintaining accuracy***
    # This is based on the special linear discrete case of the Ac|b or XTX|XTY methods of least squares approximation:
    # c_1 = [k*(i=0)E(k-1) x_i f(x_i) - (i=0)E(k-1)x_i * (i=0)E(k-1) f(x_i)] / [k*(i=0)E(k-1) (x_i)^2 - ((i=0)E(k-1) x_i)^2]
    # c_0 = [(i=0)E(k-1) f(x_i) / k] - [(i=0)E(k-1)x_i / k]*c_1

    
    # c1
        # all sums are over the number of inputs (from i = 0 to length of core_data list - 1)
        # length:                   number of inputs (i.e., length of core_data list - 1); corresponds to k
        # numerator:                (length * sum1) - (sum2 * sum3)
        # divided by denominator:   (length * sum4) - (sum2 * sum2)
        # sum_time_temp:            sum of time*temp
        # sum_time:                 sum of time
        # sum_temp:                 sum of temp
        # sum_time_time:            sum of time*time

    # c0
        # length:                   number of inputs (i.e., length of core_data list); corresponds to k
        # term1:                    sum3 / length
        # term2:                    (sum2 * c1) / length

    with open(core_output_file, "w") as output_file:

        length = len(core_data)
        
        # calculate c1
        sum_time_temp = 0
        for i in range(length):
            sum_time_temp += core_data[i][0]*core_data[i][1]

        sum_time = 0
        for i in range(length):
            sum_time += core_data[i][0]
        
        sum_temp = 0
        for i in range(length):
            sum_temp += core_data[i][1]
 
        sum_time_time = 0
        for i in range(length):
            sum_time_time += core_data[i][0]*core_data[i][0]

        numerator   = (length * sum_time_temp) - (sum_time * sum_temp)
        denominator = (length * sum_time_time) - (sum_time * sum_time)
        c_1 = numerator / denominator

        # calculate c0
        term_0 = sum_temp / length
        term_1 = (sum_time * c_1) / length
        c_0 = term_0 - (term_1)
        
        # display results
        output_file.write(str(core_data[0][0]) + "\t<= x <\t" + str(core_data[length-1][0]) + ";\t\ty =\t" + str('%.6f' % c_0) + "\t+\t" + str('%.6f' % c_1) + "x;\tleast-squares")       
    

def main():
    core_0_data = []
    core_1_data = []
    core_2_data = []
    core_3_data = []

    process_temps(input_temps, core_0_data, core_1_data, core_2_data, core_3_data)

    least_squares_approximation(core_0_data, "least-squares-0.txt")
    least_squares_approximation(core_1_data, "least-squares-1.txt")
    least_squares_approximation(core_2_data, "least-squares-2.txt")
    least_squares_approximation(core_3_data, "least-squares-3.txt")


if __name__ == "__main__":

    main()
