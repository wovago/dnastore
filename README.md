# dnastore

![release](https://img.shields.io/github/v/tag/wovago/dnastore?color=fuchsia&label=latest/stable&logo=github)
![build status](https://img.shields.io/github/actions/workflow/status/wovago/dnastore/tox-matrix.yml?color=green&label=CI&logo=github)
![language](https://img.shields.io/github/languages/top/wovago/dnastore?color=blue&logo=python&logoColor=yellow)

## Introduction

Simple Python package for DNA storage that converts text strings into DNA strings and vice versa. This package implements the algorithm described in "Towards practical, high-capacity, low-maintenance information storage in synthesized DNA" (Goldstein et al, 2013) to store information into DNA. Algorithm details are provided in the [supplementary information](docs/algorithm.pdf)

For more information, please see https://www.nature.com/articles/nature11875#Sec2


## Installation

```
git clone https://github.com/wovago/dnastore
cd dnastore
pip install .
```


## Usage

The basic workflow to encode a string into DNA and decode DNA back into a string is a follows:

```
from dnastore.converter import DNAStore 

DNAStore.encode('Hello world!')
DNAStore.decode(['ACGTACGTACGTACGTACGTACACACACTCGCGTAGTGACTATCGACAGACGCAGCGTGTCGCTCGACTAGTGACTGCTACTACTCGTACGTACGTACGTAGCGTACGTACGTACTC'])

```


If you want to encrypt and decrypt the text stored in DNA, you will need to generate a random key. This key will be needed to encrypt the input text and decrypt the DNA string as follows: 


```
from dnastore.converter import DNAStore

DNAStore().generate_key('dna.key)
DNAStore().encode("hello world", encrypt=True, key_file="dna.key")
DNAStore().decode(['ACTACAGCTGCTGCATGACTCGCGTCTGCGTCTACGCTACGCGCAGCAGCTACTAGCTGATGACTATCATACGATAGCTGCGTCTACATGATCTAGTGAGTCACGTACGTACGTAGC'], decrypt=True, key_file="my.key")
```

