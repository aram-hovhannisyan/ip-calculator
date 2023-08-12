def add_periods(binary_string, period_interval):
    return '.'.join([binary_string[i:i+period_interval] for i in range(0, len(binary_string), period_interval)])

# Assuming you have calculated the 'network' binary string as described
network_binary = "11011000101110101011110000111010"

# Adding periods after every 8th element
network_with_periods = add_periods(network_binary, 8)

print(network_with_periods)
