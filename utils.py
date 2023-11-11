# Return x and y in binary form with same number of bits
def equal_length_binary(x, y):
    bin_x = bin(x)[2:]
    bin_y = bin(y)[2:]
    max_length = max(len(bin_x), len(bin_y))
    bin_x = bin_x.zfill(max_length)
    bin_y = bin_y.zfill(max_length)
    return bin_x, bin_y, max_length