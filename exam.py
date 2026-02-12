def make_change(cost, paid):
    denominations = [20, 10, 5, 2, 1]
    change = paid - cost

    if change < 0:
        print(f"Insurfficient amount paid.")
        return

    print(f"total change: ${change}")

    for bill in denominations:
        bill_count = change // bill
        if bill_count > 0:
            print(f"${bill} bills: {bill_count}")
            change -= bill_count * bill

    if change > 0:
        print(f"Remaining change: ${change}")

make_change(47, 100)
