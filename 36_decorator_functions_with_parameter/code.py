import functools
user = {"username":"jose", "access_level":"admin"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args,**kwargs):
        if user['access_level'] == 'admin':
            return func(*args,**kwargs)
        else:
            return f"you are not admin"
    return secure_function

@make_secure
def get_password(panel):
    if panel == 'admin':
        return "1234"
    elif panel == 'billing':
        return 'super_secure_password'

#get_admin_password = make_secure(get_admin_password)
print(get_password('billing'))
