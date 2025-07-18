# 🔐 PassForge — Password Security Toolkit
***PassForge*** - A password strength analyzer and custom wordlist generator. *PassForge* is a powerful and flexible Python-based command-line tool to:
- ✅ Analyze password strength using zxcvbn entropy logic  
- 🚨 Check if a password has been leaked in known data breaches (via HaveIBeenPwned API)  
- 🧰 Generate advanced wordlists using custom keywords for CTFs or penetration testing  

---

## 📌 Features

- Analyze any password and rate its strength (score 0–4)
- Check real-time password breaches from HIBP (without sending full password)
- Generate advanced, mutated wordlists using:
  - Capitalization
  - Leetspeak (e.g. `a → @`, `i → 1`)
  - Years, numbers, special symbols
  - Reversal & combination
- Save wordlist as `wordlist.txt`
- Easy CLI usage with helpful tips and banner
- Clean, modular code for easy extension

---
## Requirements
You need Python 3 to run PassForge.

## ⚙️ Usage

### 🔍 Analyze a Password
```bash
python main.py --analyze "Enter Your Passwd Here"
```
#### ✅ Output:
- Crack time (online + offline)
- Suggestions to improve
- Breach check result (via HaveIBeenPwned)

### 🧪Generate a Custom Wordlist
```bash
python main.py --generate-wordlist "Enter words for wordlist"
```
- wordlist saved on wordlist.txt file.

## ⚠️ Disclaimer
 > *This tool is created for educational & ethical hacking purposes only. Never use against unauthorized systems.*
