# frozenset   {}

  # exactly same as set but frozenset is immutable   
      # insertion order is not important here  (set will be unordered in return)
      # duplicates are not allowed (internally it will return only one value)
      # represent in curly braces
      # heterogenous object allowed

fs={88,88,88.08,'frozen','set'}
fs=frozenset(fs)


print(type(fs))
print(fs)
