module_A_reports = (101, 205, 300, 410)
module_B_reports = (300, 550, 205, 712, 101)

module_A = set(module_A_reports)
module_B = set(module_B_reports)

unique_error_codes = module_A.union(module_B)
print("Unique error codes reported by either module:", unique_error_codes)

common_error_codes = module_A.intersection(module_B)
print("Error codes reported by both modules:", common_error_codes)