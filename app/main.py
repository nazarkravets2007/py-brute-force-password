import time
from hashlib import sha256


PASSWORDS = [
    ("02718281", "e5f3ff26aa8075ce7513552a9af1882b4fbc2a47a3525000f6eb887ab9622207"),
    ("16900355", "7e8f0ada0a03cbee48a0883d549967647b3fca6efeb0a149242f19e4b68d53d6"),
    ("18768206", "1273682fa19625ccedbe2de2817ba54dbb7894b7cefb08578826efad492f51c9"),
    ("29217843", "b4061a4bcfe1a2cbf78286f3fab2fb578266d1bd16c414c650c5ac04dfc696e1"),
    ("53853950", "4cd1a028a60f85a1b94f918adb7fb528d7429111c52bb2aa2874ed054a5584dd"),
    ("56515986", "40900aa1d900bee58178ae4a738c6952cb7b3467ce9fde0c3efa30a3bde1b5e2"),
    ("57236903", "5e6bc66ee1d2af7eb3aad546e9c0f79ab4b4ffb04a1bc425a80e6a4b0f055c2e"),
    ("64610856", "c15f56a2a392c950524f499093b78266427d21291b7d7f9d94a09b4e41d65628"),
    ("67154767", "cf0b0cfc90d8b4be14e00114827494ed5522e9aa1c7e6960515b58626cad0b44"),
    ("71120158", "e34efeb4b9538a949655b788dcb517f4a82e997e9e95271ecd392ac073fe216d"),
]


def sha256_hash_str(value: str) -> str:
    return sha256(value.encode("utf-8")).hexdigest()


def brute_force_password() -> None:
    for password, expected_hash in PASSWORDS:
        calculated_hash = sha256_hash_str(password)

        if calculated_hash == expected_hash:
            print(f"[OK] {password}")
        else:
            print(f"[FAIL] {password}")


if __name__ == "__main__":
    start_time = time.perf_counter()

    brute_force_password()

    end_time = time.perf_counter()
    print("Elapsed:", end_time - start_time)
