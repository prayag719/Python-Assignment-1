def convert_temp(celsius , fahrenheit):
    fah = (celsius * 1.8) + 32
    cel = (fahrenheit - 32) * 5/9
    print(f"{celsius} °C  = {fah} °F")
    print(f"{fahrenheit} °F  = {cel} °C")

convert_temp(80,120)

