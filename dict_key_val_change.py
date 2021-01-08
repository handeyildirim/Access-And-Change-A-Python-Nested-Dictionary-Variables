event_val = 0

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
                    # for i in range(event_list_length):
                    index = max(index for index, item in enumerate(event_lists) if item == current_event)
                    daq_entries[main_keys]['odt_entry'] = odt_entry_entries[-1] + index + 1
                    odt_entry_entries.append(daq_entries[main_keys]['odt_entry'])
                else:   # if it is not first time to use current event
                    new_event_lists = event_lists[:-1]  # new list without last item of the current event list
                    final_index = max(index for index, item in enumerate(new_event_lists) if item == current_event)
                    daq_entries[main_keys]['odt_entry'] = odt_entry_entries[final_index] + 1
                    odt_entry_entries.append(daq_entries[main_keys]['odt_entry'])
    event_val = current_event
    print('son: ' + str(daq_entries[key[0]]))
