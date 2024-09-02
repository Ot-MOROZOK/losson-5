immutable_var = 1,2.0,'ананас',True
print('Immutable tuple:'+(str(immutable_var)))
# immutable_var[0] = 120 -----Кортеж – это неизменяемая упорядоченная коллекция, которая может содержать в себе разные типы данных и он не поддерживает обращение по элементам.
mutable_list= [1,2.0,'оладушек', True]
mutable_list.remove(1)
mutable_list[2]='Баклажан'
mutable_list.append('Носок')
print('Mutable list:'+(str(mutable_list)))