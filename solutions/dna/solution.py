def count_nucleotides(seq):
    count_dict = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0
    }
    for nt in seq:
        if nt not in count_dict.keys():
            print(f"[ERROR] {nt} not in keys!")
            continue

        count_dict[nt] += 1

    return list(count_dict.values())


if __name__ == "__main__":
    with open("rosalind_dna.txt", mode="r") as handle:
        seq = handle.read()

    print(count_nucleotides(seq))
