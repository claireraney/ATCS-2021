careers = ['doctor', 'programmer', 'truck driver', 'teacher']
print(careers.index('programmer'))
print('doctor' in careers)
careers.append('CEO')
careers.insert(0, 'coach')
for career in careers:
    print(career)