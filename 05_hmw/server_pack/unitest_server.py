import unittest
from server_utils import *
# from client_functions import *
# from server_functions import *



# testing getting from command line correct address and port for server_pack and client_pack and
# their default values from config files

#functions tested: get_addr_port, parse_configs

class TestGettingConfigs(unittest.TestCase):
    default_addr_server = ''

    port = 7777
    script_name_server = 'server.py'

    config_source_server = 'configs_server.yaml'

    result_server = ('', 7777)


# parsing config files for correct default values
    def testParseConfigsServer(self):
        self.assertEqual(parse_configs(self.config_source_server), self.result_server)

# parsing command line containing :
    # all parameters "параметры командной строки скрипта client_pack.py <addr> [<port>]: addr — ip-адрес сервера"
    def testGetFullParamsServer(self):
        self.assertEqual(get_addr_port([self.script_name_server, '-a', self.default_addr_server, '-p', self.port],
                                       self.config_source_server),
                         self.result_server)


    # script and address
    def testGetAddrServer(self):
        self.assertEqual(get_addr_port([self.script_name_server, '-a', self.default_addr_server],
                                       self.config_source_server),
                         self.result_server)

    # script and port
    def testGetPortServer(self):
        self.assertEqual(get_addr_port([self.script_name_server, '-p', self.port], self.config_source_server),
                         self.result_server)



    # script only
    def testGetScriptServer(self):
        self.assertEqual(get_addr_port([self.script_name_server], self.config_source_server), self.result_server)







if __name__ == '__main__':
    unittest.main()


