# sort by the end of the events, always choose the event with earlier event to visit in the first day possible


def max_events(events):
    events.sort(key=lambda x: x[1])
    attend = set()
    for event in events:
        for i in range(event[0], event[1] + 1):
            if i - 1 not in attend:
                attend.add(i - 1)
                break
    return len(attend)
