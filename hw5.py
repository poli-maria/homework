immutable_var = (12, 18, 19, False, 'Happy Birthday')
print('Immutable tuple: ',immutable_var)
# immutable_var [0] = 8 кортеж - неизменяемая последовательность, которая может содержать изменяемые элементы. Сейчас таких элементов нет.
mutable_list = [12, 18, 19, False, 'Happy Birthday']
mutable_list [1] = 16
mutable_list [3] = True
mutable_list [4] = 'Happy New Year'
print('Mutable list: ', mutable_list)