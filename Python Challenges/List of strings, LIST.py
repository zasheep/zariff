mylist = ["Borderlands","League", "PathofElixe","Brawlhalla"]
print("My favourite games are", *mylist[0:4],sep=", ")
mylist.append("TF2")
print("Forgot to add this one too!")
print(*mylist[0:5],sep=", ")
mylist.remove("Borderlands")
print("Didn't really like this one actually")
print("Now this is my list of my favourite games",*mylist[0:4],sep=", ")
mylist.sort()
print("Lets sort this mess up!",*mylist[0:4],sep=", ")