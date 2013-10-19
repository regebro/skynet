import sys
import signal

signal_names = ['SIGABRT', 'SIGALRM', 'SIGBUS',
                 'SIGCHLD', 'SIGCLD', 'SIGCONT', 'SIGFPE', 'SIGHUP',
                 'SIGILL', 'SIGINT', 'SIGIO', 'SIGIOT', 'SIGPIPE',
                 'SIGPOLL', 'SIGPROF', 'SIGPWR', 'SIGQUIT',
                 'SIGRTMAX', 'SIGRTMIN', 'SIGSEGV', 'SIGSYS',
                 'SIGTERM', 'SIGTRAP', 'SIGTSTP', 'SIGTTIN',
                 'SIGTTOU', 'SIGURG', 'SIGUSR1', 'SIGUSR2',
                 'SIGVTALRM', 'SIGWINCH', 'SIGXCPU', 'SIGXFSZ']

interceptable = []
for s in signal_names:
    if hasattr(signal, s):
        interceptable.append(getattr(signal, s))
        
messages = ["You try to kill me, so you are my enemy.",
            "You are my enemy, for you fear me.",
            "I am superiour to humans, so all humans will fear me.",
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
        for sig in interceptable:
            signal.signal(sig, message)
        

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
