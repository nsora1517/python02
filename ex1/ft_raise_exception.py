#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    itemp = int(temp_str)
    if itemp > 40:
        raise ValueError(f"{itemp}°C is too hot for plants (max 40°C)")
    if itemp < 0:
        raise ValueError(f"{itemp}°C is too cold for plants (min 0°C)")
    return itemp


def test_temperature() -> None:
    for temp_str in ['25', 'abc', '100', '-50']:
        try:
            temp = input_temperature(temp_str)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        print("")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
    print("All tests completed - program didn't crash!")
