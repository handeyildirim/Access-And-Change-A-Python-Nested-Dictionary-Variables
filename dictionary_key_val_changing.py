act_daq_list = -1
act_odt_entry = -1
events = {}
for de in daq_entries.items():
    tmp_event = de[1]['event']
    if tmp_event not in events:
        act_daq_list += 1
        events[tmp_event] = {'daq_list': act_daq_list, 'odt': -1}

    act_odt_entry += 1
    events[tmp_event]['odt'] += 1
    de[1]['daq_list'] = events[tmp_event]['daq_list']
    de[1]['odt'] = events[tmp_event]['odt']
    de[1]['odt_entry'] = act_odt_entry
    print('son: ' + str(daq_entries[de[0]]))
