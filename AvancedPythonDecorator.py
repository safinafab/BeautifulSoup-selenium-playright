class Instagram:
    def __init__(self,name):
        self.name = name    
        self.is_logged_in = False
        
def is_authntiicaed_decortor(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

#every the function is called it go first to the decorator and if the condtion is true 
#then this function gets executed
@is_authntiicaed_decortor      
def usernamea(names):
    print(f"the name of the user is {names.name}")

new_user=Instagram("angela")
new_user.is_logged_in = True
usernamea(new_user)

