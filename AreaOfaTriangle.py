#Anshul Ramavath
#Area Of a Triangle
name = input("What is your name:")
print("Hello, ",name,", Welcome to the Algebra and geometry calculator",sep = "")
print()
input("Press Enter to continue:")
print()
print("Area of a Triangle")
base = float(input("What is the Value of the Base:"))
height = float(input("What is the Value of the Height:"))
unit = input("What is the Unit of the Triangle:")
area = 0.5*base*height
print()
print("The area of that triangle is ",format(area,'.2f')," ",unit,"^2",sep="" )