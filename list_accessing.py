

# example 1
daq_entries = {
    'V_SBC_1msState':        {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 4, 'ecu_addr_ext': 0, 'ecu_addr': 1879135900, 'event': 1},
    'V_DEM_SystemUpCounter': {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 4, 'ecu_addr_ext': 0, 'ecu_addr': 1879243776, 'event': 1},
    'V_TM_Counter':          {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 4, 'ecu_addr_ext': 0, 'ecu_addr': 1879167772, 'event': 1},
    'V_TM_Counter_1':        {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 1, 'ecu_addr_ext': 0, 'ecu_addr': 1879167772, 'event': 2},
    'V_TM_Counter_6':        {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 6, 'ecu_addr_ext': 0, 'ecu_addr': 1879167772, 'event': 2},
    'V_CSM_SYS_EcuControl':  {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 1, 'ecu_addr_ext': 0, 'ecu_addr': 1610653796, 'event': 2}}

# to get example 1 results:
for key in daq_entries.items():
    """
        print('old:')
        print(daq_entries[key[0]]['daq_list'])
    
        daq_entries[key[0]]['daq_list'] = 1
    
        print('new:')
        print(daq_entries[key[0]]['daq_list'])
    """
    for value in key:
        if key[0] in value:
            if daq_entries[key[0]]['event'] == 1:
                daq_entries[key[0]]['daq_list'] = daq_entries[key[0]]['daq_list'] + 1

                daq_entries['V_SBC_1msState']['odt'] = daq_entries['V_SBC_1msState']['odt'] + 1
                daq_entries['V_DEM_SystemUpCounter']['odt'] = daq_entries['V_DEM_SystemUpCounter']['odt'] + 1
                daq_entries['V_TM_Counter']['odt'] = daq_entries['V_TM_Counter']['odt'] + 1

                daq_entries['V_SBC_1msState']['odt_entry'] = daq_entries['V_SBC_1msState']['odt_entry'] + 1
                daq_entries['V_DEM_SystemUpCounter']['odt_entry'] = daq_entries['V_DEM_SystemUpCounter']['odt_entry'] + 1
                daq_entries['V_TM_Counter']['odt_entry'] = daq_entries['V_TM_Counter']['odt_entry'] + 1

                print(daq_entries[key[0]])

            else:
                daq_entries[key[0]]['daq_list'] = daq_entries[key[0]]['daq_list'] + 2

                daq_entries['V_TM_Counter_1']['odt'] = daq_entries['V_TM_Counter_1']['odt'] + 1
                daq_entries['V_TM_Counter_6']['odt'] = daq_entries['V_TM_Counter_6']['odt'] + 1
                daq_entries['V_CSM_SYS_EcuControl']['odt'] = daq_entries['V_CSM_SYS_EcuControl']['odt'] + 1

                daq_entries['V_TM_Counter_1']['odt_entry'] = daq_entries['V_TM_Counter']['odt_entry'] + 1
                daq_entries['V_TM_Counter_6']['odt_entry'] = daq_entries['V_TM_Counter']['odt_entry'] + 2
                daq_entries['V_CSM_SYS_EcuControl']['odt_entry'] = daq_entries['V_TM_Counter']['odt_entry'] + 3

                print(daq_entries[key[0]])
