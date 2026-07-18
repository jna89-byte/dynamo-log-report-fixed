import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load():
    assert REPORT.exists(), "no /app/report.json found"
    return json.loads(REPORT.read_text())


def test_report_has_exactly_the_three_keys():
    """Checks the output shape stated at the top of instruction.md: /app/report.json holds
    one JSON object with exactly total_requests, unique_ips, and top_path and nothing else."""
    data = _load()
    assert isinstance(data, dict), "report.json must hold a JSON object"
    assert set(data) == {"total_requests", "unique_ips", "top_path"}, (
        f"expected exactly total_requests, unique_ips, top_path; got {sorted(data)}"
    )


def test_total_requests():
    """Checks instruction.md criterion 1: total_requests is how many non-empty lines are
    in /app/access.log."""
    data = _load()
    assert data["total_requests"] == 5, f"expected 5, got {data['total_requests']!r}"


def test_unique_ips():
    """Checks instruction.md criterion 2: unique_ips is how many different client IPs
    appear, reading the IP as the first thing on each line before the first space."""
    data = _load()
    assert data["unique_ips"] == 3, f"expected 3, got {data['unique_ips']!r}"


def test_top_path():
    """Checks instruction.md criterion 3: top_path is the path requested most often, with
    ties broken alphabetically."""
    data = _load()
    assert data["top_path"] == "/index.html", f"expected '/index.html', got {data['top_path']!r}"
