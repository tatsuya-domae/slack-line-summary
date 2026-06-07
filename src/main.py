import os
from dotenv import load_dotenv

from slack_client import SlackClient
from line_client import LineClient
from summarizer import format_messages


def main():
    load_dotenv()

    slack = SlackClient(
        bot_token=os.getenv("SLACK_BOT_TOKEN", ""),
        channel_id=os.getenv("SLACK_CHANNEL_ID", ""),
    )
    line = LineClient(
        channel_access_token=os.getenv("LINE_CHANNEL_ACCESS_TOKEN", ""),
        user_id=os.getenv("LINE_USER_ID", ""),
    )

    try:
        print("Slack からメッセージを取得中...")
        messages = slack.get_recent_messages(limit=10)
        print(f"{len(messages)} 件取得しました。")

        text = format_messages(messages)

        print("LINE に送信中...")
        line.send_text(text)
        print("送信完了。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        raise


if __name__ == "__main__":
    main()
