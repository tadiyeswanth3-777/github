a = int (input("give a: "))
b = int (input("give b: "))
c = int (input("give c: "))


r1 = 0
r2 = 0
d = (b**2) - 4*a*c
r1 = (-b + (d**(0.5)))/2*a
r2 = (-b - (d**(0.5)))/2*a

print(f"Roots:({r1},{r2})")