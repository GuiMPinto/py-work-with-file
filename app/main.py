def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as file:
        total_supply = 0
        total_buy = 0
        result = 0   
        for line in file:
            if line.split(",")[0] == "supply":
                total_supply += line.split(",")[1]
            if line.split(",")[0] == "buy":
                total_buy += line.split(",")[1]
        result = total_supply - total_buy
    with open(report_file_name, "w") as report:
        report.write(f"supply,{total_supply}\n")
        report.write(f"buy,{total_buy}\n")
        report.write(f"result,{total_supply - total_buy}\n")
