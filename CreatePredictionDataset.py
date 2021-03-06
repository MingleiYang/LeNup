#!/usr/bin/env python
from optparse import OptionParser

def main():
    usage = 'usage: %prog [options] <seq_file> <output_file>'
    parser = OptionParser(usage)
    (options,args) = parser.parse_args()
    if len(args) != 2:
        parser.error('Must provide fasta file, targets file, and an output prefix')
    else:
        seq_file = args[0]
        output_file = args[1]
        
        
    seq_outfile = seq_file[:-4] + m + '.txt'
    
    seq_file = open(seq_file, 'r')
    line1 = seq_file.readlines()
    len1 = len(line1)
    str1 = [[0 for col in range(147)] for row in range(len1)]
    j = -1
    for line in line1:
        j += 1
        for i in range(147):
            str1[j][i] = line[i : i + 1]


    l = 1
    seq_outfile = open(seq_outfile, 'w')
    for i in range(len1):
        p = i * 147 + 1
        q = (i + 1) * 147
        seq_outfile.write('>chr:')
        seq_outfile.write(str(p))
        seq_outfile.write('-')
        seq_outfile.write(str(q))
        seq_outfile.write('(+)\n')
        l += 1
        for j in range(147):
            if str1[i][j] != 'N':
                seq_outfile.write(str1[i][j])
            else:
                seq_outfile.write('A')
        seq_outfile.write("\n")

    seq_outfile.close()
    
    
    
    seqs = dna_io_test.load_data_1hot(seq_outfile)

    seqs = seqs.reshape((seqs.shape[0],4,1,seqs.shape[1]/4))
    name = output_file
    h5f = h5py.File(name, 'w')
    h5f.create_dataset('test_in', data=seqs)
    h5f.close()

if __name__ == '__main__':
    main()