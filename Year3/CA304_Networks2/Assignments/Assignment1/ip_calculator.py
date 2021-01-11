# dictionary map index to a list containing (ip class, network bits, host bits, start address, end address)
# the keys indicate which index the first 0 appears in the prefix
classes = {
    0:["A", 7, 24, "0.0.0.0", "127.255.255.255"],
    1:["B", 14, 16, "128.0.0.0", "191.255.255.255"],
    2:["C", 21, 8, "192.0.0.0", "223.255.255.255"],
    3:["D", "N/A", "N/A", "224.0.0.0", "239.255.255.255"],
    4:["E", "N/A", "N/A", "240.0.0.0", "255.255.255.255"]
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
        ipPrefixIndex = firstOctet.index("0")   # gets first index that 0 appears in prefix (index of first "0" occurence in first octet)

        ipClass = classes[ipPrefixIndex][0]     # gets corresponding IP Class from "classes" mapping based on ipPrefixIndex

        # calculating the number of networks, hosts, and the first and last address based on current class (from dictionary)
        numNetworks = 2 ** classes[ipPrefixIndex][1]
        numHosts = 2 ** classes[ipPrefixIndex][2]
        firstAddress, lastAddress = classes[ipPrefixIndex][3], classes[ipPrefixIndex][4]

    # else if it's class D (checking prefix)
    elif firstOctet[:4] == "1110":
        ipPrefixIndex = 3   # hardcoded index of first zero of the prefix to get class stats
        classDInfo = get_D_or_E(ipPrefixIndex)
        # string formatting for output
        return "Class: {}\nNetwork: {}\nHost: {}\nFirst Address: {}\nLast Address: {}".format(
            classDInfo[0], classDInfo[1], classDInfo[2], classDInfo[3], classDInfo[4])

    # else it's class E
    else:
        ipPrefixIndex = 4
        classEInfo = get_D_or_E(ipPrefixIndex)
        # string formatting for output
        return "Class: {}\nNetwork: {}\nHost: {}\nFirst Address: {}\nLast Address: {}".format(
            classEInfo[0], classEInfo[1], classEInfo[2], classEInfo[3], classEInfo[4])

    # string formatting for output
    return "Class: {}\nNetwork: {}\nHost: {}\nFirst Address: {}\nLast Address: {}".format(
        ipClass, numNetworks, numHosts, firstAddress, lastAddress)

# added this function to remove code repetition
# gets stats for class D or E networks (depending on prefix), returns info in list
def get_D_or_E(index):

    # index is the ipPrefixIndex
    # getting the class info from the dictionary
    ipClass = classes[index][0]
    numNetworks, numHosts = classes[index][1], classes[index][2]
    firstAddress, lastAddress = classes[index][3], classes[index][4]

    return [ipClass, numNetworks, numHosts, firstAddress, lastAddress]


# Class B and C subnet calculator
def get_subnet_stats(ip_addr, subnet_mask):

    binarySubnet = to_binary_string(subnet_mask)    # converts subnet_mask to binary to get CIDR

    cidr = "".join(binarySubnet).count("1")    # gets count of num of 1-bits from subnet mask

    # not the best approach having the same thing twice to only deal with something specific in IP addresses
    # check if cidr is within range 16-23 (Class B)
    if 16 <= cidr <= 23:
        subnetIndex = -2    # used for indexing to subnet_mask octet to get subnetMask
        subnetMask = int(subnet_mask.split(".")[subnetIndex])   # gets value of subnet mask for block size calculation
        blockSize = 256 - subnetMask   # value of the block size
        ip = ".".join(ip_addr.split(".")[:subnetIndex])    # getting first 2 octets of ip_addr to use for concatenation

        address = "{}.0.0/{}".format(ip, cidr)  # IP address in cidr notation
        # not the best since I'm hardcoding the last octet
        # list comprehensions which concatenates ip with incrementing blocksizes for the following addresses:
        validSubnets = ["{}.{}.{}".format(ip, str(i), "0") for i in range(0, int(subnetMask) + 1, int(blockSize))]
        broadcastAddresses = ["{}.{}.{}".format(ip, str(i), "255") for i in range(int(blockSize) - 1, 256, int(blockSize))]
        firstAddresses = ["{}.{}.{}".format(ip, str(i), "1") for i in range(0, 256, int(blockSize))]
        lastAddresses = ["{}.{}.{}".format(ip, str(i), "254") for i in range(int(blockSize) - 1, 256, int(blockSize))]
        
    # else it's 24 <= cidr <= 30 (Class C)
    # does same thing as above, except the last octet is updating in list comprehension and not hardcoded
    elif 24 <= cidr <= 30:
        subnetIndex = -1
        subnetMask = int(subnet_mask.split(".")[subnetIndex])
        blockSize = 256 - subnetMask   # value of the block size
        ip = ".".join(ip_addr.split(".")[:subnetIndex])    # getting first 3 octets of ip_addr to use for concatenation

        address = "{}.0/{}".format(ip, cidr)
        validSubnets = ["{}.{}".format(ip, str(i)) for i in range(0, int(subnetMask) + 1, int(blockSize))]
        broadcastAddresses = ["{}.{}".format(ip, str(i)) for i in range(int(blockSize) - 1, 256, int(blockSize))]
        firstAddresses = ["{}.{}".format(ip, str(i)) for i in range(1, 256, int(blockSize))]
        lastAddresses = ["{}.{}".format(ip, str(i)) for i in range(int(blockSize) - 2, 256, int(blockSize))]

    # class C addresses have subnets with first 3 octets being 255
    # class B have 255's within first 2 octets
    subnets = 2 ** ("".join(binarySubnet[subnetIndex:])).count("1")  # therefore (last/last 2) octet(s) of subnet is only considered for this

    addressableHostsPerSubnet = (2 ** ("".join(binarySubnet[subnetIndex:])).count("0")) - 2  # addressable hosts per subnet

    # string formatting the output
    return "Address: {}\nSubnets: {}\nAddressable hosts per subnet: {}\nValid subnets: {}\nBroadcast addresses: {}\nFirst addresses: {}\nLast addresses: {}".format(
        address, subnets, addressableHostsPerSubnet, validSubnets, broadcastAddresses, firstAddresses, lastAddresses)

# supernetting class C address list (passed in as ip_addr_list)
def get_supernet_stats(ip_addr_list):

    binaryIP = [to_binary_string(ipAddr) for ipAddr in ip_addr_list]

    # checking first 2 octets are equal
    # assert (binaryIP[0][0], binaryIP[0][1]) == (binaryIP[1][0], binaryIP[1][1])
    # assert (binaryIP[1][0], binaryIP[1][1]) == (binaryIP[2][0], binaryIP[2][1])
    # assert (binaryIP[2][0], binaryIP[2][1]) == (binaryIP[3][0], binaryIP[3][1])

    # iterating over last 2 octets of binaryIP's last binary ip addresses
    # essentially, will be used for comparing the first and last ip addresses in binary (using their last 2 octets)
    firstIpLast2Octets = binaryIP[0][-2] + binaryIP[0][-1]   # last 2 octets of first ip address in binary
    lastIpLast2Octets = binaryIP[-1][-2] + binaryIP[-1][-1]    # last 2 octets of last ip address in binary

    # linear search, checking the index of where the last 2 octets don't match
    # then the index is added to 16, since first 16 bits of ip address are all 1's
    i = 0
    while lastIpLast2Octets[i] == firstIpLast2Octets[i] and i < len(lastIpLast2Octets):
        i += 1
    # if the bit we stopped at don't match, but we haven't reached the end, we're done
    if i < len(lastIpLast2Octets):
        subnet = i + 16     # since first 2 octets are common (16 bits guaranteed), we get remaining bits for the subnet
    
    ipCidr = "{}/{}".format(ip_addr_list[0], str(subnet))   # converting IP address to CIDR notation (using first ip address from ip_addr_list)

    # the subnet is the index where the ip address' bits don't match
    # so we now add 1's where they do match, and 0's everywhere else to get netMask
    netMaskStr = ("1" * subnet) + ("0" * (32 - subnet))
    netMask = to_decimal_dot([netMaskStr[i:i + 8] for i in range(0, len(netMaskStr), 8)])  # converts netMaskStr to list (each item in list is an octet), then passed to "to_decimal_dot()"

    return "Address: {}\nNetwork Mask: {}".format(ipCidr, netMask)

def main():

    # running test suite
    import unittest
    from ipUnitTest import IpTestCase
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(IpTestCase))
    runner = unittest.TextTestRunner()
    print(runner)


    # testing sample tests from examples
    print(get_class_stats("136.206.18.7"))
    print("#########################################")
    print("#########################################")
    print(get_class_stats("224.192.16.5"))
    print("#########################################")
    print("#########################################")
    print(get_subnet_stats("192.168.10.0","255.255.255.192"))
    print("#########################################")
    print("#########################################")
    print(get_subnet_stats("172.16.0.0","255.255.192.0"))
    print("#########################################")
    print("#########################################")
    print(get_supernet_stats(["205.100.0.0","205.100.1.0","205.100.2.0","205.100.3.0"]))
    print("#########################################")
    print("#########################################")
    print(get_supernet_stats(["205.100.0.0","205.100.1.0","205.100.2.0","205.100.3.0", "205.100.4.0", "205.100.5.0"]))
    print("#########################################")
    print("#########################################")
    print(get_supernet_stats(["192.100.0.1","192.100.0.2","192.100.0.3","192.100.0.4", "192.100.0.5"]))

    # user can test more IP addresses here
    # print(get_class_stats())
    # print(get_subnet_stats())
    # print(get_supernet_stats())

if __name__ == '__main__':
    main()
