#ALERTS: min. 3 readings required,too much deviation means wrong observation, allobs/data have to be in same units
#IMP NOTES: make computer work, you only design code, follow abstraction
def main():
    vernier_callipers()

def vernier_callipers():
    #default zero error is zero
    info()
    values = []
    zero_error = 0
    least_count = 0.01 #cm
    while True:
        try:
            error = ask("Zero error? (+/-/0) : ")
        except TypeError:
            pass
        else:
            if error == "+" or error == "-" or error == "0":
                try:
                    vsd = int(ask("Zero Error VSD: "))
                    if vsd < 0:
                        print("VSD is strictly a positive integer or zero.\n")
                        continue
                except ValueError:
                    print("VSD is strictly a positive integer or zero..\n")
                else:
                    zero_error = vsd * least_count
                    break
            else:
                print("Choose Type of error: positive, negative, zero.\n")
    while True:
        try:
            n = int(ask("No. of observations you will take? "))
            if n < 3:
                print("Minimum of 3 observations are required.\n")
                continue
        except ValueError:
            print("no.of observation is a digit.\n")
            continue
        for _ in range(n):
            print(f"\nObservation no: {(_ + 1)}")
            while True:
                try:
                    msr = float(ask("MSR: "))
                    vsd = int(ask("VSD: "))
                    if msr <= 0 or vsd < 0:
                        print("MSR can be positive value with digits after decimal points.\nVSD is strictly a positive integer or zero.\n")
                        continue
                except ValueError:
                    print("MSR can be positive value with digits after decimal points.\nVSD is strictly a positive integer or zero..\n")
                else:
                    break
            vsr = vsd * least_count
            ob_ext_diameter = round((msr + vsr), 4) #corrected diameter = observed diameter
            if error == "+":
                cr_ext_diameter = ob_ext_diameter - zero_error
            elif error == "-":
                cr_ext_diameter = ob_ext_diameter + zero_error
            else:
                cr_ext_diameter = ob_ext_diameter
            ob = {"observation_no": (_ + 1),
                "msr": msr,
                "vsd": vsd,
                "vsr": vsr,
                "observed_diameter": ob_ext_diameter,
                "corrected_diameter":cr_ext_diameter}
            values.append(ob)
        observation_table(values)
        diameter = avg(values)
        print(f"\nDiameter: {round(diameter,2)} cm\n")
        break

def info():
    print("\nVERNIER CALLIPERS: External Diameter")
    print("\nLeast count: 0.01 cm\n")
    print("Formula:\nVSR = VSD x Least Count")
    print("Observed diameter = MSR + VSR")
    print("\nALERT !\nMinimum observations: 3\nUnit: cm")
    print("-" * 60)

def ask(prompt):
    return input(prompt)

def avg(values):
    mean = 0
    for ob in values:
        mean += ob["corrected_diameter"]
    return mean/len(values)

def observation_table(values):
    print("\nOBSERVATION TABLE")
    print("-" * 60)
    print(f"{"Obs no.":<12}{"MSR":<12}{"VSD":<12}{"VSR":<12}{"Obs diameter":<12}{"Crr diameter":<12}")
    print("-" * 60)
    for ob in values:
        print(f"{ob["observation_no"]:<12}{ob["msr"]:<12}{ob["vsd"]:<12}{ob["vsr"]:<12}{ob["observed_diameter"]:<12}{ob["corrected_diameter"]:<12}")
    print("-" * 60)

main()
