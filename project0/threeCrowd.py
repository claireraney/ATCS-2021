people = ['claire', 'elizabeth', 'zoe', 'alli']
if (len(people)) > 3:
    print('The room is crowded')
del people[0]
people.remove('alli')
if (len(people)) > 3:
    print('The room is crowded')