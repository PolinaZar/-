def calc(x):
    ver_var_Samsung Galaxy A3 = {0:0.1, 1:1, 2:1, 5:1, 7:0}
    ver_var_Samsung Galaxy A5 = {0:0.1, 1:1, 3:1, 4:1, 7:0}
    ver_var_Samsung Galaxy S7 = {0:0.5, 1:1, 7:0.8}
    ver_var_Samsung Galaxy S8 = {0:0.3, 1:1, 7:0.7}
    ver_var_iPhone6S = {0:0.1, 1:1, 8:0.6, 7:0}
    ver_var_iPhone7 = {0:0.1, 1:1, 6:1, 7:0.6}
    ver_var_Lenovo Vibe K5 Note= {0:0.1, 1:1, 6:1, 7:0.5}
    ver_var_Lenovo K6 Note  = {0:0.1, 1:1, 6:1, 7:0.4}
    ver_var_Lenovo Moto X Style = {0:0.1, 1:1, 7:0}
    ver_var_Lenovo Moto Z = {0:0.1, 1:1, 6:1, 7:0.3}
    for i in range(0,len(x)-1):
        for j in range(0,len(ver_var_Samsung Galaxy A3)-1):
            if i==list(ver_var_Samsung Galaxy A3.keys())[j]:
                 Samsung Galaxy A3 = x[i]*list(ver_var_Samsung Galaxy A3.values())[j]
        for k in range(0,len(ver_var_Samsung Galaxy A5)-1):
            if i==list(ver_var_Samsung Galaxy A5.keys())[k]:
                Samsung Galaxy A5 = x[i]*list(ver_var_Samsung Galaxy A5.values())[k]
        for l in range(0,len(ver_var_Samsung Galaxy S7)-1):
            if i==list(ver_var_Samsung Galaxy S7.keys())[l]:
                Samsung Galaxy S7 = x[i]*list(ver_var_Samsung Galaxy S7.values())[l]
        for m in range(0,len(ver_var_Samsung Galaxy S8)-1):
            if i==list(ver_var_Samsung Galaxy S8.keys())[m]:
                Samsung Galaxy S8 = x[i]*list(ver_var_Samsung Galaxy S8.values())[m]
        for n in range(0,len(ver_var_iPhone6S)-1):
            if i==list(ver_var_iPhone6S.keys())[n]:
                iPhone6S = x[i]*list(ver_var_iPhone6S.values())[n]
        for o in range(0,len(ver_var_iPhone7)-1):
            if i==list(ver_var_iPhone7.keys())[o]:
                iPhone7 = x[i]*list(ver_var_iPhone7.values())[o]
        for p in range(0,len(ver_var_Lenovo Vibe K5 Note)-1):
            if i==list(ver_var_Lenovo Vibe K5 Note.keys())[p]:
                Lenovo Vibe K5 Note = x[i]*list(ver_var_Lenovo Vibe K5 Note.values())[p]
        for q in range(0,len(ver_var_Lenovo K6 Note)-1):
            if i==list(ver_var_Lenovo K6 Note.keys())[q]:
                Lenovo K6 Note = x[i]*list(ver_var_Lenovo K6 Note.values())[q]
        for r in range(0,len(ver_var_Lenovo Moto X Style)-1):
            if i==list(ver_var_Lenovo Moto X Style.keys())[r]:
                Lenovo Moto X Style = x[i]*list(ver_var_Lenovo Moto X Style.values())[r]
        for s in range(0,len(ver_var_Lenovo Moto Z)-1):
            if i==list(ver_var_Lenovo Moto Z.keys())[s]:
                Lenovo Moto Z = x[i]*list(ver_var_Lenovo Moto Z.values())[s]
    y=[str(Samsung Galaxy A3),str(Samsung Galaxy A5),str(Samsung Galaxy S7),str(Samsung Galaxy S8),str(iPhone6S),str(iPhone7),str(Lenovo Vibe K5 Note),str(Lenovo K6 Note),str(Lenovo Moto X Style),str(Lenovo Moto Z)]
    return y
