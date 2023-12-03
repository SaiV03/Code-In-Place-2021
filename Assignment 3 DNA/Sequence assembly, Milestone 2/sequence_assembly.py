"""
File: sequence_assembly.py
--------------
ADD YOUR DESCRIPTION HERE
"""
import os
import sys

from TextGrid import TextGrid

SEQUENCES_FOLDER = 'large'

def assemble_sequence(s1,s2,s3):
    """
    Given three TextGrid objects, this function creates and returns a solution genome based on the sequences passed in. All the sequences passed in will be the same size.

    Input:
        three TextGrids to be processed
    Returns:
        a new solution genome (also a TextGrid)
    """
    # Delete the pass statement below and write your code here!
    assemble=TextGrid.blank(s1.width,s1.height)
    for y in range(s1.height):
        for x in range(s1.width):
            best_cell=get_best_nucleotide(s1.get_cell(x,y),s2.get_cell(x,y),s3.get_cell(x,y))
            assemble.set_cell(x,y,best_cell)
    return assemble

def get_best_nucleotide(n1,n2,n3):
    """
    Given three nucleotides, returns a nucleotide with the most common *non-blank* value. If multiple nucleotides have the same value, it doesn't matter which specific nucleotide is returned so long as its value is correct. You can assume there will never be ambiguity -- there will always be a clear majority non-blank character.

    Input:
        three nucleotides (Cells) to be compared
    Returns:
        best (Cell): nucleotide with most common non-blank value

    This doctest creates nucleotides for simple tests.
    >>> grid = TextGrid('ATCG_.txt')
    >>> A = grid.get_cell(0,0)
    >>> T = grid.get_cell(1,0)
    >>> C = grid.get_cell(2,0)
    >>> G = grid.get_cell(3,0)
    >>> blank = grid.get_cell(4,0)
    >>> best1 = get_best_nucleotide(A, A, A)
    >>> best1.value
    'A'
    >>> best2 = get_best_nucleotide(A, T, T)
    >>> best2.value
    'T'
    >>> best3 = get_best_nucleotide(A, blank, A)
    >>> best3.value
    'A'
    >>> best4 = get_best_nucleotide(blank, blank, T)
    >>> best4.value
    'T'
    """
    # Replace the pass statement below with your code from the previous milestone!
    nucld=[n1.value,n2.value,n3.value]
    while '_' in nucld:
        nucld.remove('_')
    if len(nucld)<3:
        val = nucld[0]
    else:
        if nucld[0]==nucld[1]:
            val = nucld[0]
        else:
            val = nucld[2]
    if n1.value==val:
        return n1
    if n2.value==val:
        return n2
    return n3


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########


def txts_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a directory, returns a list of the .txt filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filenames.append(os.path.join(directory, filename))
    return filenames


def load_sequences(directory):
    """
    DO NOT MODIFY
    Given a directory name, reads all the .txt files within it into memory and
    returns them in a list. Prints to terminal the names of the files it loads.

    Input:
        dir (string): name of directory
    Returns:
        sequences (List[TextGrids]): list of sequences in directory
    """
    sequences = []
    txts = txts_in_dir(directory)
    txts.sort()
    for filename in txts:
        print("Loading", filename)
        sequence = TextGrid(filename)
        sequences.append(sequence)
    return sequences


def main():
    # DO NOT MODIFY
    sequences = load_sequences(SEQUENCES_FOLDER)
    # print(sequences[0], sequences[1], sequences[2])
    full_genome = assemble_sequence(sequences[0], sequences[1], sequences[2])
    if full_genome:
        print("Genome assembled as follows:")
        print(full_genome)
    else:
        print("No genome to display!")

if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) > 0:
        SEQUENCES_FOLDER = args[0]
    main()
