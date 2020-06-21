#!/usr/bin/env pypy

import txt_reader
import algorithm
import os

directory_name = 'mincut_dataset'
i = 0

files = os.listdir(directory_name)

for file in files:
    filename = os.fsdecode(file)
    if filename.startswith("input"): # use  and filename.endswith("1_6.txt")  to do a single file
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

        k = 10
        mincut, mean_contraction_time, total_time, discovery_time, error = algorithm.karger(gr, k, int(given_minimum))

        i += 1
        print('Processed: {} -- {}/{}'.format(vertices_edges, i, int(len(files)/2)))

        results_file_name = 'results_k_{}.csv'.format(k)
        f = open(results_file_name, 'a')
        f.write('{},{},{},{},{},{}\n'.format(vertices_edges, mincut, mean_contraction_time,
                                           total_time, discovery_time, error))
