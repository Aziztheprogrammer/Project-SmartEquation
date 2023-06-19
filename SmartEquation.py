from math import*
print("Created By : Mohamed Aziz Berhouma \nProject : Smart Equation \nGitHub : https://github.com/Aziztheprogrammer")
def equation(a, b, c):
    equation = str(a) +"x² "+ string_b +"x "+ string_c+" = 0"
    print("C'est Votre Equation : " + equation)
    disc = b**2 - (4*a*c)
    print("Le Discriminant De Cet Equation Est :" + str(disc))
    if disc > 0 :
        solution_primaire = (-b - sqrt(disc)) / (2*a)
        solution_secondaire = (-b + sqrt(disc)) / (2*a)
        print('Solution Primaire = ', solution_primaire,
        'Solution Secondaire = ', solution_secondaire)
    elif disc < 0 :
        print("Il y a Pas De Solution Pour Cette Equation ! ")
    else :
        solution_double = -b / (2*a)
        print("Solution Double = ", solution_double)
    
a_1 = int(input("Donner a :"))
if a_1 > 0 or a_1 == 0 :
    string_a = str(a_1)
elif a_1 < 0 :
    string_a = "- " + str(a_1*(-1))
b_1 = int(input("Donner b :"))
if b_1 > 0 or b_1 == 0 :
    string_b = "+ " + str(b_1)
elif b_1 < 0 :
    string_b = "- " + str(b_1*(-1))
c_1 = int(input("Donner c :"))
if c_1 > 0 or c_1 == 0 :
    string_c = "+ " + str(c_1)
elif c_1 < 0 :
    string_c = "- " + str(c_1*(-1))

equation(a_1, b_1, c_1)
    
	


