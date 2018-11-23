FROM registry.gitlab.com/rbtech/collab/task29/jupyterhub_base:samuraizer_research

#Change user to root to install libs
USER root

#install git and perl
RUN apt-get install -y  git && apt-get install -y  libxml-dom-perl &&  apt-get install -y  wget && pip install pyrouge

#Install required libs
RUN cd /home/jovyan && git clone https://github.com/OpenNMT/OpenNMT-py && cd OpenNMT-py && pip install -r requirements.txt \
&& cd ../torch_samuraizer/SummaRuNNer && git clone https://github.com/hpzhao/nlp-metrics 

# Throw ports of our image
# 8888 jupyter port 
EXPOSE 8888 

#Install vi
RUN apt-get update 
RUN apt-get install -y vim

#Add data
RUN cd /home/jovyan/OpenNMT-py/data && wget "https://www.dropbox.com/s/1ha6m0dd0x305fx/train.tar.gz?dl=1" -O TRAIN_TAR.tar.gz
RUN cd /home/jovyan/OpenNMT-py/data && tar -xf TRAIN_TAR.tar.gz && cd /home/jovyan/OpenNMT-py/data/data && mv * .. && cd ..   
# Add path
RUN pyrouge_set_rouge_path /home/jovyan/torch_samuraizer/SummaRuNNer/nlp-metrics/ROUGE-1.5.5

# SET path
ENV ROUGE_EVAL_HOME=/home/jovyan/torch_samuraizer/SummaRuNNer/nlp-metrics/ROUGE-1.5.5/data 

#Modify SummaRuNNer's files in order to trace losses and fix bugs
COPY ./main.py /home/jovyan/torch_samuraizer/SummaRuNNer/main.py
COPY ./eval.py /home/jovyan/torch_samuraizer/SummaRuNNer/outputs/eval.py

#Copy start train script and set permissions 
COPY ./setup.py /home/jovyan/
RUN chmod og+rwx /home/jovyan/setup.py
RUN chmod og+rwx /home/jovyan/OpenNMT-py -R
RUN chmod og+rwx /home/jovyan/torch_samuraizer -R

#Change user on jovyan
USER jovyan



