import re
from colorama import Fore, Style, init

# Initialize color formatting for the terminal
init(autoreset=True)

def analyze_url(url):
    risk_score = 0
    reasons = []

    # 1. Check for HTTPS (Higher risk if missing)
    if not url.startswith("https"):
        risk_score += 40
        reasons.append("Missing HTTPS encryption")

    # 2. Check for suspicious keywords
    suspicious_words = ['login', 'verify', 'bank', 'secure', 'update', 'account', 'paypal', 'facebook']
    for word in suspicious_words:
        if word in url.lower():
            risk_score += 20
            reasons.append(f"Contains suspicious keyword: {word}")

    # 3. Check for '@' symbol (Commonly used in phishing to hide real domains)
    if "@" in url:
        risk_score += 30
        reasons.append("URL contains '@' symbol (potentially fraudulent)")

    # 4. Check for shortened links
    shorteners = ['bit.ly', 't.co', 'tinyurl']
    if any(s in url for s in shorteners):
        risk_score += 25
        reasons.append("This is a shortened link (hides the real destination)")

    return min(risk_score, 100), reasons

def main():
    print(f"{Fore.CYAN}--- Credential Guardian: Phishing Checker ---{Style.RESET_ALL}")
    link = input("Enter the URL to analyze: ").strip()

    score, findings = analyze_url(link)

    print(f"\nAnalysis for: {link}")
    print(f"Risk Score: {score}/100")

    # Displaying the results based on score
    if score >= 70:
        print(f"{Fore.RED}STATUS: HIGHLY DANGEROUS! Do not enter any credentials.")
    elif score >= 40:
        print(f"{Fore.YELLOW}STATUS: CAUTION. This link is suspicious.")
    else:
        print(f"{Fore.GREEN}STATUS: LIKELY SAFE.")

    if findings:
        print("\nFlagged Issues:")
        for issue in findings:
            print(f"- {issue}")

if __name__ == "__main__":
    main()