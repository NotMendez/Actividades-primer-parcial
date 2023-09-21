def multiplicacion(a,b):
 x= a*b
 return=x 

def division(a,b):
 x= a/b
 return = x

print("Dame el primer número:")
 a= int(input())
print("Dame el segundo número:")
 b= int(input())
print("La multiplicación da", multiplicacion,"y la división da", division)


def conversion(k,m):
  
 x= k*m
 return x

print("¿Cuántos kilometros recorriste?")
k= int(input())
m=1000
print("Recorriste:",conversion(k,m),"metros")



def area_triangulo (b,a):
 x= (a*b)/2
 return x

print("¿Cuál es la base?")
b= int(input())
print("¿Cuál es la altura?")
a=int(input())
print("El área del triangulo es:",area_triangulo (b,a),"m^2")
