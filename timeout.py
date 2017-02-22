import signal

# http://stackoverflow.com/questions/492519/timeout-on-a-function-call
class TimeoutException(BaseException):
    pass

# To use this funciton, pass in the amount of time, in seconds that this function should run maximally, and the function that you're looking to time out. This will return a clojure involving your function that will then take in you funtion and either return null or the value of the passed in function 
def timeout(time, func):
    def handler(signum, other):
        raise TimeoutException
    
    signal.alarm(time)
    signal.signal(signal.SIGALRM, handler)
            
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return null
        
    return wrapped

