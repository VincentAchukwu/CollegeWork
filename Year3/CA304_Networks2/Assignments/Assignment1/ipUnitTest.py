import unittest, ip_calculator

class IpTestCase(unittest.TestCase):

    # testing via boundary value analysis (above, on, and below the boundary where test case would pass)
    # testing the to_binary_string method for correct output
    def test_toBinaryString(self):
        print("test to_binary_string")

        self.assertEqual(ip_calculator.to_binary_string("128.0.0.0"), ["10000000", "00000000", "00000000", "00000000"])
        self.assertNotEqual(ip_calculator.to_binary_string("128.0.0.0"), ["10000000", "00000000", "00000000", "00000001"])
        self.assertNotEqual(ip_calculator.to_binary_string("128.0.0.0"), ["11111111", "11111111", "00000000", "00000000"])
        self.assertEqual(ip_calculator.to_binary_string("192.168.0.220"), ["11000000", "10101000", "00000000", "11011100"])
        self.assertNotEqual(ip_calculator.to_binary_string("0.0.0.0"), [])
        self.assertNotEqual(ip_calculator.to_binary_string("255.255.255.255"), ["1", "1", "1", "1"])
        self.assertEqual(ip_calculator.to_binary_string("255.255.255.255"), ["11111111", "11111111", "11111111", "11111111"])
        self.assertEqual(ip_calculator.to_binary_string("132.206.19.7"), ["10000100", "11001110", "00010011", "00000111"])

    # testing the to_decimal_dot method for correct output
    def test_toDecimalDot(self):
        print("test to_decimal_dot")

        self.assertEqual(ip_calculator.to_decimal_dot(["11111111", "11111111", "11111111", "11111111"]), "255.255.255.255")
        self.assertNotEqual(ip_calculator.to_decimal_dot(["00000000", "00000000", "00000000", "00000000"]), "0")
        self.assertEqual(ip_calculator.to_decimal_dot(["10110000", "00010000", "00000000", "00000000"]), "176.16.0.0")
        self.assertEqual(ip_calculator.to_decimal_dot(["11001010", "00001010", "10000101", "00001011"]), "202.10.133.11")
        self.assertNotEqual(ip_calculator.to_decimal_dot(["11111111", "01111111", "00000001", "11111110"]), "1.0.0.1")
        self.assertEqual(ip_calculator.to_decimal_dot(["10000100", "11001110", "00010011", "00000111"]), "132.206.19.7")
        self.assertEqual(ip_calculator.to_decimal_dot([]), "")

    # testing the subnet method for correct output
    def test_GetSubnet(self):
        print("test get_subnet_stats")

        self.assertEqual(ip_calculator.get_subnet_stats("192.168.10.0", "255.255.255.192"),
            """Address: 192.168.10.0/26\nSubnets: 4\nAddressable hosts per subnet: 62\nValid subnets: ['192.168.10.0', '192.168.10.64', '192.168.10.128', '192.168.10.192']\nBroadcast addresses: ['192.168.10.63', '192.168.10.127', '192.168.10.191', '192.168.10.255']\nFirst addresses: ['192.168.10.1', '192.168.10.65', '192.168.10.129', '192.168.10.193']\nLast addresses: ['192.168.10.62', '192.168.10.126', '192.168.10.190', '192.168.10.254']""")
        self.assertEqual(ip_calculator.get_subnet_stats("172.16.0.0","255.255.192.0"),
            """Address: 172.16.0.0/18\nSubnets: 4\nAddressable hosts per subnet: 16382\nValid subnets: ['172.16.0.0', '172.16.64.0', '172.16.128.0', '172.16.192.0']\nBroadcast addresses: ['172.16.63.255', '172.16.127.255', '172.16.191.255', '172.16.255.255']\nFirst addresses: ['172.16.0.1', '172.16.64.1', '172.16.128.1', '172.16.192.1']\nLast addresses: ['172.16.63.254', '172.16.127.254', '172.16.191.254', '172.16.255.254']""")
        self.assertNotEqual(ip_calculator.get_subnet_stats("172.16.0.0","255.255.192.0"), "")
        self.assertNotEqual(ip_calculator.get_subnet_stats("192.168.0.0","255.255.255.0"), 
            """Address: 192.168.0.0/26\nSubnets: 0\nAddressable hosts per subnet: 0\nValid subnets: []\nBroadcast addresses: []\nFirst addresses: []\nLast addresses: []""")

    # testing the supernet method for correct output
    def test_GetSupernet(self):
        print("test get_supernet_stats")

        self.assertEqual(ip_calculator.get_supernet_stats(["205.100.0.0","205.100.1.0","205.100.2.0","205.100.3.0"]),
            """Address: 205.100.0.0/22\nNetwork Mask: 255.255.252.0""")
        self.assertEqual(ip_calculator.get_supernet_stats(["192.100.0.1","192.100.0.2","192.100.0.3","192.100.0.4"]), 
            """Address: 192.100.0.1/29\nNetwork Mask: 255.255.255.248""")
        self.assertNotEqual(ip_calculator.get_supernet_stats(["192.100.0.1","192.100.0.2","192.100.0.3","192.100.0.4"]), 
            """Address: 192.0.0.1/29\nNetwork Mask: 0.0.0.0""")
        self.assertEqual(ip_calculator.get_supernet_stats(["192.100.0.1","192.100.0.2","192.100.0.3","192.100.0.4", "192.100.0.5"]), 
            """Address: 192.100.0.1/29\nNetwork Mask: 255.255.255.248""")

    def test_getD_Or_E(self):
        print("test get_D_or_E")

        # this get_D_or_E() returns class D or E properties based on the index passed in
        # here, we're testing if those properties (coming from dictionary in ip_calculator.py) has correct values

        # testing method has correct values for Class D
        self.assertEqual(len(ip_calculator.get_D_or_E(3)), 5)    # if length of list is correct
        self.assertEqual(ip_calculator.get_D_or_E(3)[0], "D")    # check if the ip class is correct
        self.assertEqual(ip_calculator.get_D_or_E(3)[1], "N/A")  # if network bits and host bits are both "N/A"
        self.assertEqual(ip_calculator.get_D_or_E(3)[2], "N/A")
        self.assertEqual(ip_calculator.get_D_or_E(3)[3], "224.0.0.0")    # checking if the ip ranges are correct
        self.assertEqual(ip_calculator.get_D_or_E(3)[4], "239.255.255.255")
        self.assertNotEqual(ip_calculator.get_D_or_E(3)[0], "C")
        self.assertNotEqual(ip_calculator.get_D_or_E(3)[1], 21)

        # testing Class E
        self.assertEqual(len(ip_calculator.get_D_or_E(4)), 5)    # if length of list is correct
        self.assertEqual(ip_calculator.get_D_or_E(4)[0], "E")    # check if the ip class is correct
        self.assertEqual(ip_calculator.get_D_or_E(4)[1], "N/A")  # if network bits and host bits are both "N/A"
        self.assertEqual(ip_calculator.get_D_or_E(4)[2], "N/A")
        self.assertEqual(ip_calculator.get_D_or_E(4)[3], "240.0.0.0")    # checking if the ip ranges are correct
        self.assertEqual(ip_calculator.get_D_or_E(4)[4], "255.255.255.255")
        self.assertNotEqual(ip_calculator.get_D_or_E(4)[0], "A")
        self.assertNotEqual(ip_calculator.get_D_or_E(4)[1], 7)

if __name__ == '__main__':
    unittest.main()
