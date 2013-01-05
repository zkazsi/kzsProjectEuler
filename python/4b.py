def ispalindrome(w):
    return str(w) == str(w)[::-1]

def is_palindromic(num, base=10):
    """Check if 'num' in base 'base' is a palindrome, that's it, if it can be
    read equally from left to right and right to left."""
    digitslst = digits_from_num(num, base)
    return digitslst == list(reversed(digitslst))
    
def problem4():
    """Find the largest palindrome made from the product of two 3-digit numbers."""
    # A brute-force solution is a bit slow, let's try to simplify it a little bit:
    # x*y = "abccda" = 100001a + 10010b + 1100c = 11 * (9091a + 910b + 100c)
    # So at least one of them must be multiple of 11. 
    candidates = (x*y for x in xrange(110, 1000, 11) for y in xrange(x, 1000))
    print(max(x for x in candidates if ispalindrome(x)))
