intensities =       [0, 1, 2, 3, 4, 5, 6, 7]
intensity_count =   [0, 2, 5, 3, 3, 1, 0, 1]
pdf =               [0, 0.133, 0.333, 0.2, 0.2, 0.067, 0, 0.067] # Probability Density Function
cdf =               [0, 0.133, 0.466, 0.666, 0.866, 0.933, 0.933, 1] # Cumulative Distribution Function
new_intensities =   [0, 0, 3, 4, 6, 6, 6, 7] # Round down any resulting pixel intensities that are not integers (use the floor operator)

M_equalized =     [[7, 3, 6, 6, 6],
                [4, 4, 0, 3, 3],
                [4, 6, 0, 3, 3]]