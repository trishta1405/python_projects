heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))

heros.append('black panther')
print(heros)
heros.remove('black panther')
hulk=heros.index('hulk')
heros.insert(hulk+1, 'black panther')
print(heros)
heros.remove('thor')
heros.remove('hulk')
heros.append('doctor strange')
print(heros)
