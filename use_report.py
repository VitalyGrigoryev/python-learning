import log_report

lines = log_report.read_logs("app.log")
counts = log_report.count_levels(lines)
print(counts)