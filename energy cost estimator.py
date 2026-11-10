# Workshop Energy Cost Estimator
# Calculates daily and monthly energy use (kWh) and cost for workshop machines.
# Own twist: finds the most energy-hungry machine and shows the money saved
# if it ran 1 hour less per day.

DAYS_IN_MONTH = 30  


def get_number(prompt, minimum, maximum=None, whole=False):
    while True:
        text = input(prompt).strip()
        try:
            value = int(text) if whole else float(text)
        except ValueError:
            print("  Invalid input. Please type a number (e.g. 5 or 2.5).")
            continue
        if value < minimum:
            print(f"  The number must be at least {minimum}.")
        elif maximum is not None and value > maximum:
            print(f"  The number must not be more than {maximum}.")
        else:
            return value


def get_name(prompt):
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("  The name cannot be empty.")


def daily_kwh(power_watts, hours):
    return power_watts * hours / 1000


def usage_level(monthly_kwh):
    if monthly_kwh < 100:
        return "LOW usage"
    elif monthly_kwh < 500:
        return "MODERATE usage"
    else:
        return "HIGH usage - look for ways to save energy"


def main():
    print("=== Workshop Energy Cost Estimator ===\n")

    count = get_number("How many machines do you have? ", 1, whole=True)
    tariff = get_number("Enter your tariff (cost per kWh, e.g. 209.5): ", 0)

    machines = [] 


    for i in range(1, count + 1):
        print(f"\nMachine {i} of {count}")
        name = get_name("  Name: ")
        watts = get_number("  Power in watts: ", 1)
        hours = get_number("  Hours used per day (0 to 24): ", 0, 24)
        kwh = daily_kwh(watts, hours)
        machines.append({"name": name, "watts": watts, "hours": hours, "daily": kwh})



    print("\n" + "=" * 62)
    print(f"{'Machine':<18}{'Daily kWh':>12}{'Monthly kWh':>14}{'Monthly cost':>16}")
    print("-" * 62)

    total_daily = 0
    for m in machines:
        monthly = m["daily"] * DAYS_IN_MONTH
        cost = monthly * tariff
        total_daily += m["daily"]
        print(f"{m['name']:<18}{m['daily']:>12.2f}{monthly:>14.2f}{cost:>16.2f}")

    total_monthly = total_daily * DAYS_IN_MONTH
    total_cost = total_monthly * tariff
    print("-" * 62)
    print(f"{'TOTAL':<18}{total_daily:>12.2f}{total_monthly:>14.2f}{total_cost:>16.2f}")
    print("=" * 62)
    print(f"Daily cost: {total_daily * tariff:.2f}")
    print(f"Workshop rating: {usage_level(total_monthly)}")

    
    biggest = machines[0]
    for m in machines:
        if m["daily"] > biggest["daily"]:
            biggest = m

    if biggest["daily"] == 0:
        print("\nNo machine is in use, so there is nothing to save.")
    else:
        hours_cut = min(1, biggest["hours"])
        saved_kwh = daily_kwh(biggest["watts"], hours_cut) * DAYS_IN_MONTH
        print(f"\nBiggest energy user: {biggest['name']}")
        print(f"If it runs {hours_cut:g} hour less per day, you save "
              f"{saved_kwh:.2f} kWh and {saved_kwh * tariff:.2f} per month.")


main()
