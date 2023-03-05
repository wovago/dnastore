import unittest
import os
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH, "src")
sys.path.append(SOURCE_PATH)
from dnastore.dnastore import DNAStore

key_file = os.path.join(PROJECT_PATH, "test", "dna.key")

INPUT = "This is a test."
ENCODED = DNAStore.encode(INPUT, encrypt=True, key_file=key_file)

OUTPUT = [
    "ACGCATCAGACTGCAGTGTGTCGACAGTGTGTGCGACGTACTGAGCTCATAGCAGCATGCTGACGAGTCTGTAGTCTACATGCATGAGCAGCTGCGTCAGAGCGTACGTACGTACTG",
    "TAGAGTATACTCATCATCAGCACAGCGTGCGAGCGAGTCAGTCGAGCGAGACGATCGTACTCGCTGACACTCGTAGTCATATGAGCTCACATAGCGCTGCGATACGTACGTACGAGC",
]


class TestEncode(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(ENCODED[1], OUTPUT[1])


unittest.main()
