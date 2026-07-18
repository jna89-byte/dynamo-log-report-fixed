Read the access log at /app/access.log and write a JSON summary to /app/report.json.

/app/report.json must hold one JSON object with exactly these three keys and nothing else:

1. "total_requests" — a number. How many non-empty lines are in /app/access.log.
2. "unique_ips" — a number. How many different client IPs appear. The client IP is the first thing on each line, before the first space.
3. "top_path" — a string. The path that was requested most often, taken from the quoted request. If two paths are requested the same number of times, use the one that comes first alphabetically.

Do not change /app/access.log.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
