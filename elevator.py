def elevator_simulator(requests):
    total_floors = 0
    current_floor = 0

    for next_floor in requests:
        if next_floor > current_floor:
            print(f"Elevator going up: from {current_floor} to {next_floor}")
            total_floors += next_floor - current_floor
        elif next_floor < current_floor:
            print(f"Elevator going down: from {current_floor} to {next_floor}")
            total_floors += current_floor - next_floor
        else:
            print(f"Elevator staying at floor {current_floor}")

        current_floor = next_floor  # update current position

    print(f"Total floors traveled: {total_floors}")
    print("Elevator simulation complete.")


request_test = [1, 3, 2, 5, 4, 6, 6, 3, 1]
elevator_simulator(request_test)

