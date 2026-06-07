from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackClient:
    def __init__(self, bot_token: str, channel_id: str):
        if not bot_token:
            raise ValueError("SLACK_BOT_TOKEN が設定されていません。")
        if not channel_id:
            raise ValueError("SLACK_CHANNEL_ID が設定されていません。")
        self.channel_id = channel_id
        self.client = WebClient(token=bot_token)

    def get_recent_messages(self, limit: int = 10) -> list[dict]:
        limit = max(1, min(limit, 15))
        try:
            response = self.client.conversations_history(
                channel=self.channel_id,
                limit=limit,
            )
        except SlackApiError as e:
            error_code = e.response.get("error", "unknown_error")
            raise RuntimeError(f"Slack API error: {error_code}") from e

        messages = [
            {
                "user": msg.get("user", "unknown"),
                "text": msg.get("text", ""),
                "ts": msg.get("ts", ""),
            }
            for msg in response.get("messages", [])
            if msg.get("type") == "message" and msg.get("text")
        ]

        return messages
