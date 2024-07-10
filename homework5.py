immutable_var= 123,'food', 321
print('immutable_var: ',immutable_var,)
try:
    immutable_var[1]=258
except Exception as err:
    print(err)
mutable_list = [321,'to',258]
mutable_list[0]='id like'
mutable_list[2]='sleep'
print('mutable_list:',mutable_list,' Modified')


