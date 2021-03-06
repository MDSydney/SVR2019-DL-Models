#!/usr/bin/python

from svr2019.datasets import *
from svr2019.sumarize import *
import os


path_list = list()
dataset_list = ['baron-human','campbell','chen','macosko','marques','shekar']
#for dataset in os.listdir('data/embeddings/'):
#for dataset in ['koh']:
for dataset in dataset_list:
    ds = DuoBenchmark('data/datasets/'+dataset+'.csv')
    labels = ds.tags
    for reduction in os.listdir('data/embeddings/'+dataset):
#    for reduction in ['sdae']:
        for item in os.listdir('data/embeddings/'+dataset+'/'+reduction):
            path_list.append((os.path.join('data/embeddings/',dataset,reduction,item),dataset,labels))

print_summaries(path_list)

#for dataset in os.listdir('data/embeddings/'):
for dataset in dataset_list:
    ds = DuoBenchmark('data/datasets/'+dataset+'.csv',log_trans=False)
    labels = ds.tags
    points = ds.data
    summary_dict = internal_summary(points, labels)
    print(','.join([dataset] + [str(summary_dict[x]) for x in sorted(summary_dict.keys())]))
