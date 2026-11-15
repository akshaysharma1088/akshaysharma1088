import json
import os
import urllib.request

PACKAGES = ["dataranger", "pipeverify"]
PEPY_API_KEY = os.environ.get("PEPY_API_KEY", "")

def fetch_downloads(pkg: str) -> int:
    # Uses PePy v2 API (if key provided) with fallback to PyPI Stats API (180-day window)
    if PEPY_API_KEY:
        req = urllib.request.Request(
            f"https://api.pepy.tech/api/v2/projects/{pkg}",
            headers={"X-Api-Key": PEPY_API_KEY, "User-Agent": "GitHub-Actions-Stats"}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            return int(data.get("total_downloads", 0))
    else:
        req = urllib.request.Request(
            f"https://pypistats.org/api/packages/{pkg}/overall?mirrors=true",
            headers={"User-Agent": "GitHub-Actions-Stats"}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            return sum(row["downloads"] for row in data.get("data", []))

def format_number(num: int) -> str:
    if num >= 1_000_000:
        return f"{num / 1_000_000:.1f}M"
    if num >= 1_000:
        return f"{num / 1_000:.1f}k"
    return str(num)

def main():
    os.makedirs("stats", exist_ok=True)
    counts = {pkg: fetch_downloads(pkg) for pkg in PACKAGES}
    total = sum(counts.values())

    # 1. Shields.io Endpoint Schema for Combined Badge
    badge_payload = {
        "schemaVersion": 1,
        "label": "Ecosystem Downloads (pipeverify + dataranger)",
        "message": f"{format_number(total)} ({total:,})",
        "color": "007EC6",
        "namedLogo": "pypi",
        "logoColor": "white"
    }
    with open("stats/ecosystem_badge.json", "w") as f:
        json.dump(badge_payload, f, indent=2)

    # 2. Detailed JSON for akshaysharma1088.github.io Bento Card
    portfolio_payload = {
        "total_downloads": total,
        "total_formatted": format_number(total),
        "packages": counts
    }
    with open("stats/ecosystem_metrics.json", "w") as f:
        json.dump(portfolio_payload, f, indent=2)

if __name__ == "__main__":
    main()
