from dotenv import load_dotenv
import os

load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

print(f"User name: {USERNAME}, PASSWORD: {PASSWORD}")

STORE_DIR = os.getenv('STORE_DIR', '.')
print(f"STORE_DIR: {STORE_DIR}")

DEV = os.getenv('DEV', 'False').lower() in ('true', '1', 't')
if DEV:
    print("In dev environment.")
else:
    print("In production environment.")