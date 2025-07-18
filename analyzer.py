# analyzer.py

from zxcvbn import zxcvbn
from breach_checker import check_password_breach

def analyze_password(password):
    print(f"\n🔍 Analyzing password: {password}\n")

    result = zxcvbn(password)
    score = result['score']
    crack_time = result['crack_times_display']['offline_fast_hashing_1e10_per_second']
    suggestions = result['feedback']['suggestions']

    strength = {
        0: "Very Weak 😣",
        1: "Weak 😟",
        2: "Medium 😐",
        3: "Strong 🙂",
        4: "Very Strong 💪"
    }

    print(f"🔐 Strength Score: {strength[score]}")
    print(f"⏱️ Estimated Crack Time: {crack_time}")

    if suggestions:
        print("💡 Suggestions:")
        for s in suggestions:
            print(f"  - {s}")
    else:
        print("✅ Great! No improvement suggestions.\n")

    print("\n🌐 Checking for password breaches...")
    count = check_password_breach(password)
    if count:
        print(f"⚠️ Found in {count} known data breaches!")
    else:
        print("✅ Good news! This password has NOT been found in public breaches.")
