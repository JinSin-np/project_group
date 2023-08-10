from pathlib import Path
import cash_on_hand, overheads, profit_and_loss

# create a text file named as "summaryReport"
text_file = Path.cwd()/"summaryReport.txt"
# Checks if file exists
if text_file.exists() == False:
    # creates files if it doesnt exist
    text_file.touch()
with text_file.open(mode="w") as file:
    file.write(f"[HIGHEST OVERHEAD] {overheads.largest_overheads()[0]}: {overheads.largest_overheads()[1]}%")
    if cash_on_hand.print_cash_deficit()[0][1] > 0:
        file.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        file.write(f"\n[HIGHEST CASH SURPLUSH] DAY: {cash_on_hand.print_cash_deficit()[0]}, AMOUNT: USD{cash_on_hand.print_cash_deficit()[1]}")
    else:
        for day in cash_on_hand.print_cash_deficit():
            file.write(f"\n[CASH DEFICIT] DAY: {day[0]}, AMOUNT: USD{day[1] * -1}")
    if profit_and_loss.profit_deficit_calculator()[0][1] > 0:
        file.write("\n[PROFIT SURPLUS] PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        file.write(f"\n[HIGHEST PROFIT SURPLUSH] DAY: {profit_and_loss.profit_deficit_calculator()[0]}, AMOUNT: USD{profit_and_loss.profit_deficit_calculator()[1]}")
    else:
        for day in profit_and_loss.profit_deficit_calculator():
            file.write(f"\n[PROFIT DEFICIT] DAY: {day[0]}, AMOUNT: USD{day[1] * -1}")
