
in_weight = input("Type your weight: ")
in_weight = float(in_weight)
lbs_kg = input("Convert in (L)bs or (K)g? ")
converted = 0

if lbs_kg.upper() == 'L':
    #Converet to Lbs
    converted = in_weight / 0.45
elif lbs_kg.upper() == 'K':
    #Convert to Kg
    converted = in_weight * 0.45
else:
    print("The chosen unit is not valid")

print(f"Conversion result: {converted} {lbs_kg}")