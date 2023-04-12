feet_inches= input("What is your height in feet and inches?:")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet":feet, "inches":inches}

def convertor(x,y):
    meters =x * 0.3048 + y * 0.0254
    return meters
parsed = parse (feet_inches)
result = convertor(parsed["feet"], parsed["inches"])
print(result)
if result < 1.65:
    print("kid is too small")
else:
    print("Kid can ride")




