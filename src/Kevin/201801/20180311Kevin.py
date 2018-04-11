def list_min(g):
    m = g[0]
    for i in g:   
        if i < m:
            m = i
    print(m)             
   
list_min(g = [1, 8, 6, 9, 5])