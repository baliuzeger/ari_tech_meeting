from dotenv import dotenv_values

config = dotenv_values(".env")

print(f"User name: {config['USERNAME']}, PASSWORD: {config['PASSWORD']}")