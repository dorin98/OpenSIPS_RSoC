#!/usr/bin/env python3

# import communication
from config_parser import *


class OpenSIPSCTLComm:
    comm_type = ''
    comm_func = ''

    def __init__(self, section):
        # print(section)
        # print(Config.ConfigMap['MODULES.CORE'])
        comm_type = Config.ConfigMap[section]['comm_type']
        comm_type = 'json'
        if comm_type == 'json':
            comm_func = 'communication/opensipsctl_json'
        else:
            print("Unknown communication protocol!")

    # def execute(self, cmd, args=None):
    #     print(mi_json(cmd))
