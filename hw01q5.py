def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition: #不用改，if 後面 隱含 is True
        return true_result
    else:
        return false_result
# print(if_function(True, 2, 3))
# print(if_function(False, 2, 3))
# print(if_function(3==2, 3+2, 3-2))
# print(if_function(3>2, 3+2, 3-2))

def with_if_statement():
    """
    >>> result = with_if_statement()
    47
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    Welcome to
    61A
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func()) # 在執行if_function時，在執行def的時候才print出welcom to，以及61A。若把順序對調，結果也會對調
    
def cond():
    return True
    
def true_func():
    print("Welcome to")
    
def false_func():
    print("61A")

result = with_if_function(  )
print(result)