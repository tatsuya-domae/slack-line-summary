# Slack → LINE Summary Tool

Slackの指定チャンネルから直近メッセージを取得し、LINEに整形して送信するCLIツール。

---

## セットアップ

### 1. リポジトリのクローン・移動

```bash
cd slack-line-summary
```

### 2. 依存ライブラリのインストール

```bash
pip install -r requirements.txt
```

### 3. 環境変数の設定

```bash
cp .env.example .env
```

`.env` を開き、各値を入力する（詳細は「環境変数」セクション参照）。

---

## 環境変数

| 変数名 | 説明 |
|--------|------|
| `SLACK_BOT_TOKEN` | Slack Bot トークン（`xoxb-` で始まる） |
| `SLACK_CHANNEL_ID` | 取得対象チャンネルの ID（`C` で始まる） |
| `LINE_CHANNEL_ACCESS_TOKEN` | LINE Messaging API のチャンネルアクセストークン |
| `LINE_USER_ID` | 送信先の LINE ユーザー ID（`U` で始まる） |

### LINE_USER_ID の取得方法

1. LINE Developers コンソール（https://developers.line.biz/）にログイン
2. 対象チャンネル > Messaging API > ボットのユーザー ID を確認
3. 送信先が自分自身の場合は、LINE アプリ上でボットと友達になったうえで  
   webhook イベント（`source.userId`）から取得する

---

## 実行方法

```bash
cd src
python main.py
```

正常に動作すると、ターミナルに以下のように出力される：

```
Slack からメッセージを取得中...
10 件取得しました。
LINE に送信中...
送信完了。
```

---

## 動作確認手順

### 1. 環境変数の確認

`.env` ファイルが存在し、4 つの変数すべてに値が入っていることを確認する。

```bash
cat .env
```

### 2. Slack チャンネルにテストメッセージを投稿

Slack の対象チャンネル（`SLACK_CHANNEL_ID` で指定したチャンネル）に、任意のメッセージを数件投稿しておく。

### 3. スクリプトを実行

```bash
cd src
python main.py
```

### 4. LINE でメッセージを確認

LINE アプリを開き、Bot からのメッセージが届いていることを確認する。  
メッセージは以下の形式で届く：

```
[06/07 23:00] U0123456789
こんにちは！テストメッセージです。

[06/07 22:55] U0123456789
別のメッセージ
```

### 5. エラーが出た場合の確認ポイント

| エラー内容 | 確認箇所 |
|-----------|---------|
| `SLACK_BOT_TOKEN が設定されていません` | `.env` の `SLACK_BOT_TOKEN` を確認 |
| `Slack API error: not_in_channel` | Bot をチャンネルに `/invite @Bot名` で招待する |
| `Slack API error: channel_not_found` | `SLACK_CHANNEL_ID` の値を確認 |
| `LINE API error: 401` | `LINE_CHANNEL_ACCESS_TOKEN` を確認 |
| `LINE API error: 400` | `LINE_USER_ID` の形式を確認（`U` で始まる） |
