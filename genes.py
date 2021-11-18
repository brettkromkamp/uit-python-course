"""
Introductory Python Course 2021 - UiT
By Brett Alistair Kromkamp (brettkromkamp@gmail.com - https://brettkromkamp.com)



Biologists use a sequence of the letters A, C, T, and G to model a genome.

A gene is a substring of a genome that starts after a triplet ATG and ends before a triplet TAG, TAA, or TGA.
Furthermore, the length of a gene string is a multiple of 3, and the gene does not contain any of the triplets ATG, TAG, TAA, or TGA.

Here are the sample runs:

<output>
Enter a genome string: TTATGTTTTAAGGATGGGGCGTTAGTT
TTT
GGGCGT
<end output>

<output>
Enter a genome string: TGTGTGTATAT
No gene is found
<end output>
"""

NOT_FOUND = -1


def find_genes(genome, genes=None):
    if genes is None:
        genes = []
    if len(genome) >= 9:
        start_index = genome.find("ATG")
        if start_index != NOT_FOUND:
            processed_genome = genome[start_index + 3 :]
            end_indexes = [
                processed_genome.find("TAG"),
                processed_genome.find("TAA"),
                processed_genome.find("TGA"),
            ]
            end_indexes = [index for index in end_indexes if index > 0]
            if len(end_indexes):
                end_index = min(end_indexes)
                candidate = processed_genome[:end_index]
                if is_gene(candidate):
                    genes.append(candidate)  # Candidate has been confirmed to be a gene
                find_genes(processed_genome[end_index:], genes)  # Recursive call!
    return genes


def is_gene(candidate):
    # Check if the gene candidate string is a multiple of 3. If it isn't then it is not a gene.
    if len(candidate) % 3 != 0:
        return False
    # Confirm that the gene candidate does not contain one of the markers. If it does then it is not a gene.
    for triplet in ["ATG", "TAG", "TAA", "TGA"]:
        if triplet in candidate:
            return False
    return True


if __name__ == "__main__":
    # genome = input("Enter a genome string: ")
    genome = "atgaaaaaagcaaaattattcggttttagtttgattgcattaggtttatcagtttcacttgcagcatgtggtggtggcaaaggcaaaaccgctgaaagcggcggtggcaaaggggatgcagcgcatagtgctgtaatcattacagatacaggcggcgtggatgacaagtcgttcaaccaatcttcttgggaaggattgcaagcttggggtaaagaacatgatttaccagaaggttcaaaagggtatgcatatattcaatcgaatgatgcagctgactatacaaccaatattgaccaagcggtatcaagtaaattcaacacaatctttggtattggctacttgctaaaagatgcaatttcttctgcagcagatgccaaccctgatacaaactttgttttaatcgatgatcaaatcgatggcaaaaagaatgtcgtttctgcaacatttagagataatgaagcagcttacttagccggtgttgctgctgcaaatgaaacaaaaacgaacaaagtcggttttgttggtggtgaagaaggggtcgtaattgaccgtttccaagctggttttgaaaaaggtgtggctgatgctgcgaaagaattaggtaaagaaattactgttgatacgaaatatgcggcttcatttgctgatcctgccaaagggaaagctttagctgctgcaatgtaccaaaacggcgttgatatcatcttccatgcttctggtgcgactggacaaggggtcttccaagaagcaaaagacttgaatgaatcaggttctggcgacaaagtttgggtaatcggcgttgaccgcgatcaagatgctgatggcaagtacaaaacaaaagacggcaaagaagacaacttcacgttaacttcaacgcttaaaggtgtcggcacagcggttcaagatattgccaaccgtgcgttagaagacaaattccctggtggcgaacatttagtttatggattaaaagatggtggcgttgacttaacagacggctatttaaacgacaaaacaaaagaagctgttaaaacagcaaaagataaagtaatctcaggtgacgtaaaagtcccagaaaaaccagaataa"
    genes = find_genes(genome.upper())
    if genes:
        print(f"The following genes were found ({len(genes)} in total): ")
        for gene in genes:
            print(gene)
    else:
        print("No genes were found!")
