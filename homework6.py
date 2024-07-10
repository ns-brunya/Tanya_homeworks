my_dict={'Eva':'cat girl','Kaiser':'Dog','Iceman':'Cat boy'}
print('Dict:',my_dict)
print('Existing value',my_dict['Kaiser'])
my_dict['Murzic']='kitten'
my_dict.update({'Brunya':'Rat',
                'Kesha':'parrot'})
deleted=my_dict.pop('Eva')
print('deleted:',deleted)
print('Modified dictionaty',my_dict)

set1=set(my_dict)
set2=set([1,1,2,2,3,3,4])
my_set = set1|set2
print('set:',my_set,'type:',type(my_set))
my_set=my_set.union({'Quiz','Answer'})
my_set.remove('Brunya')
print('Modified set: ',my_set)