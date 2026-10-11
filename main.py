# Variables
hourly_rate = 100
vat_rate = 1.23
big_discount = 0.30
medium_discount = 0.20
small_discount = 0.10

# Main Menu Loop
while True:
    # Showing Menu
    print("\n--- MAIN MENU ---")
    print("1. Add Order")
    print("2. Close App")

    try:
        choice = int(input("Choose option: "))

        # Managing choosen option
        if choice == 1:
            # Inputs
            while True:
                try:
                    car_part_price = int(input("Input car part price: "))
                    if car_part_price > 0:
                        break
                    else:
                        print("Input proper Value")
                except ValueError:
                    print("Input proper value")

            while True:
                try:
                    car_part_replace_time = int(input("Input car part replace time: "))
                    if car_part_replace_time > 0:
                        break
                    else:
                        print("Input proper Value")
                except ValueError:
                    print("Input proper value")

            while True:
                try:
                    car_value = int(input("Input car value: "))
                    if car_value > 0:
                        break
                    else:
                        print("Input proper Value")
                except ValueError:
                    print("Input proper value")
            
            repair_value = (car_part_price+(car_part_replace_time*hourly_rate))
            final_repair_value = None

            # Logic and discounts
            if repair_value > 5000:
                final_repair_value = repair_value-(repair_value*big_discount)
            elif (repair_value < 5000) and (repair_value > 2000):
                final_repair_value = repair_value-(repair_value*medium_discount)
            elif (repair_value < 2000) and (repair_value > 1000):
                final_repair_value = repair_value-(repair_value*small_discount)
            else:
                final_repair_value = repair_value

            # Return message
            print("Total price: ", final_repair_value*vat_rate, "PLN")

            if final_repair_value*vat_rate > (car_value/2):
                print("Repair is not recommended, price is at least half the value of the car")

        elif choice == 2:
            break
        else:
            print("You need to choose proper option")

    except ValueError:
        print("Input proper value")