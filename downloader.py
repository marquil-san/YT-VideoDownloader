import os
import subprocess
import sys


BASE_DOWNLOAD_DIR = r"D:\Videos\yt-dlp"
YT_DLP_URL = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe"
FFMPEG_ZIP_URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"📁 Created folder: {path}")


def download_channel(channel_name):
    url = f"https://www.youtube.com/@{channel_name}"
    output_dir = os.path.join(BASE_DOWNLOAD_DIR, channel_name)
    ensure_dir(output_dir)

    print(f"\n🎥 Starting full download of channel: @{channel_name}")
    print(f"📍 Saving videos to: {output_dir}\n")

    command = [
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",
        "--merge-output-format", "mp4",
        "-o", rf"{output_dir}\%(upload_date>%Y-%m-%d)s - %(title)s.%(ext)s",
        "--yes-playlist",
        url
    ]

    subprocess.run(command, check=True)
    print(f"\n✅ All available videos from @{channel_name} have been downloaded successfully!")
    print(f"📂 Check them in: {output_dir}")


def main():
    print("=========================================")
    print("   🎬  YouTube Channel Downloader (yt-dlp)  ")
    print("=========================================\n")

    channel_name = input("Enter the YouTube channel handle: ").strip().lstrip("@")
    if not channel_name:
        print("❌ No channel name entered. Exiting.")
        sys.exit(1)

    print(f"\n🔍 Preparing to download videos from: @{channel_name}")
    download_channel(channel_name)

    print("\n✨ Done! Enjoy your offline collection!")

if __name__ == "__main__":
    main()
