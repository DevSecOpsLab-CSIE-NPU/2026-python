def clean_sequence(s):
    if not s.strip(): return {"dedupe":[],"asc":[],"desc":[],"evens":[]}
    n = [int(x) for x in s.split()]
    return {"dedupe":list(dict.fromkeys(n)),"asc":sorted(n),"desc":sorted(n,reverse=True),"evens":[x for x in n if x%2==0]}
