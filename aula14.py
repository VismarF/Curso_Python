#função format
a = 'A'
b = 'B'
c = 1.1
string = 'b={nome2} \na={nome1} \na={nome1} \na={nome1} \nc={nome3:.2f}'

formato = string.format(
   nome1=a, nome2=b, nome3= c)


print(formato)