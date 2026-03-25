#!/usr/bin/env python3
"""
Zoom文字起こし → Obsidianノート 自動変換スクリプト

使い方:
  1. pip install watchdog
  2. python zoom_watcher.py

Zoomフォルダに meeting_saved_closed_caption.txt が保存されると自動で
Obsidianノートを生成して git push します。
"""

import re
import subprocess
import sys
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# ── パス設定 ──────────────────────────────────────────────
ZOOM_DIR = Path(r"C:\Users\vomoy\OneDrive\ドキュメント\Zoom")
VAULT_DIR = Path(r"C:\Users\vomoy\OneDrive\ドキュメント\Obsidian Vault")
KAETSU_DIR = Path(r"C:\Users\vomoy\OneDrive\ドキュメント\kaetsu-ai-kenshu")

# かえつ有明リポジトリに追加プッシュするミーティング名のキーワード
KAETSU_KEYWORDS = ["かえつ", "kaetsu"]

# ── Claudeへのプロンプト ───────────────────────────────────
PROMPT_TEMPLATE = """\
以下のZoom文字起こしから、CLAUDE.mdのルールに従ってObsidianノートを作成してください。

## 出力フォーマット（厳守）
- 必ず1行目に保存先を書く: SAVE_TO: フォルダ名/ファイル名.md
- 2行目以降: frontmatterから始まるノート全文

出力例の1行目:
SAVE_TO: 04_ツール・方法論/AI研修メモ.md

## ミーティング情報
- ミーティング名: {meeting_name}
- 日付: {date}

## 文字起こし

{transcript}
"""


# ── Claude CLI呼び出し ─────────────────────────────────────
def convert_with_claude(txt_path: Path, meeting_name: str, meeting_date: str) -> tuple[str, str]:
    transcript = txt_path.read_text(encoding="utf-8")

    prompt = PROMPT_TEMPLATE.format(
        meeting_name=meeting_name,
        date=meeting_date,
        transcript=transcript,
    )

    print("  🤖 Claude呼び出し中（1〜2分かかります）...")
    result = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=300,
        cwd=str(VAULT_DIR),  # CLAUDE.mdを自動で読む
    )

    if result.returncode != 0:
        raise RuntimeError(f"Claude CLIエラー:\n{result.stderr}")

    return _parse_output(result.stdout)


def _parse_output(output: str) -> tuple[str, str]:
    """SAVE_TO行を1行目から抽出し、(save_path, content) を返す"""
    lines = output.strip().split("\n")

    # SAVE_TO: を探す（最初の数行を検索）
    for i, line in enumerate(lines[:5]):
        m = re.match(r"SAVE_TO:\s*(.+\.md)", line.strip())
        if m:
            save_path = m.group(1).strip()
            content = "\n".join(lines[i + 1 :]).strip()
            return save_path, content

    raise ValueError(
        f"SAVE_TO行が見つかりません。\n出力の先頭:\n{output[:300]}"
    )


# ── 保存 & Git push ───────────────────────────────────────
def save_and_push(save_path: str, content: str) -> None:
    note_path = VAULT_DIR / save_path
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(content, encoding="utf-8")
    print(f"  ✅ 保存: {note_path.relative_to(VAULT_DIR)}")

    subprocess.run(["git", "add", str(note_path)], cwd=VAULT_DIR, check=True)
    subprocess.run(
        ["git", "commit", "-m", f"add: {note_path.name}（Zoom自動変換）"],
        cwd=VAULT_DIR,
        check=True,
    )
    subprocess.run(["git", "push"], cwd=VAULT_DIR, check=True)
    print("  ✅ Obsidian vault push完了")


def push_to_kaetsu(note_name: str, content: str) -> None:
    """かえつ有明リポジトリにもプッシュする"""
    note_path = KAETSU_DIR / note_name
    note_path.write_text(content, encoding="utf-8")
    print(f"  ✅ かえつリポジトリに保存: {note_name}")

    subprocess.run(["git", "add", str(note_path)], cwd=KAETSU_DIR, check=True)
    subprocess.run(
        ["git", "commit", "-m", f"add: {note_name}（Zoom自動変換）"],
        cwd=KAETSU_DIR,
        check=True,
    )
    subprocess.run(["git", "push"], cwd=KAETSU_DIR, check=True)
    print("  ✅ かえつリポジトリ push完了")


# ── ファイル監視 ──────────────────────────────────────────
class ZoomHandler(FileSystemEventHandler):
    TARGET = "meeting_saved_closed_caption.txt"

    def __init__(self):
        self._processing: set[str] = set()

    def on_created(self, event):
        self._handle(event.src_path)

    def on_modified(self, event):
        self._handle(event.src_path)

    def _handle(self, src_path: str) -> None:
        path = Path(src_path)
        if path.is_dir() or path.name != self.TARGET:
            return
        if str(path) in self._processing:
            return

        self._processing.add(str(path))

        # 書き込み完了を待つ
        time.sleep(5)

        # フォルダ名から情報抽出
        # 例: "2026-03-25 08.58.00 かえつ有明AI研修"
        folder_name = path.parent.name
        parts = folder_name.split(" ", 2)
        meeting_date = parts[0] if parts else "不明"
        meeting_name = parts[2] if len(parts) > 2 else folder_name

        print(f"\n📝 変換開始: {meeting_name} ({meeting_date})")

        try:
            save_path, content = convert_with_claude(path, meeting_name, meeting_date)
            save_and_push(save_path, content)

            # かえつ有明の研修はかえつリポジトリにも追加プッシュ
            if any(kw in meeting_name.lower() for kw in KAETSU_KEYWORDS):
                note_name = Path(save_path).name
                print(f"  📂 かえつリポジトリにも追加プッシュします: {note_name}")
                push_to_kaetsu(note_name, content)

            print(f"  🎉 完了: {save_path}\n")
        except Exception as e:
            print(f"  ❌ エラー: {e}\n")
        finally:
            self._processing.discard(str(path))


# ── エントリポイント ──────────────────────────────────────
def main() -> None:
    if not ZOOM_DIR.exists():
        print(f"❌ Zoomフォルダが見つかりません: {ZOOM_DIR}")
        sys.exit(1)

    print("=" * 50)
    print("  Zoom → Obsidian 自動変換")
    print("=" * 50)
    print(f"監視: {ZOOM_DIR}")
    print(f"保存: {VAULT_DIR}")
    print("Ctrl+C で停止\n")

    handler = ZoomHandler()
    observer = Observer()
    observer.schedule(handler, str(ZOOM_DIR), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n停止中...")
        observer.stop()
    observer.join()
    print("停止しました")


if __name__ == "__main__":
    main()
