import os
import sys
import copy
import pickle
import argparse
import networkx as nx
import numpy as np
from ndl_old import Wtd_NNetwork
from ndl_old import NetDictLearner
from ndl_old import utils
from NNetwork import NNetwork as nn

# sys.path.insert(0, ".")
from utils import *

parser = argparse.ArgumentParser(
    description="Argument Parser for Generation of Data for Network DYnamics Reconstruction"
)
parser.add_argument(
    "-m",
    "--model",
    default="HK",
    type=str,
    choices=["HK"],
    help="Opinion Dynamics model to use for simulation",
)
parser.add_argument(
    "-n",
    "--network",
    default="NWS",
    type=str,
    choices=["NWS", "BA", "ER"],
    help="Underlying Parent Network to sample subgraphs from",
)
parser.add_argument(
    "-k",
    "--samplek",
    default=25,
    type=int,
    help="Number of nodes in the sampled subgraphs",
)
parser.add_argument(
    "-data",
    "--data_dir",
    default="data/reconstruction_data",
    type=str,
    help="Directory to store generated data",
)
parser.add_argument(
    "-seed",
    "--seed",
    default=0,
    type=int,
    help="Set reproducibility seed",
)
args = parser.parse_args()

# Set seed
set_seed(args.seed)

widthTable = {"HK": widthOD}

sample_k, model = args.samplek, args.model
num_nodes, probability, auxiliary = 450, 0.25, 10

if args.network == "NWS":
    G_net = nx.newman_watts_strogatz_graph(num_nodes, auxiliary, probability)
elif args.network == "BA":
    G_net = nx.barabasi_albert_graph(num_nodes, auxiliary)
elif args.network == "ER":
    G_net = nx.erdos_renyi_graph(num_nodes, probability)
else:
    raise NotImplementedError(f"{args.network} is not yet supported.")

new_nodes = {e: n for n, e in enumerate(G_net.nodes, start=0)}
new_edges = [(new_nodes[e1], new_nodes[e2]) for e1, e2 in G_net.edges]
edgelist = []
for i in range(len(new_edges)):
    temp = [str(new_edges[i][0]), str(new_edges[i][1])]
    edgelist.append(temp)
G_nn = nn.NNetwork()
G_nn.add_edges(edgelist)
A_new = G_nn.get_adjacency_matrix()
num_nodes_new = G_nn.num_nodes()

s = np.random.rand(num_nodes_new)
op_eps = np.random.rand()
max_rounds = 149
label = False
dynamics = hk_local(A_new, s, op_eps, max_rounds, eps=1e-7, conv_stop=False)
if ((np.max(dynamics[-1]) - np.min(dynamics[-1])) < 1e-3) or (np.std(dynamics[-1]) < 1e-3):
    label = True

######### Rank 4 #########

NDL_NWS_rank4 = NetDictLearner(G=G_nn, dynamics=dynamics, n_components=4, k=25, MCMC_iterations=500)
NDL_NWS_rank4.train_dict()

save_dict = {
        'Adjacency Matrices': NDL_NWS_rank4.result_dict['Adjacency Matrices'],
        'Dynamics': NDL_NWS_rank4.result_dict['Dynamics Learned'],
}

with open(f"{args.data_dir}/{model}_{args.network}_{sample_k}_rank4.pkl", "wb") as output_file:
    pickle.dump(save_dict, output_file)

##########################

######### Rank 9 #########

NDL_NWS_rank9 = NetDictLearner(G=G_nn, dynamics=dynamics, n_components=9, k=25, MCMC_iterations=500)
NDL_NWS_rank9.train_dict()

save_dict = {
        'Adjacency Matrices': NDL_NWS_rank9.result_dict['Adjacency Matrices'],
        'Dynamics': NDL_NWS_rank9.result_dict['Dynamics Learned'],
}

with open(f"{args.data_dir}/{model}_{args.network}_{sample_k}_rank9.pkl", "wb") as output_file:
    pickle.dump(save_dict, output_file)

##########################

######### Rank 16 #########

NDL_NWS_rank16 = NetDictLearner(G=G_nn, dynamics=dynamics, n_components=16, k=25, MCMC_iterations=500)
NDL_NWS_rank16.train_dict()

save_dict = {
        'Adjacency Matrices': NDL_NWS_rank16.result_dict['Adjacency Matrices'],
        'Dynamics': NDL_NWS_rank16.result_dict['Dynamics Learned'],
}

with open(f"{args.data_dir}/{model}_{args.network}_{sample_k}_rank16.pkl", "wb") as output_file:
    pickle.dump(save_dict, output_file)

##########################

######### Rank 25 #########

NDL_NWS_rank25 = NetDictLearner(G=G_nn, dynamics=dynamics, n_components=25, k=25, MCMC_iterations=500)
NDL_NWS_rank25.train_dict()

save_dict = {
        'Adjacency Matrices': NDL_NWS_rank25.result_dict['Adjacency Matrices'],
        'Dynamics': NDL_NWS_rank25.result_dict['Dynamics Learned'],
}

with open(f"{args.data_dir}/{model}_{args.network}_{sample_k}_rank25.pkl", "wb") as output_file:
    pickle.dump(save_dict, output_file)

##########################

######### Rank 36 #########

NDL_NWS_rank36 = NetDictLearner(G=G_nn, dynamics=dynamics, n_components=36, k=25, MCMC_iterations=500)
NDL_NWS_rank36.train_dict()

save_dict = {
        'Adjacency Matrices': NDL_NWS_rank36.result_dict['Adjacency Matrices'],
        'Dynamics': NDL_NWS_rank36.result_dict['Dynamics Learned'],
}

with open(f"{args.data_dir}/{model}_{args.network}_{sample_k}_rank36.pkl", "wb") as output_file:
    pickle.dump(save_dict, output_file)

##########################