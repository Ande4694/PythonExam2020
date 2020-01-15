"""
    Exercise: Slow down code

    The code below counts down from n -> 0.
    calling countdown(5) prints: 5 4 3 2 1 0

    Create a decorator that slows down you code by 1 second for each step. 
    Call it slowdown().
    For this you can use the 'time' module.

    The countdown function is a recursive function.
    
    When you got the 'slowdown code' working on this recursive function, try to create a more (for you) normal function that does the countdown, and see what happens if you decorate that function with you slowdown() function

"""
def countdown(n):
    if not n:   # 0 is false, not false is true
        return n
    else:
        print(n, end=' ')
        return countdown(n-1) # call the same function with n as one less 
