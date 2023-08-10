from pathlib import Path
import cash_on_hand, overheads, profit_and_loss

# create a text file named as "summaryReport"
text_file = Path.cwd()/"summaryReport.txt"
# Checks if file exists
if text_file.exists() == False:
    # creates files if it doesnt exist
    text_file.touch()
# open tect file to write
with text_file.open(mode="w") as file:
    # writes the highest overhead and its percentage
    file.write(f"[HIGHEST OVERHEAD] {overheads.largest_overheads()[0]}: {overheads.largest_overheads()[1]}%")
    # Checks if cash on hand is in surplus
    if cash_on_hand.print_cash_deficit()[0][1] > 0:
        # writes day with the highest cash surplus and the amount
        file.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        file.write(f"\n[HIGHEST CASH SURPLUSH] DAY: {cash_on_hand.print_cash_deficit()[0]}, AMOUNT: USD{cash_on_hand.print_cash_deficit()[1]}")
    else:
        # writes the days with cash deficit and the amount
        for day in cash_on_hand.print_cash_deficit():
            file.write(f"\n[CASH DEFICIT] DAY: {day[0]}, AMOUNT: USD{day[1] * -1}")
    # checks if profit is in surplus
    if profit_and_loss.profit_deficit_calculator()[0][1] > 0:
        # writes day with the highest profit surplus and the amount
        file.write("\n[PROFIT SURPLUS] PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        file.write(f"\n[HIGHEST PROFIT SURPLUSH] DAY: {profit_and_loss.profit_deficit_calculator()[0]}, AMOUNT: USD{profit_and_loss.profit_deficit_calculator()[1]}")
    else:
        # writes the days with cash deficit
        for day in profit_and_loss.profit_deficit_calculator():
            file.write(f"\n[PROFIT DEFICIT] DAY: {day[0]}, AMOUNT: USD{day[1] * -1}")
