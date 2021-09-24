"""
Python program to find the largest element and its location.
"""

def largest_element(a, loc = False):
    """ Return the largest element of a sequence a.
    """
    max = a[0]
    maxelem = 0
    try:
        for i in range(0, len(a)):
            if a[i] > max:
                max = a[i]
                maxelem = i
        if (loc):
            return (max, maxelem)
        return max
    except TypeError:
        print("Type Error")
    except:
            print("Unexpected error")
            raise

def largest_el2(a, loc=False):
    maxval = 0
    for (i, e) in enumerate(a):
        if e > maxval:
            maxval = e
    return maxval


if __name__ == "__main__":

    a = [1,2,'a',2,1]
    print("Largest element is {:}".format(largest_element(a)))
