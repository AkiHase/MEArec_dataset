# MEArec_dataset
- Run this python script to get the same datasets that used in our paper. Because [MEArec](https://github.com/alejoe91/MEArec) can produce reproducible datasets.
- These datasets are generated by [MEArec](https://github.com/alejoe91/MEArec) and used to evaluate the performance of Spike Sorting algorithms in our paper. 
- A total of **nine** different specifications of the dataset were prepared, each of which contains **five** copies of data generated using different random seeds. The different random seeds affect the background noise of the signal and the template shape of the spike signal.

# Dependencies
- python 3.7 or above
- [MEArec](https://github.com/alejoe91/MEArec) and its dependencies

# How to run
'''
python genMearecData.py
'''
