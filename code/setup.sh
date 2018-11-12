#!/bin/bash


#SummaRuNNer train
echo "SummaRuNNer training, test and metric calculation"
cd torch_samuraizer/SummaRuNNer
# in case of CUDA device available use: python main.py -device 0 -batch_size 32 -model RNN_RNN -seed 1 -save_dir checkpoints/XXX.pt
python main.py -batch_size 32 -model RNN_RNN -seed 1 -save_dir checkpoints/new_
# in case of CUDA device available use: python main.py -device 0 -batch_size 1 -test -load_dir checkpoints/new_RNN_RNN_seed_1.pt
python main.py -batch_size 1 -test -load_dir checkpoints/new_RNN_RNN_seed_1.pt
cd outputs
#ROUGE metric computation
./eval.py | tail -n 12 > ../result.txt
cd ..
cat result.txt


#openNMT
echo "openNMT training"
cd ~




