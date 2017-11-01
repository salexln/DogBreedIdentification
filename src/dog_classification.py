#!/usr/bin/env python

import argh

from image_classifier import ImageClassifier




@argh.arg('--train-data', help='Train data dir', type=str, required=True)
def main(**kwargs):
    classifier = ImageClassifier(train_dir=kwargs['train_data'])
    classifier.train()
    classifier.test()



if __name__ == "__main__":
    parser = argh.ArghParser()
    parser.set_default_command(main)
    parser.dispatch()