#!/usr/bin/env python3
import unittest
import os
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH, "src")
sys.path.append(SOURCE_PATH)
from dnastore.converter import DNAStore

INPUT = "This is a test."
ENCODED = DNAStore.encode(INPUT)

OUTPUT = [
    "TCGTACGTACGTACGTACGTACATCGCGAGCACACGCGCTAGTGCACATCATATCGACATGTGCTGTCTCACATCAGTGCTGTACTCGCATCGCAGTATCGATACGTACGTACGTCG",
    "TACGTACGTACGTACGTACGTACGTACGATACTGCGATGCGAGTACAGCACTGATGTGAGACAGCACATGTCGATATGATGTGCACTAGCGCGTGTGCTCGATACGTACGTACGAGC",
]


class TestEncode(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(ENCODED[1], OUTPUT[1])


if __name__ == "__main__":
    unittest.main()
