#!/usr/bin/env pypy

import txt_reader
import algorithm
import os
import math

directory_name = '../mincut_dataset'
i = 0

files = os.listdir(directory_name)

for file in files:
    filename = os.fsdecode(file)
    if filename.startswith("input") and filename.endswith("200.txt"): # use  and filename.endswith("1_6.txt")  to do a single file
        # assembling corresponding output filename
        file_meta_data = filename.split('_')
        vertices_edges = file_meta_data[2] + "_" + file_meta_data[3].split('.')[0]
        output_filename = "output_random_" + vertices_edges + ".txt"

        # assembling input and output file paths
        input_file_path = os.path.join(directory_name, filename)
        output_file_path = os.path.join(directory_name, output_filename)

        # getting the baseline minimum and the graph
        given_minimum = txt_reader.file_to_minimum(output_file_path)
        gr = txt_reader.file_to_graph(input_file_path)

        n = len(gr.V)
        k = int(((n**2) / 2) * math.log(n))
        timeout = 5 * 60  # 5 minutes timeout, maximum total time: 3.33 hours
        mincut, mean_contraction_time, total_time, discovery_time, error = algorithm.karger(gr, k, int(given_minimum), timeout)

        i += 1
        print('Processed: {} -- {}/{}'.format(vertices_edges, i, int(len(files)/2)))

        results_file_name = 'results_k_theoretical.csv'
        f = open(results_file_name, 'a')
        f.write('{},{},{},{},{},{},{}\n'.format(vertices_edges, k, mincut, mean_contraction_time,
                                           total_time, discovery_time, error))