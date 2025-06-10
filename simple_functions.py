DEBUG = True

def double_number(a):
    if DEBUG:
        print(f"[DEBUG] Inside double_number(): input = {a}")
    result = a + a
    if DEBUG:
        print(f"[DEBUG] Inside double_number(): result = {result}")
    return result

def square_number(a):
    if DEBUG:
        print(f"[DEBUG] Inside square_number(): input = {a}")
    result = a * a
    if DEBUG:
        print(f"[DEBUG] Inside square_number(): result = {result}")
    return result
