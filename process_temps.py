#! /usr/bin/env python3

from parse_temps import (parse_raw_temps)

"""
    Organize the parsed temperatures and times into 4 lists, 
    with each list containing both time and temperature
    
"""

def process_temps(input_temps, core_0_data, core_1_data, core_2_data, core_3_data):
    with open(input_temps) as temps_file:
        for time, core_data in parse_raw_temps(temps_file):
            current_input_0 = [time,core_data[0]]
            current_input_1 = [time,core_data[1]]
            current_input_2 = [time,core_data[2]]
            current_input_3 = [time,core_data[3]]
            core_0_data.append(current_input_0)
            core_1_data.append(current_input_1)
            core_2_data.append(current_input_2)
            core_3_data.append(current_input_3)

