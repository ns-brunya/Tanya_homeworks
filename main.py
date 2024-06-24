immutable_var='summer','autumn','winter','spring',282,5.5
print(type(immutable_var),':',immutable_var)
mutable_list=['summer','autumn','winter','spring',282,5.5]
print(type(mutable_list),':',mutable_list)
mutable_list[1]='spring'
mutable_list[-1]='PINEAPPLE'
print('Modified list: ',mutable_list)
