from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description='Adds locus_tag field to the GBK or EMBL files.')
parser.add_argument('-f', '--file', help='Path to the input file.')
parser.add_argument('-n', '--in_type', default='gb', help='Input file type. Values: "gb" (Default) or "embl".')
parser.add_argument('-u', '--out_type', default='gb', help='Input file type. Values: "gb" (Default) or "embl".')
parser.add_argument('-o', '--out', help='Path to the output file.')
parser.add_argument('-p', '--prefix', help='Locus_tag prefix.')
parser.add_argument('-l', '--len_num', default=5, help='Length of the numeric part of the locus tag. Default: 5')
args = parser.parse_args()

if args.file == '':
    exit('No input was given. Set "--file" argument.')

if args.out == '':
    exit('The output file path is required. Set "--out" argument.')

# Define features that require locus tag
# Based on The DDBJ/ENA/GenBank Feature Table Definition
# Version 11.1 October 2021
lt_features = (
    'C_region',
    'CDS',
    'D-loop',
    'D_segment',
    'exon',
    'gene',
    'iDNA',
    'intron',
    'J_segment',
    'mat_peptide',
    'misc_binding',
    'misc_difference',
    'misc_feature',
    'misc_recomb',
    'misc_RNA',
    'misc_structure',
    'mobile_element',
    'modified_base',
    'mRNA',
    'ncRNA',
    'N_region',
    'old_sequence',
    'oriT',
    'polyA_site',
    'precursor_RNA',
    'prim_transcript',
    'primer_bind',
    'propeptide',
    'protein_bind',
    'regulatory',
    'repeat_region',
    'rep_origin',
    'rRNA',
    'S_region',
    'sig_peptide',
    'stem_loop',
    'STS',
    'tmRNA',
    'transit_peptide',
    'tRNA',
    'unsure',
    'V_region',
    'V_segment',
    'variation',
    '3\'UTR',
    '5\'UTR'
)

# Initialize locus tag index
lt_index = 1

with open(args.out, 'w') as out_file:
    with open(args.file, 'r') as in_file:
        # For each contig
        for record in SeqIO.parse(args.file, args.in_type):
            # Add locus tag to features
            for feature in record.features:

                if feature.type in lt_features:
                    feature.qualifiers['locus_tag'] = args.prefix + '_' + str(lt_index).zfill(int(args.len_num))
                    lt_index += 1

            SeqIO.write(record, out_file, args.out_type)
