import random
import time

log_levels = ["INFO", "WARN", "ERROR"]
log_messages = [
    "User login successful",
    "User login failed",
    "File not found",
    "Database connection established",
    "Database connection lost",
    "Server started",
    "Server shutdown"
]

def generate_log():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    level = random.choice(log_levels)
    message = random.choice(log_messages)
    log_line = f"{timestamp} {level} {message}"
    return log_line

with open("logs.txt", "a") as f:
    for _ in range(100):
        log_line = generate_log()
        f.write(log_line + "\n")
        time.sleep(0.1)
