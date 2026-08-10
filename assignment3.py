print("Welcome To Book My Bus")
name=input("Enter Your Name: ")
age=int(input("Enter Your Age: "))
ph_numer=int(input("Enter Your Phone Number: "))
email=input("Enter Your Email: ")
places=print("\n1.Thiruvananthapuram\n","2.Kollam\n","3.Alappuzha\n")
route1=input("From: ")
route2=input("To: ")
seats=int(input("Number of seates: "))
if "Thiruvananthapuram"==route1 and "Kollam"==route2 or "Kollam"==route1 and "Thiruvananthapuram"==route2:
    print("Thiruvanathapuram - Kollam")
    print("Rs 250")
    price=250
elif "Thiruvananthapuram"==route1 and "Alappuzha"==route2 or "Alappuzha"==route1 and "Thiruvananthapuram"==route2:
    print("Thiruvanathapuram - Alappuzha ")
    print("Rs 500")
    price=500
elif "Kollam"==route1 and "Alappuzha"==route2 or "Alappuzha"==route1 and "Kollam"==route2:
    print("Kollam - Alappuzha")
    print("Rs 300")
    price=300
else:
    print("invalid route")
total=price*seats


if price>0:
    print("\n----------Ticket Details----------\n")
    print(f"Name:{name} \nAge:{age} \nPhone numer:{ph_numer} \nEmail:{email}")
    print("From",route1)
    print("To",route2)
    print("Rs.",price)
    print("No of seats=",seats)
    print("Total=Rs",total)
else:
    print("Transation invalid")

