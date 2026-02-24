import time
from hashlib import sha256

# Список хешів, які потрібно знайти (беремо саме значення хешів)
TARGET_HASHES = {
    "e5f3ff26aa8075ce7513552a9af1882b4fbc2a47a3525000f6eb887ab9622207",
    "7e8f0ada0a03cbee48a0883d549967647b3fca6efeb0a149242f19e4b68d53d6",
    "1273682fa19625ccedbe2de2817ba54dbb7894b7cefb08578826efad492f51c9",
    "b4061a4bcfe1a2cbf78286f3fab2fb578266d1bd16c414c650c5ac04dfc696e1",
    "4cd1a028a60f85a1b94f918adb7fb528d7429111c52bb2aa2874ed054a5584dd",
    "40900aa1d900bee58178ae4a738c6952cb7b3467ce9fde0c3efa30a3bde1b5e2",
    "5e6bc66ee1d2af7eb3aad546e9c0f79ab4b4ffb04a1bc425a80e6a4b0f055c2e",
    "c15f56a2a392c950524f499093b78266427d21291b7d7f9d94a09b4e41d65628",
    "cf0b0cfc90d8b4be14e00114827494ed5522e9aa1c7e6960515b58626cad0b44",
    "e34efeb4b9538a949655b788dcb517f4a82e997e9e95271ecd392ac073fe216d",
}

# для швидкого пошуку та видалення знайдених
remaining = TARGET_HASHES.copy()
found = {}  # hash → password

start_time = time.perf_counter()

print("Початок brute-force пошуку 8-значних паролів...")
print("Це може зайняти від 3 до 15 хвилин залежно від комп'ютера\n")

for i in range(100_000_000):
    # два найпоширеніших і швидких способи форматування
    password = f"{i:08d}"                    # варіант 1 (сучасний, зручний)
    # password = str(i).zfill(8)             # варіант 2 (рекомендує рев'ювер)

    hash_value = sha256(password.encode("utf-8")).hexdigest()

    if hash_value in remaining:
        found[hash_value] = password
        remaining.discard(hash_value)
        print(f"ЗНАЙДЕНО → {password}   (хеш: {hash_value})")
        
        if not remaining:
            break

end_time = time.perf_counter()
elapsed = end_time - start_time

print("\n" + "═" * 70)
print(f"Завершено. Знайдено {len(found)} з 10 паролів")
print(f"Час виконання: {elapsed:.1f} секунд  (~ {elapsed/60:.1f} хвилин)")
print("Знайдені паролі (відсортовані за значенням):")

for pwd in sorted(found.values()):
    h = [k for k, v in found.items() if v == pwd][0]
    print(f"  {pwd}  →  {h}")
