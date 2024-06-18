import os
import sys
import copy
import pickle
import argparse
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
# from ndl import NetDictLearner
# from ndl import utils
from ndl import ndl, onmf
from NNetwork import NNetwork as nn

# sys.path.insert(0, ".")
from utils import *

parser = argparse.ArgumentParser(
    description="Argument Parser for Generation of Data for Network DYnamics Reconstruction"
)
parser.add_argument(
    "-m",
    "--model",
    default="FCA",
    type=str,
    choices=["FCA", "KURA"],
    help="Coupled Oscillator Dynamics model to use for simulation",
)
parser.add_argument(
    "-n",
    "--network",
    default="NWS",
    type=str,
    choices=["NWS", "BA", "ER", "Caltech"],
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
    default="data/reconstruction_data_k20",
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

widthTable = {"FCA": widthFCA, "KURA": widthKURA}
phiTable = {"FCA": FCA, "KURA": Kuramoto}

sample_k, model = args.samplek, args.model
num_nodes, probability, auxiliary = 450, 0.25, 10

if args.network == "NWS":
    G_net = nx.newman_watts_strogatz_graph(num_nodes, auxiliary, probability, seed=args.seed)
elif args.network == "BA":
    G_net = nx.barabasi_albert_graph(num_nodes, auxiliary, seed=args.seed)
elif args.network == "ER":
    G_net = nx.erdos_renyi_graph(num_nodes, probability, seed=args.seed)
elif args.network == "Caltech":
    G_net = nx.Graph()
    path = "network_data/caltech.txt"
    edgelist = list(np.genfromtxt(path, delimiter=",", dtype=str))
    for e in edgelist:
        G_net.add_edge(e[0], e[1])
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
num_nodes_new = G_nn.num_nodes()

s = np.random.randint(0, 5, num_nodes_new)
kappa = 5
dynamics, label = phiTable[model](G_nn, s, kappa, iteration=150)

k = 20
rank_list = [4, 9, 16, 25, 36]
# 0.32794339934203004
for n_components in rank_list:
    reconstructor = ndl.Network_Reconstructor(G=G_nn,  # networkx simple graph
                                        dynamics = dynamics,
                                        n_components=n_components,  # num of dictionaries
                                        MCMC_iterations=200,
                                        # MCMC steps (macro, grow with size of ntwk)
                                        k1=0, k2=k-1,  # left and right arm lengths
                                        # keep false to use Pivot chain for recons.
                                        omit_folded_edges=True)
    reconstructor.train_dict()

    save_dict = reconstructor.result_dict

    with open(f"{args.data_dir}/{model}_{args.network}_{n_components}.pkl", "wb") as output_file:
        pickle.dump(save_dict, output_file)

    W = reconstructor.W # Network dictionary to be used for reconstruction
    reconstructor1 = ndl.Network_Reconstructor(G=G_nn,  #  simple graph
                                    dynamics = dynamics,
                                    n_components=W.shape[1],  # num of dictionaries
                                    MCMC_iterations=200,  # MCMC steps (macro, grow with size of ntwk)
                                    k2=k-1)  # left and right arm length

    nc = W.shape[1]

    G_recons = reconstructor.reconstruct_network(W = W, recons_iter=10000) # rank-k mesoscale reconstruction of G

    try:
        G_recons_1 = G_recons.threshold2simple(0.1)
        recons_metrics_1 = reconstructor1.compute_recons_accuracy(G_recons_1, output_full_metrics=True)
    except IndexError:
        recons_metrics_1 = {"Jaccard_recons_accuracy": 0.0}

    try:
        G_recons_2 = G_recons.threshold2simple(0.2)
        recons_metrics_2 = reconstructor1.compute_recons_accuracy(G_recons_2, output_full_metrics=True)
    except IndexError:
        recons_metrics_2 = {"Jaccard_recons_accuracy": 0.0}

    try:
        G_recons_3 = G_recons.threshold2simple(0.3)
        recons_metrics_3 = reconstructor1.compute_recons_accuracy(G_recons_3, output_full_metrics=True)

    except IndexError:
        recons_metrics_3 = {"Jaccard_recons_accuracy": 0.0}

    try:
        G_recons_4 = G_recons.threshold2simple(0.4)
        recons_metrics_4 = reconstructor1.compute_recons_accuracy(G_recons_4, output_full_metrics=True)

    except IndexError:
        recons_metrics_4 = {"Jaccard_recons_accuracy": 0.0}

    try:
        G_recons_5 = G_recons.threshold2simple(0.5)
        recons_metrics_5 = reconstructor1.compute_recons_accuracy(G_recons_5, output_full_metrics=True)

    except IndexError:
        recons_metrics_5 = {"Jaccard_recons_accuracy": 0.0}

    try:
        G_recons_6 = G_recons.threshold2simple(0.6)
        recons_metrics_6 = reconstructor1.compute_recons_accuracy(G_recons_6, output_full_metrics=True)

    except IndexError:
        recons_metrics_6 = {"Jaccard_recons_accuracy": 0.0}

    try:
        G_recons_7 = G_recons.threshold2simple(0.7)
        recons_metrics_7 = reconstructor1.compute_recons_accuracy(G_recons_7, output_full_metrics=True)

    except IndexError:
        recons_metrics_7 = {"Jaccard_recons_accuracy": 0.0}

    try:
        G_recons_8 = G_recons.threshold2simple(0.8)
        recons_metrics_8 = reconstructor1.compute_recons_accuracy(G_recons_8, output_full_metrics=True)

    except IndexError:
        recons_metrics_8 = {"Jaccard_recons_accuracy": 0.0}

    try:
        G_recons_9 = G_recons.threshold2simple(0.9)
        recons_metrics_9 = reconstructor1.compute_recons_accuracy(G_recons_9, output_full_metrics=True)

    except IndexError:
        recons_metrics_9 = {"Jaccard_recons_accuracy": 0.0}

    try:
        G_recons_10 = G_recons.threshold2simple(1.0)
        recons_metrics_10 = reconstructor1.compute_recons_accuracy(G_recons_10, output_full_metrics=True)

    except IndexError:
        recons_metrics_10 = {"Jaccard_recons_accuracy": 0.0}

    with open(f"reconstruction_metrics/{args.network}_k{k}.txt", "a") as output_file:
        output_file.write(f"Rank: {n_components}\n")
        output_file.write(f"\t[{recons_metrics_1.get('Jaccard_recons_accuracy')}, \
                            {recons_metrics_2.get('Jaccard_recons_accuracy')}, \
                            {recons_metrics_3.get('Jaccard_recons_accuracy')}, \
                            {recons_metrics_4.get('Jaccard_recons_accuracy')}, \
                            {recons_metrics_5.get('Jaccard_recons_accuracy')}, \
                            {recons_metrics_6.get('Jaccard_recons_accuracy')}, \
                            {recons_metrics_7.get('Jaccard_recons_accuracy')}, \
                            {recons_metrics_8.get('Jaccard_recons_accuracy')}, \
                            {recons_metrics_9.get('Jaccard_recons_accuracy')}, \
                            {recons_metrics_10.get('Jaccard_recons_accuracy')}]\n")
    