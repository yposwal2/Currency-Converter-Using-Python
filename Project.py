def usdToPoundCal(dollar):
    return dollar * 0.83

def main():
    print("\n*****   USD $ to GBP £ calculator   *****\n")
    dollar = float(input("Enter Amount: $"))
    pounds = usdToPoundCal(dollar)
    print("$",dollar, " = £" ,pounds)

main()
