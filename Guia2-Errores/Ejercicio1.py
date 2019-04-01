def parse_bin(s):
    t = s.split(',')
    if(len(t) > 1):
        return int(t[0], 2) + int(t[1], 2) / 2.**len(t[1])
    else:
        return int(t[0], 2)

var = input("Ingrese valor binario (para decimales ingrese con ,): ")
print(str(parse_bin(var)))