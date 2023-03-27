#!/usr/bin/env python3
import unittest
import os
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH, "src")
sys.path.append(SOURCE_PATH)
from dnastore.converter import DNAStore

key_file = os.path.join(PROJECT_PATH, "test", "test.key")

INPUT = "This is a test."
ENCODED = DNAStore.encode(INPUT, encrypt=True, key_file=key_file)

ENCRYPTED = [
    "ACGCATCAGACTGCAGTGTGTCGACAGTGTGTGCGACGTACTGAGCTCATAGCAGCATGCTGACGAGTCTGTAGTCTACATGCATGAGCAGCTGCGTCAGAGCGTACGTACGTACTG",
    "TAGAGTATACTCATCATCAGCACAGCGTGCGAGCGAGTCAGTCGAGCGAGACGATCGTACTCGCTGACACTCGTAGTCATATGAGCTCACATAGCGCTGCGATACGTACGTACGAGC",
]
DECRYPTED = DNAStore.decode(ENCRYPTED, decrypt=True, key_file=key_file)

INPUT = "This is a test."


class TestDecrypt(unittest.TestCase):
    def test_decrypt(self):
        self.assertEqual(DECRYPTED, INPUT)


if __name__ == "__main__":
    unittest.main()
