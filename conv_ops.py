# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p.

import sys
import math


# Arguements 
# c_in: input channel count
# h_in: input height count
# w_in: input width count
# n_filt: number of filters in the convolution layer
# h_filt: filter height count
# w_filt: filter width count
# s: stride of convolution filters
# p: amount of padding on each of the four input map sides

# Parse script arguments
if len(sys.argv) == 9:
    c_in = int(sys.argv[1])
    h_in = int(sys.argv[2])
    w_in = int(sys.argv[3])
    n_lift = int(sys.argv[4])
    h_lift = int(sys.argv[5])
    w_lift = float(sys.argv[6])
    s = float(sys.argv[7])
    p = float(sys.argv[8])
else:
    print('Usage: python3 conv_ops.py c_in h_in w_in n_lift h_lift w_lift s p')
    exit()


# Height of the output
h_out = [(h_in+2*p-h_lift)/s +1]

# Width of the output
w_out = [(w_in+2*p-w_lift)/s +1]


# Total additions and multiplications
adds = n_lift*h_out*w_out*c_in*h_lift*w_lift

# Total additions and multiplications
muls = n_lift*h_out*w_out*c_in*h_lift*w_lift

# total divisions
divs = n_lift*h_out*w_out

c_out = n_lift

# End your script with the following print statements:
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed