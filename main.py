# main.py

import argparse
import sys
import time
from analyzer import analyze_password
from generator import generate_wordlist

# 🔰 Banner and Author Info
def show_banner():
    banner = """

      _____         _____ _____ ______ ____  _____   _____ ______ 
 |  __ \ /\    / ____/ ____|  ____/ __ \|  __ \ / ____|  ____|
 | |__) /  \  | (___| (___ | |__ | |  | | |__) | |  __| |__   
 |  ___/ /\ \  \___ \\___ \|  __|| |  | |  _  /| | |_ |  __|  
 | |  / ____ \ ____) |___) | |   | |__| | | \ \| |__| | |____ 
 |_| /_/    \_\_____/_____/|_|    \____/|_|  \_\\_____|______|
                                                                  
            🔐 PassForge - Password Security Tool

Author     : Virendra Khunte  
GitHub     : https://github.com/0xV1RU  
LinkedIn   : https://linkedin.com/in/virendra-khunte-842273293
"""
    print(banner)

# 🔹 CLI Setup
def main():
    show_banner()

    parser = argparse.ArgumentParser(
        description="PassForge - Analyze passwords & generate wordlists securely"
    )
    #parser.add_argument("--analyze", action="store_true", help="Analyze password strength & check breaches")
    #parser.add_argument("--generate-wordlist", action="store_true", help="Generate custom password wordlist")
    parser.add_argument("--analyze", metavar="PASSWORD", type=str, help="Analyze password strength")
    parser.add_argument("--generate-wordlist", metavar="WORDS", type=str, help="Generate wordlist from keywords")
    

    args = parser.parse_args()

    if args.analyze:
        try:
            password = input("🔑 Enter a password to analyze: ")
            analyze_password(password)
            print("💡 Want to generate a custom wordlist too? Run: python main.py --generate-wordlist\n")
        except KeyboardInterrupt:
            print("\n❌ Operation cancelled.")
            sys.exit(1)

    elif args.generate_wordlist:
        try:
            #generate_wordlist()
            words = args.generate_wordlist.split()
            generate_wordlist(words)
            print("💡 Want to analyze a password? Run: python main.py --analyze\n")
        except KeyboardInterrupt:
            print("\n❌ Operation cancelled.")
            sys.exit(1)

    else:
        print("⚠️ Please use --analyze or --generate-wordlist option.\nExample: python main.py --analyze")

if __name__ == "__main__":
    main()
