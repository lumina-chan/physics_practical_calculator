#ALERTS: min. 3 readings required,too much deviation means wrong observation, allobs/data have to be in same units
#IMP NOTES: make computer work, you only design code, follow abstraction
import math 

def main():
    print("MAIN MENU")
    while True :
        choices = [
            {"no.":"0.", "sub":"Exit"},
            {"no.":"1.", "sub":"External diameter"},
            {"no.":"2.", "sub":"Internal diameter + height"}
            ]
        for choice in choices:
            print(f"{choice["no."]:<4}{ choice["sub"]:<}")
        x = get_int("> ")
        match x :
            case 0:
                break
            case 1:
                vernier_callipers("External diameter")
            case 2:
                cylindrical_volume()

def get_int(prompt):
    while True:
        try :
            ask_user = int(input(prompt))
            if ask_user >= 0:
                break
            print("Strictly input a positive integer or zero.")
        except ValueError:
            print("Strictly input a positive integer or zero.")
    return ask_user

def get_float(prompt):
    while True:
        try:
            ask_user = float(input(prompt))
            if ask_user > 0:
                break
            print("Strictly input a positive number.")
        except ValueError:
            print("Strictly input a positive number.")        
    return ask_user

def info_vernier_callipers(prompt):
    print(f"\nVERNIER CALLIPERS: {prompt.upper()}")
    print("\nLeast count: 0.01 cm\n")
    print("Formula:\nVSR = VSD x Least Count")
    print("Observed value = MSR + VSR")
    print("\nALERT !\nMinimum observations: 3\nUnit: cm")
    print("-" * 60)

def cylindrical_volume():
    internal_diameter = vernier_callipers("Internal diameter")
    height = vernier_callipers("Depth")
    volume = (math.pi * (internal_diameter)**2 * height)/4
    print("\nV = (pi * D^2 * h )/ 4\n")
    print(f"VOLUME: {volume:.3f}")

def vernier_callipers(prompt):
    info_vernier_callipers(prompt)
    values = []
    zero_error_magnitude = 0
    least_count = 0.01 #cm

    while True:
        error = input("Zero error? (+/-/0) : ")
        if error == "0":
            break
        if error == "+" or error == "-" :
            vsd = get_int("Zero Error VSD: ")
            zero_error_magnitude = vsd * least_count
            break
        else:
            print("Choose Type of error: positive, negative, zero.\n")

    while True:
        try:
            n = int(input("No. of observations you will take? "))
            if n < 3:
                print("Minimum of 3 observations are required.\n")
                continue
        except ValueError:
            print("no.of observation is a digit.\n")
            continue
        for _ in range(n):
            print(f"\nObservation no: {(_ + 1)}")
            
            msr = get_float("MSR: ")
            vsd = get_int("VSD: ")
            
            vsr = vsd * least_count
            observed_value = round((msr + vsr), 4) 
            if error == "+":
                corrected_value = observed_value - zero_error_magnitude
            elif error == "-":
                corrected_value = observed_value + zero_error_magnitude
            else:
                corrected_value = observed_value
            ob = {"observation_no": (_ + 1),
                "msr": msr,
                "vsd": vsd,
                "vsr": vsr,
                "observed_value": observed_value,
                "corrected_value":corrected_value}
            values.append(ob)
        observation_table(values, prompt)
        value = avg(values)
        print(f"\n{prompt}: {round(value,2)} cm\n")
        break
    return value

def avg(values):
    mean = 0
    for ob in values:
        mean += ob["corrected_value"]
    return mean/len(values)

def observation_table(values, prompt):
    print(f"\nOBSERVATION TABLE: {prompt.upper()}")
    print("-" * 72)
    print(f"{"Obs no.":<12}{"MSR":<12}{"VSD":<12}{"VSR":<12}{"Observed":<12}{"Corrected":<12}")
    print("-" * 72)
    for ob in values:
        print(f"{ob["observation_no"]:<12}{ob["msr"]:<12}{ob["vsd"]:<12}{ob["vsr"]:<12}{ob["observed_value"]:<12}{ob["corrected_value"]:<12}")
    print("-" * 72)

if __name__ == "__main__":
    main()
