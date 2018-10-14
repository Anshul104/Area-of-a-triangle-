#Anshul Ramavath
#Area Of a Triangle
name = input("What is your name:")
print("Hello, ",name,", Welcome to the Algebra and geometry calculator",sep = "")
print()
input("Press Enter to continue:")
print()
print("Area of a Triangle:")
base = float(input("What is the Value of the Base:"))
height = float(input("What is the Value of the Height:"))
unit = input("What is the Unit of the Triangle:")
area = 0.5*base*height
print()
print("The area of that triangle is ",format(area,'.2f')," ",unit,"^2",sep="" )
print()
input('Press Enter to Continue:')
print()
print('Volume of a Cube:')
side = float(input('What is the Length of your Side:'))
unitvolume = input('What is the Unit of the Side:')
volume = side*side*side
print("The Volume of the Cube is ",format(volume,'.2f')," ",unitvolume,"^3",sep="" )
print()
input('Press enter to Continue:')
print('Quadratic Formula:')
a = float(input('What is the value of a:'))
b = float(input('What is the value of b:'))
c = float(input('What is the value of c:'))
unitquad = input("What is the Units being used:")
print()
preroot = (b*b - 4*a*c)
squareRoot = preroot ** .5
bplus = -1*b + squareRoot
bminus = -1*b - squareRoot
bottom = 2*a
firstanswer = bplus/bottom
secondanswer = bminus/bottom
print()
print("Here is your First possible answer: x =",format(firstanswer,'.2f'),unitquad,sep="")
print("Here is your Second possible answer: x =",format(secondanswer,'.2f'),unitquad,sep="")
print()
print("Goodbye,",name," thank you for using this calculator",sep="")
