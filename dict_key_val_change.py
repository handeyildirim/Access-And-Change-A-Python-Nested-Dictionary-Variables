
# example 1
daq_entries = {
    'V_SBC_1msState':        {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 4, 'ecu_addr_ext': 0, 'ecu_addr': 1879135900, 'event': 1},
    'V_DEM_SystemUpCounter': {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 4, 'ecu_addr_ext': 0, 'ecu_addr': 1879243776, 'event': 1},
    'V_TM_Counter':          {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 4, 'ecu_addr_ext': 0, 'ecu_addr': 1879167772, 'event': 1},
    'V_TM_Counter_1':        {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 1, 'ecu_addr_ext': 0, 'ecu_addr': 1879167772, 'event': 2},
    'V_TM_Counter_6':        {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 6, 'ecu_addr_ext': 0, 'ecu_addr': 1879167772, 'event': 2},
    'V_CSM_SYS_EcuControl':  {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 1, 'ecu_addr_ext': 0, 'ecu_addr': 1610653796, 'event': 2}
}

"""
daq_entries = {
    'V_SBC_1msState':        {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 4, 'ecu_addr_ext': 0, 'ecu_addr': 1879135900, 'event': 2},
    'V_DEM_SystemUpCounter': {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 4, 'ecu_addr_ext': 0, 'ecu_addr': 1879243776, 'event': 2},
    'V_TM_Counter':          {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 4, 'ecu_addr_ext': 0, 'ecu_addr': 1879167772, 'event': 1},
    'V_TM_Counter_1':        {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 1, 'ecu_addr_ext': 0, 'ecu_addr': 1879167772, 'event': 2},
    'V_TM_Counter_6':        {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 6, 'ecu_addr_ext': 0, 'ecu_addr': 1879167772, 'event': 2},
    'V_CSM_SYS_EcuControl':  {'daq_list': -1, 'odt': -1, 'odt_entry': -1, 'bitoff': 255, 'size': 1, 'ecu_addr_ext': 0, 'ecu_addr': 1610653796, 'event': 1},

}
"""
event_val = 0
n = 0
key_list = {}
event_list = {}
daq_list = {}
odt_list = {}
odt_entry_list = {}
event_lists = []
daq_list_entries = []
odt_entries = []
odt_entry_entries = []
for key in daq_entries.items():
    main_keys = key[0]
    value = key[1]
    key_list[main_keys] = daq_entries[main_keys]
    event_list[main_keys] = key_list[key[0]]['event']
    current_event = event_list[main_keys]
    event_lists.append(current_event)
    event_list_length = len(event_list)
    daq_list[main_keys] = key_list[key[0]]['daq_list']
    current_daq_val = daq_list[main_keys]
    odt_list[main_keys] = key_list[key[0]]['odt']
    current_odt_val = odt_list[main_keys]
    odt_entry_list[main_keys] = key_list[key[0]]['odt_entry']
    current_odt_entry_val = odt_entry_list[main_keys]
    if event_val == current_event:
        if 'daq_list' in value:
            daq_entries[main_keys]['daq_list'] = daq_list_entries[-1]
            last_daq_list_entry = daq_entries[main_keys]['daq_list']
            daq_list_entries.append(daq_entries[main_keys]['daq_list'])
        if 'odt' in value:
            daq_entries[main_keys]['odt'] = odt_entries[-1] + 1
            current_odt_val = daq_entries[main_keys]['odt']
            odt_entries.append(current_odt_val)
        if 'odt_entry' in value:
            daq_entries[main_keys]['odt_entry'] = odt_entry_entries[-1] + 1
            odt_entry_entries.append(daq_entries[main_keys]['odt_entry'])
    else:
        if 'daq_list' in value:
            if event_lists.count(current_event) == 1:   # if it is first time to use event
                if not daq_list_entries:
                    daq_entries[main_keys]['daq_list'] += 1
                else:
                    daq_entries[main_keys]['daq_list'] = daq_list_entries[-1] + 1
                current_daq_val = daq_entries[main_keys]['daq_list']
                daq_list_entries.append(current_daq_val)
            else:
                new_event_lists = event_lists[:-1]  # new list without last item of the current event list
                final_index = max(index for index, item in enumerate(new_event_lists) if item == current_event)
                daq_entries[main_keys]['daq_list'] = daq_list_entries[final_index]
                daq_list_entries.append(daq_entries[main_keys]['daq_list'])
        if 'odt' in value:
            if current_event in event_lists:
                count_event = event_lists.count(current_event)  # how many times current event used in event lists
                daq_entries[main_keys]['odt'] = current_odt_val + count_event
                odt_entries.append(daq_entries[main_keys]['odt'])
            else:
                daq_entries[main_keys]['odt'] += 1
        if 'odt_entry' in value:
            if not odt_entry_entries:   # if odt_entry list is empty(beginning)
                daq_entries[main_keys]['odt_entry'] += 1
                odt_entry_entries.append(daq_entries[main_keys]['odt_entry'])
            else:   # if odt_entry list is not empty
                count_all_events = event_lists.count(current_event)
                if count_all_events == 1:   # if it is first time to use current event
                    if event_lists[n] <= event_lists[n+1]:
                        daq_entries[main_keys]['odt_entry'] = odt_entry_entries[-1] + 1
                    else:
                        index = max(index for index, item in enumerate(event_lists) if item == current_event)
                        daq_entries[main_keys]['odt_entry'] = odt_entry_entries[-1] + count_all_events + index
                        odt_entry_entries.append(daq_entries[main_keys]['odt_entry'])
                    odt_entry_entries.append(daq_entries[main_keys]['odt_entry'])
                else:   # if it is not first time to use current event
                    new_event_lists = event_lists[:-1]  # new list without last item of the current event list
                    final_index = max(index for index, item in enumerate(new_event_lists) if item == current_event)
                    daq_entries[main_keys]['odt_entry'] = odt_entry_entries[final_index] + 1
                    odt_entry_entries.append(daq_entries[main_keys]['odt_entry'])
        n += 1
    event_val = current_event
    print('son: ' + str(daq_entries[key[0]]))


