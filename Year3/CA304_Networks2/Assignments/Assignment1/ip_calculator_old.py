# arranged in class, network bits, host bits, start address, end address
# the keys indicate which index the first 0 appears in the prefix
classes = {
    0:["A", 7, 24, "0.0.0.0", "127.255.255.255"],
    1:["B", 14, 16, "128.0.0.0", "191.255.255.255"],
    2:["C", 21, 8, "192.0.0.0", "223.255.255.255"],
    3:["D", "n/a", "n/a", "224.0.0.0", "239.255.255.255"],
    4:["E", "n/a", "n/a", "240.0.0.0", "255.255.255.255"]
}

# converts each octet in ip_addr string to binary and returns list
def to_binary_string(ip_addr):
    byte_split = ip_addr.split(".")
    return ["{0:08b}".format(int(x)) for x in byte_split]

# converts each binary string in ip_addr_list to corresponding decimal value
# arranges them back to decimal dot notation
def to_decimal_dot(ip_addr_list):
    return ".".join([str(int(x, 2)) for x in ip_addr_list])

# ip_addr is IPv4 address (string)
def get_class_stats(ip_addr):
    
    binaryIP = to_binary_string(ip_addr)    # converting ip_addr to binary, stored in a list
    firstOctet = binaryIP[0]    # first octet of ip address (binary string)

    # get info if 0 in first 3 bits of first octet, else it's class D or E
    if "0" in firstOctet[:3]:
        ipPrefixIndex = firstOctet.index("0")   # gets first index that 0 appears in first byte

        ipClass = classes[ipPrefixIndex][0]     # gets corresponding IP Class from "classes" mapping based on ipPrefixIndex

        # calculating the number of networks, hosts, and the first and last address based on current class
        numNetworks = 2 ** classes[ipPrefixIndex][1]
        numHosts = 2 ** classes[ipPrefixIndex][2]
        firstAddress, lastAddress = classes[ipPrefixIndex][3], classes[ipPrefixIndex][4]

    # else if it's class D (checking prefix)
    elif firstOctet[:4] == "1110":
        ipPrefixIndex = 3   # hardcoded first index of zero in the prefix
        ipClass = classes[ipPrefixIndex][0]
        numNetworks, numHosts = classes[ipPrefixIndex][1], classes[ipPrefixIndex][2]
        firstAddress, lastAddress = classes[ipPrefixIndex][3], classes[ipPrefixIndex][4]

    # else it's class E
    else:
        ipPrefixIndex = 4
        ipClass = classes[ipPrefixIndex][0]
        numNetworks, numHosts = classes[ipPrefixIndex][1], classes[ipPrefixIndex][2]
        firstAddress, lastAddress = classes[ipPrefixIndex][3], classes[ipPrefixIndex][4]        

    # string formatting for output
    return "Class: {}\nNetwork: {}\nHost: {}\nFirst Address: {}\nLast Address: {}".format(
        ipClass, numNetworks, numHosts, firstAddress, lastAddress)

# Class B and C subnet calculator
def get_subnet_stats(ip_addr, subnet_mask):

    binarySubnet = to_binary_string(subnet_mask)    # converts subnet_mask to binary to get CIDR

    cidr = "".join(binarySubnet).count("1")    # gets count of num of 1-bits from subnet mask
    address = "{}/{}".format(ip_addr, cidr)    # IP address in CIDR notation

    # if class B, binarySubnet[-2], else -1
    # if class B, ip should be till second octet, and last octet handled, else till -1

    # class C addresses have subnets with first 3 octets being 255
    subnets = 2 ** binarySubnet[-1].count("1")  # therefore last octet of subnet is only considered for this

    addressableHostsPerSubnet = (2 ** binarySubnet[-1].count("0")) - 2  # addressable hosts per subnet

    ip = ".".join(ip_addr.split(".")[:3])   # getting first 3 octets of ip_addr to use for concatenation (class C)

    subnetmask = int(subnet_mask.split(".")[-1])
    blockSize = 256 - subnetmask   # value of the block size

    # list comprehensions which concatenates ip with incrementing blocksizes for the following addresses:
    validSubnets = ["{}.{}".format(ip, str(i)) for i in range(0, subnetmask + 1, blockSize)]
    broadcastAddresses = ["{}.{}".format(ip, str(i)) for i in range(blockSize - 1, 256, blockSize)]
    firstAddresses = ["{}.{}".format(ip, str(i)) for i in range(1, 256, blockSize)]
    lastAddresses = ["{}.{}".format(ip, str(i)) for i in range(blockSize - 2, 256, blockSize)]
    return "Address: {}\nSubnets: {}\nAddressable hosts per subnet: {}\nValid subnets: {}\nBroadcast addresses: {}\nFirst addresses: {}\nLast addresses: {}".format(
        address, subnets, addressableHostsPerSubnet, validSubnets, broadcastAddresses, firstAddresses, lastAddresses)

def main():
    # 
    # print(get_class_stats("192.168.10.0"))
    print(get_subnet_stats("192.168.10.0","255.255.255.192"))
    # print(get_subnet_stats("172.16.0.0","255.255.192.0"))

if __name__ == '__main__':
    main()
