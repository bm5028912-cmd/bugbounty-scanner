import requests, re
from urllib.parse import urljoin

target = input("Target URL (e.g. https://example.com): ")
print(f"[*] Scanning {target}")

try:
    html = requests.get(target, timeout=10).text
    js_files = re.findall(r'src=["\'](.*?.js)["\']', html)
    print(f"[+] Found {len(js_files)} JS files")

    for js_path in js_files[:10]:
        full_url = urljoin(target, js_path)
        print(f"\n--- Checking {full_url} ---")
        try:
            js_code = requests.get(full_url, timeout=10).text
            if "slice" in js_code or "postMessage" in js_code:
                print("[!!!] Potential vuln - review file")
            if "location" in js_code and "search" in js_code:
                print("[!] URL manipulation found")
        except:
            pass
    print("\n[Done] Scan finished")
except Exception as e:
    print(f"Error: {e}")
