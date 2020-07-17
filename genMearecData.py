#!/usr/bin/python
# -*-coding:utf-8 -*-
# author: Yangtao Jiang 07-17-2020
# brief: generate the same MEArec datasets used in our paper.
import os

print("-------generate templates-------")
os.system("mkdir templates && mearec set-templates-folder templates/")
prbTypes = ["tetrode-mea-l -n 30", "Neuropixels-24 -n 100",
 "Neuronexus-32 -n 100", " Neuropixels-64 -n 100", "Neuropixels-128 -n 100"]
for i in range(len(prbTypes)):
    os.system(f"mearec gen-templates -prb {prbTypes[i]} --seed 0")

print("-------generate recordings-------")
os.system("mkdir recordings && mearec set-recordings-folder recordings/")
seeds = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1]] # five different random seeds

for root, dirs, files in os.walk("./templates/physrot/"):
    # select a random seed
    for sd in seeds:
        # select a template
        for f in files:
            tmpPath = os.path.join(root, f)
            # generate recording
            os.system(f"mearec gen-recordings -t {tmpPath} -d 30 -ne 10 -ni 0 --st-seed {sd[0]} --temp-seed {sd[1]} --noise-seed {sd[2]}")
            if (f.split("_")[2]) == "Neuronexus-32":
                for nro in [4,6,8,15]:
                    os.system(f"mearec gen-recordings -t {tmpPath} -d 30 -ne {nro} -ni 0 --st-seed {sd[0]} --temp-seed {sd[1]} --noise-seed {sd[2]}")
