import matplotlib.pyplot as plt


def draw_step_graph(binary_string):
    # Convert binary string to a list of integers
    binary_list = [int(x) for x in binary_string]

    # Set up the plot
    fig, ax = plt.subplots(figsize=(20, 1))
    ax.set_ylim([-0.1, 2.8])
    ax.set_xlim([-1, len(binary_list)])
    ax.set_xticks(range(len(binary_list)))
    ax.set_yticks([0, 1])
    ax.grid(True, axis='both', linestyle='--', linewidth=0.5)

    # Draw the step graph
    x = range(len(binary_list))
    y = [0] + binary_list[:-1]
    plt.step(x, binary_list, where='post', color='black')
    plt.step(x, y, where='pre', color='black')

    # Show the plot
    plt.show()


def to_hex(binary_string):
    res = ''
    for i in range(0, int(len(binary_string) / 4)):
        number = binary_string[(4 * i):]
        number = number[:4]
        res += hex(int(number, 2))[2:]
    res = res.upper()
    return res


def check_middle(binary_string):
    res = [0] * 100
    counter = 0
    previous = ''
    for i in binary_string:
        if i == previous:
            counter += 1
        else:
            res[counter] += 1 * (counter + 1)
            previous = i
            counter = 0
    return res


def manchester(input_bin):
    res = ''
    for i in input_bin:
        if i == '1':
            res += '10'
        else:
            res += '01'
    return res


def nrz(input_bin):
    res = ''
    for i in input_bin:
        res += i + i
    return res


def rz(input_bin):
    res = ''
    prev = -1
    count_half_c = 0
    for i in input_bin:
        if i == '1':
            if prev == 0:
                count_half_c += 1
            prev = 1
            res += '21'
        else:
            if prev == 1:
                count_half_c += 1
            prev = 0
            res += '01'
    print(len(input_bin))
    print(count_half_c)
    return res


def ami(input_bin):
    res = ''
    prev = 0
    max_count_zeroes_siq = [0] * 10
    count_zeroes = 0
    for i in input_bin:
        if i == '1':
            # if count_zeroes > max_count_zeroes_siq[]:
            #     max_count_zeroes_siq = count_zeroes
            max_count_zeroes_siq[count_zeroes] += 1
            count_zeroes = 0
            if prev == 0:
                res += '2'
                prev = 1
            else:
                res += '0'
                prev = 0
        else:
            res += '1'
            count_zeroes += 1
    print(max_count_zeroes_siq)
    return res


def nrzi(input_bin):
    res = ''
    prev = '0'
    for i in input_bin:
        if i == '1':
            if prev == '0':
                res += '1'
                prev = '1'
            else:
                res += '0'
                prev = '0'
        else:
            res += prev
    return res


encoding_table = {
    '0000': '11110',
    '0001': '01001',
    '0010': '10100',
    '0011': '10101',
    '0100': '01010',
    '0101': '01011',
    '0110': '01110',
    '0111': '01111',
    '1000': '10010',
    '1001': '10011',
    '1010': '10110',
    '1011': '10111',
    '1100': '11010',
    '1101': '11011',
    '1110': '11100',
    '1111': '11101'
}


def extra_4b_5b(input_bin):
    res = ''
    for i in range(0, int(len(input_bin) / 4)):
        number = input_bin[4 * i:]
        number = number[:4]
        res += encoding_table[number]
    return res


def scramble_binary_string(binary_string):
    """
    Scrambles a binary string using an addition algorithm modulo two.

    Args:
    binary_string (str): The binary string to be scrambled.

    Returns:
    str: The scrambled binary string.
    """

    # Convert binary string to list of integers
    binary_list = [int(bit) for bit in binary_string]

    # Initialize variables
    n = len(binary_list)
    scrambled_list = [0] * n

    # Scramble the binary string using addition algorithm modulo two
    for i in range(n):
        scrambled_list[i] = binary_list[i] ^ scrambled_list[(i-3) % n] ^ scrambled_list[(i-5) % n]

    # Convert list of integers back to binary string
    scrambled_string = ''.join(str(bit) for bit in scrambled_list)

    return scrambled_string


input_bin_data = '1100101011110011111100011111001011100000111100001110010111100010001000001100100000101110001000001100111100101110'
# input_bin_data = input_bin_data[:16]
input_bin_data = scramble_binary_string(input_bin_data)
print(input_bin_data)
print(to_hex(input_bin_data))
res = ami(input_bin_data)

print(res)
draw_step_graph(res[:32])

hex_res = to_hex(res)
print(hex_res)

middle_arr = check_middle(res)
for counter, value in enumerate(middle_arr):
    print(value, end=' ')
