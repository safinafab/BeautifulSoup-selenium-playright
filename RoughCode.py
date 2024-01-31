class WhatsApp:
    def __init__(self,name) :
       self.username = name
       self.is_logged_in = False
       
def is_authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated
def new_user(name):
    print(f"The new accoount is created for {name.username}")
    
    
create_account = WhatsApp("angela")
create_account.is_logged_in = True
new_user(create_account)