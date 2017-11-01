#!/usr/bin/env python

import argh
import os



@argh.arg('--train-data', help='Train data dir', type=str, required=True)
def main(**kwargs):
    print kwargs['train_data']



if __name__ == "__main__":
    parser = argh.ArghParser()
    parser.set_default_command(main)
    parser.dispatch()