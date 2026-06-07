import requests


LINE_API_URL = "https://api.line.me/v2/bot/message/push"
MAX_TEXT_LENGTH = 5000


class LineClient:
    def __init__(self, channel_access_token: str, user_id: str):
        if not channel_access_token:
            raise ValueError("LINE_CHANNEL_ACCESS_TOKEN が設定されていません。")
        if not user_id:
            raise ValueError("LINE_USER_ID が設定されていません。")
        self.user_id = user_id
        self.headers = {
            "Authorization": f"Bearer {channel_access_token}",
            "Content-Type": "application/json",
        }

    def send_text(self, text: str) -> None:
        if len(text) > MAX_TEXT_LENGTH:
            text = text[:MAX_TEXT_LENGTH - 3] + "..."

        payload = {
            "to": self.user_id,
            "messages": [{"type": "text", "text": text}],
        }

        response = requests.post(LINE_API_URL, headers=self.headers, json=payload, timeout=10)

        if response.status_code != 200:
            raise RuntimeError(
                f"LINE API error: {response.status_code} {response.text}"
            )
