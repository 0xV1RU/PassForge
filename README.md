# 🔐 PassForge — Password Security Toolkit
***PassForge*** - *PassForge* is a powerful and flexible Python-based command-line tool to:
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
#### 1) Clone the Repository from GitHub
```bash
sudo git clone https://github.com/0xV1RU/PassForge.git.
cd PassForge
```
#### 2) Create Virtual Environment (Optional but Recommended) 
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate   # Linux/Mac
```
#### 3) Install Required Dependencies
```bash
pip install -r requirements.txt
```
#### 4) Run the Tool from *`main.py`*
#### 🔍 Analyze a Password
```bash
python main.py --analyze "Enter Your Passwd Here"
```
#### ✅ Output:
- Crack time (online + offline)
- Suggestions to improve
- Breach check result (via HaveIBeenPwned)

#### 🧪Generate a Custom Wordlist
```bash
python main.py --generate-wordlist "Enter words for wordlist"
```
- Variations of your input saved in `wordlist.txt`
- Includes:
  - Capitalization
  - Reversals
  - Leetspeak (`a→@`, `i→1`)
  - Numbers/symbols
  - Year suffix (`2024`, `@123`, `etc.`)

## ⚠️ Disclaimer
 > *This tool is created for educational & ethical hacking purposes only. Never use against unauthorized systems.*
