import json
import re
from collections import Counter

paths, ips, total = Counter(), set(), 0
with open("/app/access.log") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += 1
        ips.add(line.split()[0])
        m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
        if m:
            paths[m.group(1)] += 1

# Deterministic: highest count, ties broken lexicographically.
top_path = sorted(paths.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] if paths else ""

with open("/app/report.json", "w") as out:
    json.dump(
        {"total_requests": total, "unique_ips": len(ips), "top_path": top_path},
        out,
    )
