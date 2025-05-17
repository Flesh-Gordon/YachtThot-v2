from flask import Flask, request, abort
import subprocess
import requests
import ipaddress

app = Flask(__name__)

# Load GitHub's official webhook IP ranges
GITHUB_HOOK_IP_RANGES = requests.get("https://api.github.com/meta").json()["hooks"]
GITHUB_HOOK_NETWORKS = [ipaddress.ip_network(ip) for ip in GITHUB_HOOK_IP_RANGES]

def is_github_ip(ip):
    ip_obj = ipaddress.ip_address(ip)
    return any(ip_obj in net for net in GITHUB_HOOK_NETWORKS)

@app.route("/webhook", methods=["POST"])
def webhook():
    remote_ip = request.remote_addr
    if not is_github_ip(remote_ip):
        print(f"[SECURITY] Blocked unauthorized IP: {remote_ip}")
        abort(403)

    subprocess.Popen(["/bin/bash", "/home/thefleshgordon/deploy-hook.sh"])
    print(f"[WEBHOOK] Triggered from {remote_ip}")
    return "Webhook received and deploy triggered.", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)