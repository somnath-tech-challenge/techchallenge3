import requests

def get_value_nested(nested_object,*key):
    if key and nested_object:
        value = key[0]
        if value:
            d = nested_object.get(value)
            return d if len(key) == 1 else get_value_nested(d, *key[1:])

# The main function to call the pass object to fetch value.
if __name__ == '__main__':
    object = {'a':{'b':{'c':'d'}}}
    val = get_value_nested(object,"a", "b", "c")
    print(val)
