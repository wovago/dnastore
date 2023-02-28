#!/usr/bin/env python
# *_* coding: utf-8 *_*

import secrets
import string
import textwrap
from itertools import accumulate
from operator import add, itemgetter, sub
from random import randint


class DNAStore:
    # Ditionary with huffman code generated from
    # htps://www.ebi.ac.uk/goldman-srv/DNA-storage/orig_files/View_huff3.cd.new
    __HUFFMAN_DICT = {
        0: "22201",
        1: "00100",
        2: "11220",
        3: "00211",
        4: "20222",
        5: "00222",
        6: "02211",
        7: "222110",
        8: "22002",
        9: "02100",
        10: "22001",
        11: "222122",
        12: "12001",
        13: "02021",
        14: "10100",
        15: "02010",
        16: "20101",
        17: "12211",
        18: "12120",
        19: "11111",
        20: "21211",
        21: "21221",
        22: "20220",
        23: "00122",
        24: "20022",
        25: "12121",
        26: "21111",
        27: "00221",
        28: "00202",
        29: "222202",
        30: "222102",
        31: "00010",
        32: "02212",
        33: "10011",
        34: "22011",
        35: "02221",
        36: "21212",
        37: "21021",
        38: "11211",
        39: "10111",
        40: "12220",
        41: "22110",
        42: "22101",
        43: "11122",
        44: "22022",
        45: "01210",
        46: "00210",
        47: "02122",
        48: "10122",
        49: "01011",
        50: "11101",
        51: "01102",
        52: "22112",
        53: "12122",
        54: "11012",
        55: "222112",
        56: "02201",
        57: "02011",
        58: "20021",
        59: "222021",
        60: "00022",
        61: "222200",
        62: "222120",
        63: "21010",
        64: "00121",
        65: "02022",
        66: "20100",
        67: "10211",
        68: "21001",
        69: "21210",
        70: "10212",
        71: "222212",
        72: "20110",
        73: "20010",
        74: "21220",
        75: "21022",
        76: "21000",
        77: "01211",
        78: "10220",
        79: "12002",
        80: "12011",
        81: "11212",
        82: "21100",
        83: "12210",
        84: "20112",
        85: "22200",
        86: "22102",
        87: "21222",
        88: "21012",
        89: "12101",
        90: "10120",
        91: "01202",
        92: "10200",
        93: "02210",
        94: "222211",
        95: "11201",
        96: "00102",
        97: "01112",
        98: "22010",
        99: "00012",
        100: "22100",
        101: "20001",
        102: "20202",
        103: "02102",
        104: "20200",
        105: "20210",
        106: "20012",
        107: "11100",
        108: "02101",
        109: "11021",
        110: "00021",
        111: "02110",
        112: "12102",
        113: "01012",
        114: "10101",
        115: "10222",
        116: "10221",
        117: "10002",
        118: "01120",
        119: "00201",
        120: "10020",
        121: "222111",
        122: "222220",
        123: "02111",
        124: "222222",
        125: "00000",
        126: "10112",
        127: "22121",
        128: "02000",
        129: "10000",
        130: "20111",
        131: "00212",
        132: "22021",
        133: "21112",
        134: "11022",
        135: "01220",
        136: "11102",
        137: "20011",
        138: "22111",
        139: "10021",
        140: "12212",
        141: "11202",
        142: "10201",
        143: "02200",
        144: "02002",
        145: "11120",
        146: "20102",
        147: "11110",
        148: "11002",
        149: "22000",
        150: "21002",
        151: "21102",
        152: "222221",
        153: "11020",
        154: "20221",
        155: "01002",
        156: "11001",
        157: "00120",
        158: "02202",
        159: "10202",
        160: "10012",
        161: "22012",
        162: "20211",
        163: "21201",
        164: "00220",
        165: "11222",
        166: "21011",
        167: "10110",
        168: "20002",
        169: "20122",
        170: "22122",
        171: "20201",
        172: "10022",
        173: "21101",
        174: "12110",
        175: "12222",
        176: "00200",
        177: "21202",
        178: "10210",
        179: "10010",
        180: "02012",
        181: "12221",
        182: "12022",
        183: "02222",
        184: "01100",
        185: "02121",
        186: "01122",
        187: "00112",
        188: "01020",
        189: "222100",
        190: "01222",
        191: "21020",
        192: "01201",
        193: "00001",
        194: "12021",
        195: "12010",
        196: "20121",
        197: "21120",
        198: "00002",
        199: "222201",
        200: "00011",
        201: "01010",
        202: "12112",
        203: "11112",
        204: "02120",
        205: "11010",
        206: "01110",
        207: "01212",
        208: "20120",
        209: "12000",
        210: "12100",
        211: "11210",
        212: "11011",
        213: "21200",
        214: "12200",
        215: "01111",
        216: "01200",
        217: "12012",
        218: "10121",
        219: "10102",
        220: "222210",
        221: "00020",
        222: "01000",
        223: "20020",
        224: "11121",
        225: "10001",
        226: "02001",
        227: "01101",
        228: "222121",
        229: "21121",
        230: "02220",
        231: "01001",
        232: "222101",
        233: "01022",
        234: "20212",
        235: "00101",
        236: "222022",
        237: "01021",
        238: "00111",
        239: "11200",
        240: "12201",
        241: "11000",
        242: "02112",
        243: "01221",
        244: "00110",
        245: "11221",
        246: "01121",
        247: "12111",
        248: "12020",
        249: "02020",
        250: "22020",
        251: "20000",
        252: "21110",
        253: "22120",
        254: "12202",
        255: "21122",
        256: "222020",
    }

    __TRIT2DNA_MATRIX = {
        "0": {"A": "C", "C": "G", "G": "T", "T": "A"},
        "1": {"A": "G", "C": "T", "G": "A", "T": "C"},
        "2": {"A": "T", "C": "A", "G": "C", "T": "G"},
    }

    __DNA2TRIT_MATRIX = {
        "A": {"T": "0", "G": "1", "C": "2"},
        "C": {"A": "0", "T": "1", "G": "2"},
        "G": {"C": "0", "A": "1", "T": "2"},
        "T": {"G": "0", "C": "1", "A": "2"},
    }

    __DNA2TRIT = {"A": 0, "C": 1, "G": 2, "T": 3}
    __TRIT2DNA = {0: "A", 1: "C", 2: "G", 3: "T"}

    @classmethod
    def encode(cls, input_string, encrypt=False, key_file=None, verbose=False):
        """
        Encodes an input string to DNA sequence

        :return: encoded dna sequences
        :rtype: list[str]
        """
        huff_string = cls.__encode_string2huffman(input_string, verbose=verbose)
        concatenated_trits = cls.__pad_trits(huff_string, verbose=verbose)
        dna_string = cls.__convert_trits_2dna(concatenated_trits, verbose=verbose)
        segments = cls.__create_segments(dna_string, verbose=verbose)
        random_segs = []
        if encrypt:
            assert key_file, "Key file missing! Please provide a key."

            key_streams = cls.__import_key(key_file=key_file)
            random_segs = cls.__randomize_segments(
                segments, mode="encrypt", key_streams=key_streams, verbose=verbose
            )
        else:
            random_segs = cls.__randomize_segments(
                segments, mode=None, key_streams=None, verbose=verbose
            )
        indexed_segments = cls.__create_indexed_segments(random_segs, verbose=verbose)
        directed_segments = cls.__add_orientation_bases(
            indexed_segments, verbose=verbose
        )
        if verbose:
            for index, segment in enumerate(directed_segments):
                print(f"Encoded DNA segment %{index}: %{segment}")
        return directed_segments

    @classmethod
    def decode(cls, input_dna, decrypt=False, key_file=None, verbose=False):
        """
        Decodes a DNA sequence to input string

        return: decoded string
        rtype: str
        """
        assert isinstance(input_dna, str) or isinstance(
            input_dna, list
        ), "Input needs to be either a DNA sequence or a list of DNA sequences!"
        remove_orientation = True
        if isinstance(input_dna, str):
            input_dna = cls.__create_segments(input_dna, verbose=verbose)
            remove_orientation = False
        if remove_orientation:
            input_dna = cls.__remove_orientation(input_dna, verbose=verbose)
        extracted_segs = cls.__extract_segments(input_dna, verbose=verbose)
        decrypted_segs = []
        if decrypt:
            assert key_file, "Key file missing! Please provide a key."

            key_streams = cls.__import_key(key_file=key_file)
            decrypted_segs = cls.__randomize_segments(
                extracted_segs, mode="decrypt", key_streams=key_streams, verbose=verbose
            )
        else:
            decrypted_segs = cls.__randomize_segments(
                extracted_segs, mode=None, key_streams=None, verbose=verbose
            )
        assembled_seq = cls.__assemble_segments(decrypted_segs, verbose=verbose)
        decoded = cls.__decode_dna_string(assembled_seq, verbose=verbose)
        if verbose:
            print("Decoded string:", decoded)
        return decoded

    @classmethod
    def generate_key(cls, key_file="dna.key", bits=512, verbose=False):
        """
        Generates a key to encrypt DNA and writes key to file

        Keyword Arguments:
            file -- file name of key file_ (default: {"dna.key"})
            bits -- nr of bits per base (will be multiplied by 4) (default: {512})
            verbose -- ptint verbose output (default: {False})
        """
        digit = string.digits
        key = "".join([(secrets.choice(digit)) for _ in range(bits * 4)])
        wrapped = textwrap.fill(key, width=80)

        with open(key_file, "w", encoding="utf-8") as fout:
            fout.write("-----START DNA PRIVATE KEY-----\n")
            fout.write(wrapped)
            fout.write("\n-----END DNA PRIVATE KEY-----")

        if verbose:
            print("key:", key)

    @classmethod
    def __import_key(cls, key_file="dna.key", verbose=False):
        """
        Imports a DNA key file

        Keyword Arguments:
            file -- input file name_ (default: {"dna.key"})
            verbose -- _print verbose output_ (default: {False})

        Returns:
            _description_
        """
        key_string = ""
        with open(key_file, "r", encoding="utf-8") as fin:
            key_string = "".join(
                [
                    line.replace("\n", "") if not line.startswith("-----") else ""
                    for line in fin
                ]
            )

        l = len(key_string) // 4
        key_streams = [key_string[i : i + l] for i in range(0, len(key_string), l)]

        if verbose:
            print("key_streams:", key_streams)

        return key_streams

    @classmethod
    def __encode_string2huffman(cls, s_0, verbose=False):
        """
        Converts a string to bytes and then encodes bytes with huffman code

        return: string with huffman code
        rtype: str
        """
        arr = bytearray(s_0, encoding="utf8")
        s_1 = "".join([cls.__HUFFMAN_DICT[arr[i]] for i in range(len(arr))])
        if verbose:
            print("s_0:", s_0)
            print("s_1:", s_1)
        return s_1

    @classmethod
    def __convert2base3(cls, number):
        """
        Converts number to base 3

        return: base 3 representation
        rtype: str
        """
        if number == 0:
            return "0"
        digits = []
        while number:
            number, remainder = divmod(number, 3)
            digits.append(str(remainder))
        return "".join(reversed(digits))

    @classmethod
    def __encode_string_length2trits(cls, s_1, verbose=False):
        """
        Gets length of input string, converts to base 3 representation
        and encodes into trits

        return: trit for length input sequence
        rtype: str
        """
        length_base3 = cls.__convert2base3(len(s_1))
        prefix = "0" * (25 - len(length_base3))
        s_2 = prefix + length_base3
        if verbose:
            print("s_2:", s_2)
        return s_2

    @classmethod
    def __pad_trits(cls, s_1, verbose=False):
        """
        Gets the length of input string and converts to trits.
        Prepend those trits to input string and append padding trits
        to make sure final string is a multiple of 25

        return: padded sequence with trits
        rtype: str
        """
        s_2 = cls.__encode_string_length2trits(s_1)
        s_3 = "0" * (25 - (len(s_2 + s_1) % 25))
        s_4 = s_2 + s_1 + s_3
        if verbose:
            print("s_3:", s_3)
            print("s_4:", s_4)
        return s_4

    @classmethod
    def __convert_trits_2dna(cls, s_4, verbose=False):
        """
        Converts trits to DNA

        return: DNA sequence
        rtype: str
        """
        prev_nt = "A"
        s_5 = ""
        for i, _ in enumerate(s_4):
            current_nt = cls.__TRIT2DNA_MATRIX[s_4[i]][prev_nt]
            prev_nt = current_nt
            s_5 += current_nt
        if verbose:
            print("s_5:", s_5)
        return s_5

    @classmethod
    def __reverse_complement(cls, dna_string):
        """
        Returns reverse complement of DNA string

        return: reverse complement
        rtype: str
        """
        complementary_dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
        return "".join(
            complementary_dict.get(base, base) for base in reversed(dna_string)
        )

    @classmethod
    def __create_segments(cls, s_5, verbose=False):
        """
        Splits string into overlapping segments.
        Also reverse complements the segments with odd indexes

        return: list of overlapping segments
        rtype: list[str]
        """
        sequences = []
        for i in range(int(len(s_5) / 25) - 3):
            if i % 2 == 0:
                sequences.append(s_5[25 * i : 25 * i + 100])
            else:
                sequences.append(cls.__reverse_complement(s_5[25 * i : 25 * i + 100]))
        if verbose:
            for index, seq in enumerate(sequences):
                print(f"F{index}: {seq}")
        return sequences

    @classmethod
    def __randomize_segments(cls, segment_list, mode, key_streams, verbose=False):
        """
        Randomizes segments using keystreams

        return: encrypted/decrypted sequence
        rtype: str
        """
        assert mode in [
            None,
            "encrypt",
            "decrypt",
        ], "mode parameter needs to be either 'encrypt' or 'decrypt' or None"
        if mode is None:
            if verbose:
                for index, segment in enumerate(segment_list):
                    print(f"F{index}_random: {segment}")
            return segment_list
        randomized_segments = []
        for index, segment in enumerate(segment_list):
            digits = [cls.__DNA2TRIT[x] for x in segment]
            base4_differences = [(y - x) % 4 for x, y in zip(digits[:-1], digits[1:])]
            base3_trits = [(x - 1) % 3 for x in base4_differences]
            combined = []
            if mode == "encrypt":
                combined = list(
                    map(
                        add,
                        base3_trits,
                        [int(x) for x in key_streams[index % 4]],
                    )
                )
            elif mode == "decrypt":
                combined = list(
                    map(
                        sub,
                        base3_trits,
                        [int(x) for x in key_streams[index % 4]],
                    )
                )
            combined = [(x % 3) + 1 for x in combined]
            combined = [x % 4 for x in accumulate([digits[0]] + combined)]
            randomized = "".join([cls.__TRIT2DNA[x] for x in combined])
            randomized_segments.append(randomized)
        if verbose:
            if mode == "encrypt":
                for index, segment in enumerate(randomized_segments):
                    print(f"F{index}_encrypted: {segment}")
            elif mode == "decrypt":
                for index, segment in enumerate(randomized_segments):
                    print(f"F{index}_decrypted: {segment}")
        return randomized_segments

    @classmethod
    def __create_indexed_segments(cls, segment_list, file_id_trit="12", verbose=False):
        """
        Appends indexing information to segments

        return: return segments with indexing adapters
        rtype: list[str]
        """
        for index, _ in enumerate(segment_list):
            i_base3 = cls.__convert2base3(index)
            i_3 = "0" * (12 - len(i_base3)) + i_base3
            parity_trit = (int(file_id_trit[0]) + sum([int(i) for i in i_3[0::2]])) % 3
            idx = file_id_trit + i_3 + str(parity_trit)
            prev_nt = segment_list[index][-1]
            ix_nt = ""
            for i, _ in enumerate(idx):
                current_nt = cls.__TRIT2DNA_MATRIX[idx[i]][prev_nt]
                prev_nt = current_nt
                ix_nt += current_nt
            segment_list[index] += ix_nt
        if verbose:
            for index, segment in enumerate(segment_list):
                print(f"F{index}' (indexed): {segment}")
        return segment_list

    @classmethod
    def __add_orientation_bases(cls, segment_list, verbose=False):
        """
        Adds flanking bases to determine orientation of sequence

        return: sequence with added orientation bases
        rtype: str
        """
        for index, segment in enumerate(segment_list):
            nt_prepend = ""
            if segment[0] == "A":
                nt_prepend = "T"
            elif segment[0] == "T":
                nt_prepend = "A"
            else:
                nt_prepend = ["A", "T"][randint(0, 1)]
            nt_append = ""
            if segment[-1] == "C":
                nt_append = "G"
            elif segment[-1] == "G":
                nt_append = "C"
            else:
                nt_append = ["C", "G"][randint(0, 1)]
            segment_list[index] = nt_prepend + segment_list[index] + nt_append
        if verbose:
            for index, segment in enumerate(segment_list):
                print(f"F{index}' (oriented): {segment}")
        return segment_list

    @classmethod
    def __remove_orientation(cls, segment_list, verbose=False):
        """
        Removes the bases used to determine direction of sequence

        return: sequence with orientation bases removed
        rtype: str
        """
        for index, segment in enumerate(segment_list):
            if (segment[0] == "A" or segment[0] == "T") and (
                segment[-1] == "C" or segment[-1] == "G"
            ):
                segment_list[index] = segment[1:-1]
            elif (segment[0] == "C" or segment[0] == "G") and (
                segment[-1] == "A" or segment[-1] == "T"
            ):
                segment = cls.__reverse_complement(segment)
                segment_list[index] = segment[1:-1]
            else:
                raise ValueError(
                    f"Could not determine orientation of DNA sequence {segment}!"
                )
        if verbose:
            for index, segment in enumerate(segment_list):
                print(f"Reoriented {index}: {segment}")
        return segment_list

    @classmethod
    def __convert_dna2trits(cls, s_4, start_nt="A", verbose=False):
        """
        Converts DNA to trits

        return: sequence of trits
        rtype: str
        """
        prev_nt = start_nt
        s_5 = ""
        for i, _ in enumerate(s_4):
            current_nt = cls.__DNA2TRIT_MATRIX[s_4[i]][prev_nt]
            prev_nt = current_nt
            prev_nt = s_4[i]
            s_5 += current_nt
        if verbose:
            print("s_5:", s_5)
        return s_5

    @classmethod
    def __extract_segments(cls, segment_list, verbose=False):
        """
        Extracts the encoded segments

        return: sorted segments without indexing adapters
        rtype: list[str]
        """
        segment_tuples = []
        for segment in segment_list:
            read = segment[0:100]
            indexing_dna = segment[100:]
            indexing_trits = cls.__convert_dna2trits(
                "".join(indexing_dna), start_nt=read[-1]
            )
            i_3 = "".join(indexing_trits[2:14])
            i = i_3.lstrip("0") or "0"
            segment_tuples.append((read, int(i)))
        if verbose:
            for tup in segment_tuples:
                print(f"Sequence {tup[1]}: {tup[0]}")
        return [x[0] for x in sorted(segment_tuples, key=itemgetter(1))]

    @classmethod
    def __assemble_segments(cls, segment_list, overlap=25, verbose=False):
        """
        Assembles (and reverse complements odd) segments

        return: assembled sequence from segments
        rtype: str
        """
        assembled = segment_list[0][0 : (100 - overlap)]
        for index, segment in enumerate(segment_list):
            if index % 2 != 0:
                segment = cls.__reverse_complement(segment)
            assembled = assembled + segment[-overlap:]
        if verbose:
            print("Assembled sequence:", assembled)
        return assembled

    @classmethod
    def __decode_dna_string(cls, dna_string, verbose=False):
        """
        Decodes DNA into original representation via huffman code

        return: decoded sequence
        rtype: str
        """
        trits = cls.__convert_dna2trits(dna_string)
        length = int(trits[:25].lstrip("0"), 3)
        inverted_huffman = dict([v, k] for k, v in cls.__HUFFMAN_DICT.items())
        index = 0
        byte_array = []
        while index < len(trits[25 : (25 + length)]):
            trit = trits[25 + index : 25 + index + 5]
            if trit in inverted_huffman.keys():
                byte_array.append(int(inverted_huffman[trit]))
                index += 5
            elif trits[25 + index : 25 + index + 6] in inverted_huffman.keys():
                trit = trits[25 + index : 25 + index + 6]
                byte_array.append(int(inverted_huffman[trit]))
                index += 6
        if verbose:
            print("Decoded:", "".join(map(chr, byte_array)))
        return "".join(map(chr, byte_array))


if __name__ == "__main__":
    INPUT = """
ON THE ORIGIN OF SPECIES by Charles Darwin

When on board H.M.S. "Beagle," as naturalist, I was much struck with
certain facts in the distribution of the inhabitants of South America,
and in the geological relations of the present to the past inhabitants
of that continent. These facts seemed to me to throw some light on the
origin of species—that mystery of mysteries, as it has been called by
one of our greatest philosophers. On my return home, it occurred to me,
in 1837, that something might perhaps be made out on this question by
patiently accumulating and reflecting on all sorts of facts which could
possibly have any bearing on it. After five years’ work I allowed
myself to speculate on the subject, and drew up some short notes; these
I enlarged in 1844 into a sketch of the conclusions, which then seemed
to me probable: from that period to the present day I have steadily
pursued the same object. I hope that I may be excused for entering on
these personal details, as I give them to show that I have not been
hasty in coming to a decision.
"""
    ENCODED = DNAStore().encode(INPUT, encrypt=False, key_file="dna.key", verbose=False)
    print("Encoded:", ENCODED)
    DECODED = DNAStore().decode(
        ENCODED, decrypt=False, key_file="dna.key", verbose=False
    )
    print("Decoded:", DECODED)

    # DNAStore().generate_key(verbose=True)
    # DNAStore().import_key(verbose=True)
