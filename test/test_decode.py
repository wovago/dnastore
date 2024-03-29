#!/usr/bin/env python3
import unittest
import os
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH, "src")
sys.path.append(SOURCE_PATH)
from dnastore.converter import DNAStore


ENCODED = [
    "TCGTACGTACGTACGTACGTACATCGCGAGCACACGCGCTAGTGCACATCATATCGACATGTGCTGTCTCACATCAGTGCTGTACTCGCATCGCAGTATCGATACGTACGTACGTCG",
    "TACGTACGTACGTACGTACGTACGTACGATACTGCGATGCGAGTACAGCACTGATGTGAGACAGCACATGTCGATATGATGTGCACTAGCGCGTGTGCTCGATACGTACGTACGAGC",
]
DECODED = DNAStore.decode(ENCODED)

INPUT = "This is a test."


class TestDecode(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(DECODED, INPUT)


if __name__ == "__main__":
    unittest.main()
