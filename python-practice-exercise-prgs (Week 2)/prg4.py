project_status = {'P101': 'In Progress', 'P102': 'Complete'}

print("Project IDs and values:", list(project_status.items()))

project_status['P101'] = 'On Hold'
print("Updated Project Status:", project_status)

status_P103 = project_status.get('P103', 'Not Found')
print("Status of P103:", status_P103)
