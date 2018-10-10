#things to permutate
permutables = ['A', 'B', 'C']

permutation_logic = [[a, b, c]
            for a in permutables
            for b in permutables
            for c in permutables
            #a single input does not equal another input
            if ( a != b and b != c and a != c )
            ]

print(permutation_logic)
print('Total Permutations Available: ', len(permutation_logic))
