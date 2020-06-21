#!/usr/bin/env pypy

import txt_reader
import algorithm
import os
import math

directory_name = 'mincut_dataset'

for file in os.listdir(directory_name):
    filename = os.fsdecode(file)
    if filename.startswith("input") and filename.endswith("1_6.txt"): # 40_200
        # assembling corresponding output filename
        file_meta_data = filename.split('_')
        output_filename = "output_random_" + file_meta_data[2] + "_" + file_meta_data[3]

        # assembling input and output file paths
        input_file_path = os.path.join(directory_name, filename)
        output_file_path = os.path.join(directory_name, output_filename)

        # getting the baseline minimum and the graph
        given_minimum =  txt_reader.file_to_minimum(output_file_path)
        gr = txt_reader.file_to_graph(input_file_path)

        k = int(len(gr.V)**2 / 2 * math.log(len(gr.V)) )
        mincut, mean_contraction_time, total_time, discovery_time, error = algorithm.karger(gr, 1000, int(given_minimum))

        print(mincut)
        print(mean_contraction_time)
        print(total_time)
        print(discovery_time)
        print(error)
