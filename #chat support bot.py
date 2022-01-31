#support bot 

#please note: this software is still in beta


from operator import truediv
from xml.etree.ElementTree import TreeBuilder

print('Please note any info typed in here is not stored')

name = input('what should we call you?:')

print('thank you for contacing us how can we help you '+name)

statement = input('state your problem?:')

print('we will be happy to help you!!! ' + name)
print('please choose from are support method as we can only help with valid options sorry if this caused any inconvince')
print('please select a number please type the number out')
print('a text will pop up above the menu')

ans=True
while ans:
    print("""
    1.Refunding a product
    2.CDC restrictions
    3.Skate issue
    4.Exit/Quit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
      print("\nRefunds are only valid up to 30 days if still in the 30 day mark contact us at example@example.com")
    elif ans=="2":
      print("\n CDC laws block us from providing certain services")
    elif ans=="3":
      print("\n skates issue is common please don't contact us on this please contact the seller")
    elif ans=="4":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")
