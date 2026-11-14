class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("That chai is not available")

        # check cups instance or type as integer
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")

        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai rupees {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visting chaicode! \n\n")


bill("mint", 2)
bill("masala", "Three")
bill("ginger", "two")
bill("masala", 2)
bill("ginger", 4)
