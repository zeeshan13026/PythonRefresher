def double(x):
    return x*2

sequence = [2,3,4,5,6,7]

'''List comprehension'''
#doubled = [double(x) for x in sequence]

'''Using lambda in list comprehension'''
#doubled = [lambda x:x*2 for x in sequence]

'''Using Map, Map returns map so we have to cast in list'''
#doubled = map(double,sequence)

'''lambda in Map'''
doubled = map(lambda x:x*2,sequence)
print(list(doubled))