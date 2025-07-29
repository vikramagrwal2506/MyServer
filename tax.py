#Australia Income Tax calculator
Annual_Income = (input("Annual_Income ="))
AI=int(Annual_Income)
X=(AI-18200)*(.16)
X1=(AI-45000)*(.30) + 4288
X2=(AI-135000)*(.37) + 31288
X3=(AI-190000)*(.45) + 51638
if AI <= 18200:
    print("Total Tax will be 0")
    print("There will be no Medicare cost for the income mentioned.")
elif AI<=45000:
    print ("Total Tax will be", X)
    print("There will be no Medicare cost for the income mentioned.")
elif AI<=135000:
    print ("Tax will be", X1)
elif AI<=190000:
    print ("Tax will be", X2)
elif AI>190000:
    print ("Tax will be", X3)
else:
    print("ERROR")
