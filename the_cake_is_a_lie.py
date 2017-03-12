# Solution overview:
# 1. Take substrings of query as a kernel
# 2. Compare kernel for matches
# 3. Earliest match results in more sharing (=> caring).
def factors(n):
    return [k for k in list(range(1, n+1)) if (n % k == 0)]

def match(kernel, vec):
    window_posn = [len(kernel)*i for i in range(int(len(vec)/len(kernel)))]
    for ix in window_posn:
            for k, asc in zip(kernel, vec[ix:ix+len(kernel)]):
                if (k - asc) != 0:
                    return False
    return True

def answer(s):
    asc = [ord(c) for c in s]
    for f in factors(len(s)):
        kernel = asc[:f]
        if match(kernel, asc):
            return int(f/len(s))
