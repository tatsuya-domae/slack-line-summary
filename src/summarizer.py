from datetime import datetime


def format_messages(messages: list[dict]) -> str:
    if not messages:
        return "（取得できるメッセージがありませんでした）"

    lines = []
    for msg in messages:
        timestamp = _format_ts(msg.get("ts", ""))
        user = msg.get("user", "unknown")
        text = msg.get("text", "").strip()
        lines.append(f"[{timestamp}] {user}\n{text}")

    result = "\n\n".join(lines)
    if len(result) > 4500:
        result = result[:4497] + "..."
    return result


def _format_ts(ts: str) -> str:
    try:
        return datetime.fromtimestamp(float(ts)).strftime("%m/%d %H:%M")
    except (ValueError, OSError):
        return ts
