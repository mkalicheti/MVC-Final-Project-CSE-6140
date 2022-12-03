import matplotlib.pyplot as plt
import glob
import numpy as np
import os

output_dir = 'output'
# dataset_names = ["as-22july06", "email", "football", "hep-th", "jazz", 
#                 "karate", "netscience", "power", "star", "star2", "delaunay_n10"]
dataset_names = ["football"]
alg = "ls2"
data_results = {k:None for k in dataset_names}
for dataset in dataset_names:
    trace_files_path = os.path.join(output_dir, f"{dataset}_{alg}*.trace")
    temp_data_results = []
    for file in glob.glob(trace_files_path):
        info = open(file, 'r').readlines()[-1].split()
        time_taken = float(info[0][:-1])
        nVC = int(info[-1])
        temp_data_results.append([time_taken, nVC])
    avg_temp_data_results = np.mean(temp_data_results, axis=0)
    data_results[dataset] = (avg_temp_data_results[0], int(avg_temp_data_results[1]))
    print(f"{dataset} | {data_results[dataset][0]} | {data_results[dataset][1]}")