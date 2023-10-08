
def supress_exception(exception = KeyError, result = False):
    def dummy(fn):
        def inner(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except exception as e:
                if result is not None:
                    return result
                else:
                    raise e
        return inner
    return dummy

users = {'Prerana': 'prerana@23', 'Pranav': 'prn@24' }

@supress_exception(KeyError, result=False)
def authenticate(user, password):
    print(f'Authenticating')
    return users.get(user) == password

result = authenticate('Preraa', 'prerana@23')
print("Authentication result: ", result)
