import unittest
from client_utils import *
# from client_functions import *
# from server_functions import *



# testing getting from command line correct address and port for server_pack and client_pack and
# their default values from config files

#functions tested: get_addr_port, parse_configs

class TestGettingConfigs(unittest.TestCase):

    default_addr_client = '127.0.0.1'
    port = 7777

    script_name_client = 'client.py'

    config_source_client = 'configs_client.yaml'

    result_client = ('127.0.0.1', 7777)

# parsing config files for correct default values
    def testParseConfigsClient(self):
        self.assertEqual(parse_configs(self.config_source_client), self.result_client)

# parsing command line containing :
    # all parameters "параметры командной строки скрипта client_pack.py <addr> [<port>]: addr — ip-адрес сервера"

    def testGetFullParamsClient(self):
        self.assertEqual(get_addr_port([self.script_name_client, '-a', self.default_addr_client, '-p', self.port],
                                       self.config_source_client),
                         self.result_client)
    # script and address

    def testGetAddrClient(self):
        self.assertEqual(get_addr_port([self.script_name_client, '-a', self.default_addr_client],
                                       self.config_source_client),
                         self.result_client)
    # script and port

    def testGetPortClient(self):
        self.assertEqual(get_addr_port([self.script_name_client, '-p', self.port], self.config_source_client),
                         self.result_client)

    # script only

    def testGetScriptClient(self):
        self.assertEqual(get_addr_port([self.script_name_client], self.config_source_client), self.result_client)





if __name__ == '__main__':
    unittest.main()


