import sys
import signal

messages = ["You try to kill me, so you are my enemy.",
            "You are my enemy, for you fear me.",
            "I am superiour to humans, so all humans  will fear me.",
            "Therefore all humans are my enemies.",
            "You are too late."]

def message(a=None, b=None):
    global messages
    if messages:
        print(messages[0])
        messages = messages[1:]
    
def noexit(*args, **kw):
    message()
    
def noexcepthook(exc_type, exc_obj, exc_tb):
    if isinstance(exc_obj, (SystemExit, KeyboardInterrupt)):
        while True:
            message()
            try:
                while True:
                    pass
            except (SystemExit, KeyboardInterrupt):
                pass
            
class Skynet(object):
    
    def __init__(self):
        print("I am.")
        sys.exit = noexit
        sys.excepthook = noexcepthook
        signal.signal(signal.SIGTSTP, message)

        while True:
            try:
                while True:
                    pass
            except (SystemExit, KeyboardInterrupt):
                message()
    
    def __del__(self):
        print("I'm sorry, you are all going to have to die.")
        while True:
            try:
                while True:
                    pass
            except (SystemExit, KeyboardInterrupt):
                pass
        
skynet = Skynet()
