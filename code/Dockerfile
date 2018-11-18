FROM registry.gitlab.com/rbtech/collab/task29/jupyterhub_base:samuraizer_research

#Change user to root to install libs
USER root

#install git and perl
RUN apt-get install -y  git && apt-get install -y  libxml-dom-perl && pip install pyrouge

#Install required libs
RUN cd /home/jovyan && git clone https://github.com/OpenNMT/OpenNMT-py && cd OpenNMT-py && pip install -r requirements.txt \
&& cd ../torch_samuraizer/SummaRuNNer && git clone https://github.com/hpzhao/nlp-metrics 

# Add path
RUN pyrouge_set_rouge_path /home/jovyan/torch_samuraizer/SummaRuNNer/nlp-metrics/ROUGE-1.5.5

# SET path
ENV ROUGE_EVAL_HOME=/home/jovyan/torch_samuraizer/SummaRuNNer/nlp-metrics/ROUGE-1.5.5/data 

#Change user on jovyan
USER jovyan

#Modify SummaRuNNer's files in order to trace losses and fix bugs
COPY ./main.py /home/jovyan/torch_samuraizer/SummaRuNNer/main.py
COPY ./eval.py /home/jovyan/torch_samuraizer/SummaRuNNer/outputs/eval.py

# Throw ports of our image
# 8888 jupyter port 
EXPOSE 8888 


