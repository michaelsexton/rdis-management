'''
    A set of helper functions for comparing strings with specific properties, eg two strings
    such as "BMR Canberra Well 1" and "Canberra Well 1" should be considered the same.
'''
import Levenshtein

def cbac(left, right):
    ''' CBAC strings normally look like "CBAC012345' and "CBAC12345", which are duplicates,
         but have the same edit distance as "CBAC12345" and "CBAC12346".
         
         Therefore, we strip the CBAC substring, convert the remainder to an int, then 
         get the Levenshtein ratio for those two integers as string

    '''
    strings = [string.lower().replace('cbac','').strip() for string in [left, right]]
    try:
        return Levenshtein.ratio(*[str(int(string)) for string in strings])
    except Exception as e:
        # The stripped usually strings cannot be converted to an int if we are here,
        # so we default to the Levenshtein distance for the stripped strings
        return Levenshtein.ratio(*strings)
    
def bmr(left, right):
    '''Compares the edit distance of two strings with the substring BMR removed'''
    left = left.lower().replace('bmr','').strip()
    right = right.lower().replace('bmr','').strip()
    return Levenshtein.ratio(left, right)