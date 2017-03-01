import signal

# http://stackoverflow.com/questions/492519/timeout-on-a-function-call
class TimeoutException(BaseException):
    pass

# To use this funciton, pass in the amount of time in seconds that this function should run maximally, the function that you're looking to time out, and the failure response you expect from the function should it time out. This will return a clojure involving your function that will then take in you funtion and either return None or the value of the passed in function 
def timeout(time, func, failure):
    def handler(signum, other):
        raise TimeoutException
        #pass    
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

            
    def wrapped(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            signal.alarm(0)
            return result
        except:
            return failure
        
    return wrapped

