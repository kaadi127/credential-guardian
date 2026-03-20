import customtkinter as ctk
from tkinter import messagebox

# UI එකේ පෙනුම සැකසීම (Dark Mode)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CredentialGuardian(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Credential Guardian v1.0")
        self.geometry("500x400")

        # --- Title Section ---
        self.title_label = ctk.CTkLabel(self, text="🛡️ CREDENTIAL GUARDIAN", 
                                        font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=(30, 10))

        self.subtitle_label = ctk.CTkLabel(self, text="Advanced Phishing Link Analyzer", 
                                           font=ctk.CTkFont(size=14))
        self.subtitle_label.pack(pady=(0, 20))

        # --- Input Section ---
        self.entry = ctk.CTkEntry(self, placeholder_text="Paste URL here (e.g., https://secure-login.com)", 
                                  width=400, height=40)
        self.entry.pack(pady=10)

        # --- Button Section ---
        self.scan_button = ctk.CTkButton(self, text="SCAN URL", 
                                         font=ctk.CTkFont(size=15, weight="bold"),
                                         fg_color="#1f538d", hover_color="#14375e",
                                         height=45, command=self.run_check)
        self.scan_button.pack(pady=20)

        # --- Result Section ---
        self.result_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.result_frame.pack(pady=10, fill="x", padx=50)

        self.score_label = ctk.CTkLabel(self.result_frame, text="Risk Score: --", 
                                        font=ctk.CTkFont(size=18, weight="bold"))
        self.score_label.pack()

        self.status_label = ctk.CTkLabel(self.result_frame, text="Status: Waiting for input...", 
                                         font=ctk.CTkFont(size=14))
        self.status_label.pack(pady=5)

    def analyze_url(self, url):
        risk_score = 0
        if not url.startswith("https"): risk_score += 40
        
        suspicious_words = ['login', 'verify', 'bank', 'secure', 'update', 'account', 'paypal']
        for word in suspicious_words:
            if word in url.lower(): risk_score += 20
            
        if "@" in url: risk_score += 30
        if url.count('.') > 3: risk_score += 15
        
        return min(risk_score, 100)

    def run_check(self):
        url = self.entry.get().strip()
        
        if not url:
            messagebox.showwarning("Empty Input", "Please enter a URL to scan!")
            return

        score = self.analyze_url(url)
        
        # UI එක update කිරීම
        self.score_label.configure(text=f"Risk Score: {score}/100")
        
        if score >= 70:
            self.status_label.configure(text="STATUS: DANGEROUS ❌", text_color="#ff4b4b")
            self.score_label.configure(text_color="#ff4b4b")
        elif score >= 40:
            self.status_label.configure(text="STATUS: CAUTION ⚠️", text_color="#ffa500")
            self.score_label.configure(text_color="#ffa500")
        else:
            self.status_label.configure(text="STATUS: SAFE ✅", text_color="#2ecc71")
            self.score_label.configure(text_color="#2ecc71")

if __name__ == "__main__":
    app = CredentialGuardian()
    app.mainloop()