#!/usr/bin/env python3
import argparse
import sys
import os


#command line argument parser. What else arguments do we need?
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', nargs='?', default='10')
    parser.add_argument('--smr_batch', nargs='?', default='32')
    parser.add_argument('--smr_svdir', nargs='?', default='test')
    parser.add_argument('--onmt_valid_batch', nargs='?', default='32')
    parser.add_argument('--onmt_batch', nargs='?', default='64')
    parser.add_argument('--onmt_steps', nargs='?', default='1000')
    parser.add_argument('--onmt_valid_steps', nargs='?', default='10000')
    return parser

if __name__ == '__main__':
    log = open("train_res.log", "w")
    parser = createParser()
    args = parser.parse_args(sys.argv[1:])
    pid_summarunner = os.fork()
    if (pid_summarunner != 0):
        pid_opennmt = os.fork()
    else:
        pid_opennmt = -1
    if (pid_summarunner == 0):
        os.chdir("/home/jovyan/torch_samuraizer/SummaRuNNer")
        status = os.system("./main.py -batch_size "+str(args.smr_batch)+" -model RNN_RNN -seed 1 -device 1 -save_dir checkpoints/"+str(args.smr_svdir) +  " -log_file smr.log -epochs "+str(args.epochs)) #it seems that parameters should be passed as a single string
        if (status != 0):
            sys.exit(1)
    elif (pid_opennmt == 0):
        #launch opennmt
        os.chdir("/home/jovyan/OpenNMT-py")
        #status = os.system("python preprocess.py -train_src data/src-train.txt -train_tgt data/tgt-train.txt -valid_src data/src-val.txt -valid_tgt data/tgt-val.txt -save_data data/corpus")
        #if (status != 0):
            #sys.exit(1)
        os.environ["CUDA_VISIBLE_DEVICES"] = "0"
        status = os.system("./train.py -data data/corpus -save_model corpus_model -world_size 1 -gpu_ranks 0 -batch_size "+str(args.onmt_batch)+  " -seed 1  -log_file omnt.log -train_steps "+str(args.onmt_steps) + " -valid_steps "+str(args.onmt_valid_steps)) 
        if (status != 0):
            sys.exit(1)
        #sys.exit(0)
    else:
        #wait for processes to exit
        res1 = os.waitid(os.P_PID, pid_summarunner, os.WEXITED)
        res2 = os.waitid(os.P_PID, pid_opennmt, os.WEXITED)
        print(str(res1.si_status)+" "+str(res2.si_status))
        log.write("Training finished, ")
        if ((res1.si_status == 0) & (res2.si_status == 0)):
            log.write("no erros encountered\n")
            log.close()
            sys.exit(0)
        elif ((res1.si_status != 0) & (res2.si_status == 0)):
            log.write("SummaRuNNer finished with error\n")
            log.close()
            sys.exit(1)
        elif ((res1.si_status == 0) & (res2.si_status != 0)):
            log.write("OpenNMT finished with error\n")
            log.close()
            sys.exit(1)
        else:
            log.write("both NNs finshed with errors\n")
            log.close()
            sys.exit(1)
