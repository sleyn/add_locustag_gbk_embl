# Add locus tags to the GenBank or EMBL files

One of the main reasons to create this script is to supplement files annotated with RASTtk pipeline from the [PATRIC](https://www.patricbrc.org/) web service with locus tags as they are absent from the standard output.

The locus tags are required for EMBL annotated assembly submisson and for work of some packages.

## Requirements

The only requirement is [BioPython](https://biopython.org/wiki/Download).

## Input

The script accepts files in GenBank and EMBL formats. Details are in the "[The DDBJ/ENA/GenBank Feature Table Definition](https://www.ddbj.nig.ac.jp/ddbj/feature-table-e.html)" document.

## Output

Output is the same GenBank or EMBL file with added `/locus_tag` fields to the feature keys that require locus tags.
Feature keys that require locus tags are specified according to the "[The DDBJ/ENA/GenBank Feature Table Definition](https://www.ddbj.nig.ac.jp/ddbj/feature-table-e.html)", 7.2 Appendix II: Feature keys reference.

The locus tag is formed by prefix and number with fixed number of positions. For numbers that has less positions than specified in `--len_num` argument leading zeroes will be added.

For example with `--prefix BA --len_num 4` the locus tags will be: `BA_0001, BA_0002, ..., BA_0748, ..., BA_3984`.   

## Usage

```
usage: add_lt.py [-h] [-f FILE] [-n IN_TYPE] [-u OUT_TYPE] [-o OUT] [-p PREFIX] [-l LEN_NUM]

Adds locus_tag field to the GBK or EMBL files.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to the input file.
  -n IN_TYPE, --in_type IN_TYPE
                        Input file type. Values: "gb" (Default) or "embl".
  -u OUT_TYPE, --out_type OUT_TYPE
                        Input file type. Values: "gb" (Default) or "embl".
  -o OUT, --out OUT     Path to the output file.
  -p PREFIX, --prefix PREFIX
                        Locus_tag prefix.
  -l LEN_NUM, --len_num LEN_NUM
                        Length of the numeric part of the locus tag. Default: 5
```

Example:

```
python3 add_lt.py -f Input.gbk --in_type gb --out_type gb -o Output.gbk -p BACT -l 5 
```

The locus tags would be:
BACT_00001
BACT_00002
BACT_00003
...