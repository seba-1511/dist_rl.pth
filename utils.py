#!/usr/bin/env python

from argparse import ArgumentParser

def parse_args():
    # Parse arguments
    parser = ArgumentParser()
    parser.add_argument('--expname', '-e', dest='exp', metavar='e', type=str,
            required=True, help='Name of the experiment to be run.')
    parser.add_argument('--env', dest='env', type=str,
            required=True, help='Name of the environment to learn.')
    parser.add_argument('--filter', dest='filter', type=bool,
            default=True, help='Whether to filter the environment\'s states.')
    parser.add_argument('--solved', dest='solved', type=float,
            default=np.inf, help='Threshold at which the environment is considered solved.')
    parser.add_argument('--n_iter', dest='n_iter', type=int,
            default=300, help='Number of updates to be performed.')
    parser.add_argument('--timesteps_per_batch', dest='timesteps_per_batch', type=int,
            default=15000, help='Number of steps before updating parameters.')
    parser.add_argument('--max_path_length', dest='max_path_length', type=int,
            default=5000, help='Max length for a trajectory/episode.')
    parser.add_argument('--momentum', dest='momentum', type=float,
            default=0.0, help='Default momentum value.')
    parser.add_argument('--gae', dest='gae', type=bool,
            default=True, help='Whether to use GAE.')
    parser.add_argument('--gae_lam', dest='gae_lam', type=float,
            default=0.97, help='Lambda value for GAE.')
    parser.add_argument('--delta', dest='delta', type=float,
            default=0.01, help='Max KL divergence for TRPO')
    parser.add_argument('--cg_damping', dest='cg_damping', type=float,
            default=0.1, help='Damping used to make CG positive def.')
    parser.add_argument('--gamma', dest='gamma', type=float,
            default=0.99, help='Discount factor.')
    parser.add_argument('--record', dest='record', type=bool,
            default=False, help='Whether to record videos at test time.')
    parser.add_argument('--upload', dest='upload', type=bool,
            default=False, help='Whether to upload results to the OpenAI servers.')



