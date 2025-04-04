# Hash
> remove duplicates, optimization
> `dictionary` based data structure

## when should we use hash?
 - when we need a key-value operation
 - cause list only can be accessed by index

## time-complexity
|operation|Dictionary|List|
|--|--|--|
|Get|O(1)|O(1)|
|insert|O(1)|O(N)|
|update|O(1)|O(1)|
|delete|O(1)|O(N)|
|search|O(1)|O(N)|

### insert
```
# init just like json 
dict = {}
dict = dict()

# insert or update
dict['a'] = 1 # {'a': 1}
dict['a'] = 3 # {'a': 3}

# get
dict = {'a': 1, 'b': 2}
dict['a'] # 1
dict.get('b', 0) # 2 // return 0 if 'b' is null

# delete

dict = {'a': 1, 'b': 2}
del dict['a'] # {'b': 2}
del dict['c'] # return keyerror if undefined

dict.pop('c',3000) # return 3000 if 'c' is undefined

```

### iterate
```
dict = {'a': 1, 'b': 2}
for key in dict:
    print(key)
    # print(dict[key]) to access values

for key, value in dict.items():
print(key, value)
```

### tips
```
# to check whether key exists
print ('a' in  dict) # True
print ('a' not in dict) # False

# to extract data

dict.keys() 

dict.values()

dict.items()
```
