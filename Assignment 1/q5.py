intensities =       [0, 1, 2, 3, 4, 5, 6, 7]
intensity_count =   [0, 2, 5, 3, 3, 1, 0, 1]
pdf =               [0, 0.13, 0.33, 0.2, 0.2, 0.07, 0, 0.07] # Probability Density Function
cdf =               [0, 0.13, 0.46, 0.66, 0.86, 0.93, 0.93, 1] # Cumulative Distribution Function
new_intensities =   [0, 0, 3, 4, 6, 6, 6, 7] # Round down any resulting pixel intensities that are not integers (use the floor operator)

M_equalized =     [[7, 3, 6, 6, 6],
                [4, 4, 0, 3, 3],
                [4, 6, 0, 3, 3]]