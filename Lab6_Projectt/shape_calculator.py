import geometry_utils


def main():
    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: _area, _perimeter (e.g., circle_area)")

    # Hesaplamaları eşleştirmek için sözlük yapısı
    calc_map = {
        "circle_area": geometry_utils.circle_area,
        "circle_perimeter": geometry_utils.circle_perimeter,
        "rectangle_area": geometry_utils.rectangle_area,
        "rectangle_perimeter": geometry_utils.rectangle_perimeter,
        "triangle_area": geometry_utils.triangle_area
    }

    choice = input("Enter the operation you want to perform: ").lower().strip()

    if choice not in calc_map:
        print("Invalid choice!")
        return

    try:
        if "circle" in choice:
            r = float(input("Enter radius: "))
            res = calc_map[choice](r)
        elif "rectangle" in choice:
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            res = calc_map[choice](w, h)
        elif "triangle" in choice:
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            res = calc_map[choice](b, h)

        print(f"Result: {res:.2f}")

    except ValueError as err:
        if "strictly positive" in str(err):
            print(f"Input Error: {err}")
        else:
            print("Input Error: Please make sure you only enter numbers.")


if __name__ == "__main__":
    main()