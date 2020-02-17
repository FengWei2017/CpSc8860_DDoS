#!/usr/bin/env python
"""
Example code to plot time series for ECE 8930 second assignment
tshark, matplotlib, and numpy are required packages for this example code
"""
import read_pcap
import time_series
import rand_arr_time

def example1_plot_time_series_from_pcap_file():
    """
    This is an example usage of read_pcap.py
    read_pcap.py reads data from pcap file
    """
    files='*.pcap*'                         # Pcap(ng) files location
    columns=['frame.time_epoch']            # Linux time
    filter_str=''                           # Filter String
    output_file='a.txt'                     # Output file
    data=read_pcap.read_pcap_files(files, columns, filter_str, output_file) # Get packets' Linux time, the output is a list of string
    arrive_time=[float(item[0])-float(data[0][0]) for item in data]         # Format the list of strings to a list of floating numbers
    time_series.plot_time_series(arrive_time)   # Plot time series using packets arrive time

def example2_plot_time_series_from_simulated_data():
    """
    This is an example usage of rand_arr_time.py
    rand_arr_time.py generate a random integer list
    """
    option=6                                # There are 6 options in total, each use different method to generate random arriving times
    Number_of_packets=10000               # Number of packets generated
    expected_duratation=1000                # Expected length of time in seconds
    arrive_time=rand_arr_time.rand_arr_time(option,Number_of_packets,expected_duratation)  # Get packet arrive time, with option 3, 100000 packets, expected in 1000 seconds.
    time_series.plot_time_series(arrive_time)   # Plot time series using packets arrive time


def main():
    example1_plot_time_series_from_pcap_file()
    example2_plot_time_series_from_simulated_data()

if __name__ == '__main__':
    main()
