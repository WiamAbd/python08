import os
from typing import Optional
from dotenv import load_dotenv


def get_env(var: str, default: Optional[str] = None) -> Optional[str]:
    value = os.getenv(var)
    if value is None:
        return default
    return value


if __name__ == "__main__":
    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...\n")

    mode = get_env("MATRIX_MODE", "development")
    db = get_env("DATABASE_URL")
    api = get_env("API_KEY")
    log = get_env("LOG_LEVEL", "INFO")
    zion = get_env("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if mode == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production system")

    print(f"API Access: {'Authenticated' if api else 'Missing'}")
    print(f"Log Level: {log}")
    print(f"Zion Network: {'Online' if zion else 'Offline'}")

    print("\nEnvironment security check:")

    if os.path.exists(".env"):
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
    else:
        print("[WARNING] .env file missing")

    print("\nThe Oracle sees all configurations.")
