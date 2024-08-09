immutable_var = (1,2.1,True,'apple')
print(immutable_var)
# так как кортеж хранит не сами объекты, а ссылку на них, следовательно, его нельзя изменить

mutable_list = [1,2,3,4,5]

mutable_list.pop(4)

print(mutable_list)