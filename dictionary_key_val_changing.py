daq_list_cfg = {}
act_daq_list = -1
events = {}
for de in daq_entries.items():
    tmp_event = de[1]['event']
    if tmp_event not in events:
        act_daq_list += 1
        # self._daq_list_cfg[act_daq_list] = {'odt_num': 0, 'event': tmp_event}
        events[tmp_event] = {'daq_list': act_daq_list, 'odt': -1}

    events[tmp_event]['odt'] += 1
    # self._daq_list_cfg[ events[tmp_event]['daq_list']]['odt_num'] += 1
    de[1]['daq_list'] = events[tmp_event]['daq_list']
    de[1]['odt'] = events[tmp_event]['odt']

act_odt_entry = -1
for daq_list in range(0, act_daq_list + 1):
    for de in daq_entries.items():
        if daq_list == de[1]['daq_list']:
            act_odt_entry += 1
            de[1]['odt_entry'] = act_odt_entry
