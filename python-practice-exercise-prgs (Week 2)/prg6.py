# Logging Function: Write a function log_message(message, level='INFO') that prints a log message. Set the level to default to 'INFO'. Demonstrate calling the function with and without the optional level argument.
def log_message(message, level='INFO'):
    print(f"[{level}] {message}")
log_message("System started")
log_message("An error occurred", level='ERROR')
