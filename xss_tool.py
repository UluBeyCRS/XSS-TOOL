#!/usr/bin/env python3
import os
import time
import requests
from datetime import datetime
import urllib.parse

# ====================== LULU XSS TOOL v2026 - Kali Edition ======================

print("\033[91m" + """
    ╔══════════════════════════════════════════════╗
    ║          LULU XSS ATTACK TOOL v2026          ║
    ║         OTOMATİK TARAMA + KALICI XSS         ║
    ║                 KALI LINUX                   ║
    ╚══════════════════════════════════════════════╝
    \033[0m""")

def temizle():
    os.system('clear')  # Kali için cls yerine clear

def menu():
    print("\n\033[93mXSS Tool Menü:\033[0m")
    print("  1. Site XSS Açığı Taraması")
    print("  2. Kalıcı XSS Saldırısı (Payload Enjeksiyonu)")
    print("  0. Çıkış\n")

# xss_tara ve kalici_xss_saldirisi fonksiyonları aynı kalıyor...
# (Kodu buraya tam olarak kopyala, sadece temizle() fonksiyonunu değiştir)

def main():
    while True:
        temizle()
        menu()
        secim = input("\033[97mSeçenek gir (1/2/0) > \033[0m").strip()
        
        if secim == "0":
            print("\033[91mTool kapatılıyor...\033[0m")
            break
        elif secim == "1":
            url = input("\033[97mTaranacak site URL'sini gir[](https://...) > \033[0m").strip()
            if url:
                xss_tara(url)
        elif secim == "2":
            url = input("\033[97mSaldırı yapılacak site URL'sini gir[](https://...) > \033[0m").strip()
            if not url:
                continue
            payload = input("\033[96mPayload > \033[0m").strip()
            if payload:
                kalici_xss_saldirisi(url, payload)
        else:
            print("\033[93mGeçersiz seçim!\033[0m")
        
        input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    print("\033[92mLULU XSS TOOL v2026 Kali başlatılıyor...\033[0m")
    time.sleep(1)
    main()