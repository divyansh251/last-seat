bus=50
passenger=int(input("how many passsenger are waiting at bus station"))
left=0
while(True):
	if passenger>50:
		passenger=passenger-50
	elif passenger<50:
		left=50-passenger
		print("seat left in bus",end=":-")
		print(left)
		break
		
		