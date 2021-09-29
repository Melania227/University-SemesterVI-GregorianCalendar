f_g= [0, 5, 3, 1]
    c = (anno-1)//100
    print(c)
    g = anno - 1 - (100 * c)
    print(g)
    w = (1 + 0 + f_g[c%4] + (g//4))%7
    print(f_g[c%4])