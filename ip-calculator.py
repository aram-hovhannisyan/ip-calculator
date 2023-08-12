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


ip = input('Enter IP address: ')
mask = input('Enter subnet mask or slash(/): ')
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

print('--------------------------------------------------')
print('Binary   Ip   -',binIp)
print('Binary Mask   -',binMask)
print('Slash         -',slash)
print('Binary Ip /   -',f"{binIp}/{slash}")
print('Broadcast bin -',broadcast)
print('Broadcast     -',toDecimalIp(broadcast))
print('Network bin   -',network)
print('Network       -',toDecimalIp(network))
print('Min Host  bin -',minHost)
print('Min Host      -',toDecimalIp(minHost))
print('Max Host  bin -',maxHost)
print('Max Host      -',toDecimalIp(maxHost))
print('IP     Count  -',2 ** (32 - slash),f"(2^{32-slash})")
print('Host   Count  -',2 ** (32 - slash) - 2, f"(2^{32-slash}) - 2")
print('--------------------------------------------------')