#!/usr/bin/env pypy

import txt_reader
import algorithm
import os
import time
import math

directory_name = 'mincut_dataset'

for file in os.listdir(directory_name):
    filename = os.fsdecode(file)
    if filename.endswith("1_6.txt"): # 40_200
        file_path = os.path.join(directory_name, filename)
        gr = txt_reader.file_to_graph(file_path)    # reading graph from file

        beg = time.time()
        k = int(len(gr.V)**2 / 2 * math.log(len(gr.V)) )
        mincut = algorithm.karger(gr, 1000)         # Kruskal with union find
        end = time.time()

        print(mincut)