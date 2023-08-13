from random import sample, choice

network_masks = [
    "0.0.0.0",          # /0
    "128.0.0.0",        # /1
    "192.0.0.0",        # /2
    "224.0.0.0",        # /3
    "240.0.0.0",        # /4
    "248.0.0.0",        # /5
    "252.0.0.0",        # /6
    "254.0.0.0",        # /7
    "255.0.0.0",        # /8
    "255.128.0.0",      # /9
    "255.192.0.0",      # /10
    "255.224.0.0",      # /11
    "255.240.0.0",      # /12
    "255.248.0.0",      # /13
    "255.252.0.0",      # /14
    "255.254.0.0",      # /15
    "255.255.0.0",      # /16
    "255.255.128.0",    # /17
    "255.255.192.0",    # /18
    "255.255.224.0",    # /19
    "255.255.240.0",    # /20
    "255.255.248.0",    # /21
    "255.255.252.0",    # /22
    "255.255.254.0",    # /23
    "255.255.255.0",    # /24
    "255.255.255.128",  # /25
    "255.255.255.192",  # /26
    "255.255.255.224",  # /27
    "255.255.255.240",  # /28
    "255.255.255.248",  # /29
    "255.255.255.252",  # /30
    "255.255.255.254",  # /31
    "255.255.255.255"   # /32
]


def ip_calculator(ip, mask):
    def toBin(num):
        if num.isdigit():
            if 0 <= int(num) <= 255:
                def addZeros(res):
                    return ((8 - len(res)) * '0' + res) if len(res) < 8 else res
                def toBIN(num):
                    return '' if int(num) == 0 else (str(int(num) % 2) + toBIN(int(num) // 2))
                return addZeros(toBIN(num)[::-1])
        return num + " Octet is not valid"

    def toBinIP(ip):
        ipArr = ip.split('.')
        binIp = ''
        for i in ipArr:
            binIp += toBin(i) + '.'
        return binIp[:-1]

    def getSlash(binMask):
        return binMask.count('1')

    def toDecimal(binary):
        decimal = 0
        power = 0
        for bit in reversed(binary):
            if bit == '1':
                decimal += 2 ** power
            power += 1
        return decimal

    def toDecimalIp(ip):
        ipList = ip.split('.')
        for i in range(len(ipList)):
            ipList[i] = str(toDecimal(ipList[i]))
        return '.'.join(ipList)
        

    def add_periods(binary_string, period_interval):
        return '.'.join([binary_string[i:i+period_interval] for i in range(0, len(binary_string), period_interval)])

    slash = 0
    if len(mask) <= 2:
        if mask == '':
            slash = 0
        elif mask.isdigit():
            slash = int(mask)
        binMask = 0
    else:
        binMask = toBinIP(mask)
        slash = getSlash(binMask)
    binIp = toBinIP(ip)
    broadcast = add_periods((binIp.replace('.','')[:slash] + (32 - slash) * '1'), 8)
    network = add_periods((binIp.replace('.','')[:slash] + (32 - slash) * '0'), 8)
    minHost = network[:-1] + '1'
    maxHost = broadcast[:-1] + '0'

    print('--------------------------------------------------------------')
    print('     IP            -',ip)
    print('     Binary   Ip   -',binIp)
    print('     Network Mask  -',mask)
    print('     Binary Mask   -',binMask)
    print('     Slash         -',slash)
    print('     Binary Ip /   -',f"{binIp}/{slash}")
    print('     Broadcast bin -',broadcast)
    print('     Broadcast     -',toDecimalIp(broadcast))
    print('     Network   bin -',network)
    print('     Network       -',toDecimalIp(network))
    print('     Min Host  bin -',minHost)
    print('     Min Host      -',toDecimalIp(minHost))
    print('     Max Host  bin -',maxHost)
    print('     Max Host      -',toDecimalIp(maxHost))
    print('     IP     Count  -',2 ** (32 - slash),f"(2^{32-slash})")
    print('     Host   Count  -',2 ** (32 - slash) - 2, f"(2^{32-slash}) - 2")
    print('--------------------------------------------------------------\n')



for i in range(25):
    ip = '.'.join(map(str, sample(range(0, 256), 4)))
    mask = choice(network_masks)
    ip_calculator(ip, mask)
