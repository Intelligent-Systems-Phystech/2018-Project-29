#!/usr/bin/env python3
import argparse
import sys
import os

#command line argument parser. What else arguments do we need?
def createParser ():
	parser = argparse.ArgumentParser()
	parser.add_argument('--epochs', nargs='?', default='5')
	parser.add_argument('--smr_batch', nargs='?', default='10')
	parser.add_argument('--smr_svdir', nargs='?', default='test')
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
		os.execv("/home/jovyan/torch_samuraizer/SummaRuNNer/main.py", ["-batch_size "+str(args.smr_batch)+"-model RNN_RNN -seed 1 -save_dir checkpoints/"+str(args.smr_svdir), " -log_file smr.log -epochs "+str(args.epochs)]) #it seems that parameters should be passed as a single string
	elif (pid_opennmt == 0):
		#launch opennmt
		os.execl("./2.py", "5")
		#sys.exit(1)
	else:
		print ("wait")
		res1 = os.waitid(os.P_PID, pid_summarunner, os.WEXITED)
		res2 = os.waitid(os.P_PID, pid_opennmt, os.WEXITED)
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
