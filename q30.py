#!/usr/bin/env python

import os,sys
import fastq
import time

def qual_stat(qstr):
    """ Modified to calculate average quality score of a sequence """
    q30_sum = 0
    q30_seq = 0
    # q30 = 0
    for q in qstr:
        # qual = ord(q) - 33
        qual = q - 33
        q30_sum += qual
        # if qual >= 30:
        #     q30 += 1
    q30_seq = q30_sum/len(qstr)
    return q30_seq

def stat(filename, output):
    """ Modified to output total sequences and sequences with >=30 avg quality """
    reader = fastq.Reader(filename)
    # q30_count = 0
    # total_count = 0
    seq_count = 0
    q30_seq_count = 0
    while True:
        read = reader.nextRead()
        if read == None:
            break
        # total_count += len(read[3])
        q30_seq = qual_stat(read[3])
        # q30_count += q30
        seq_count += 1
        if q30_seq >= 30:
            q30_seq_count += 1
    filename = str(filename)
    total_seqs = "total sequences: " + str(seq_count)
    q30_seqs = "q30 reads: " + str(q30_seq_count)

    q30_out = open(output, "w")
    q30_out.writelines([filename, "\n", total_seqs, "\n", q30_seqs])
    q30_out.close()


def main():
    if len(sys.argv) < 2:
        print("usage: python q30.py <fastq_file> <output_file>")
        sys.exit(1)
    # stat(sys.argv[1])
    stat(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
