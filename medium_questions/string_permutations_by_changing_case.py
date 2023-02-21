def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)
    for i in range(len(str)):
        if str[i].isalpha():
            n = len(permutations)
            for j in range(n):
                chs = list(permutations[j])
                chs[i] = chs[i].swapcase()
                permutations.append(''.join(chs))
    return permutations

if __name__ == "__main__":
    print("String permutaions are: " + str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " + str(find_letter_case_string_permutations("ab7c")))
                