#!/usr/bin/python1.7
#Plot graph based on data in csv file - Expense tracking
import matplotlib.pyplot as plt

colors = ['yellowgreen','gold','lightskyblue','red','green','lightcoral','coral', 'blue', 'pink','violet','black','white']
cls = []
sizes = []
explode = []
total = 0
labels=()
lbls=[]

grocery = ['TARGET', 'COSTCO', 'COCONUT','SAFEWAY', 'TMOWALMART', 'INDIA', 'WHOLEFDS', '7-ELEVEN']
restaurants = ['MCDONALD\'S','MCAFEE','COLDSTONE', 'NEW', 'EL']
dress = ['GYMBOREE', 'OSH']
car = ['HONDA']

def set_color(indx):
	if indx >= len(colors):
		return colors[len(colors) % indx]
	else:
		return colors[indx]



category={}
fl = open("dat.csv")

buff = fl.readline()
i = 0

while buff.strip() != "":
	data = buff.split(",")
	(desc, amount) = (data[3],(float(data[2])))
	print "%s : %d\n" % (desc,amount)
	total = total + amount 
	shop = desc.split(" ")[0]
	shop = shop.replace('\"','')
	print "Shop: %s\n"%shop
	if shop in grocery:
		shop = 'GROCERY'
	elif shop in restaurants:
		shop = 'RESTAURANT'
	elif shop in dress:
		shop = 'DRESS'
	
	if(category.has_key(shop)):
		category[shop] = category[shop] + abs(amount)
	else:
		category[shop] = abs(amount)
	buff = fl.readline()
chk=0
for key in category.keys():
#	sizes.append( category[key] * 100/total)
	sizes.append(category[key])
	colors.append(set_color(i))
	explode.append( 0)
	i = i + 1
	lbls.append( key) 
	chk = 1
	print "%s : %d\n" % (key, category[key])

lables = lbls
#print "labels: %s\n"%(labels)
print "Total : %d\n" % abs(total)
print "sz: %d szexp: %d lables: %d\n"%(len(sizes),len(explode),len(lables))
plt.pie(sizes, explode=explode, labels=lables, autopct='%1.1f%%', shadow=True, startangle=90)
print "After pie"
plt.axis('equal')
plt.show()

