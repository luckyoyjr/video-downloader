import os
import re
from tkinter import *
from tkinter import messagebox, filedialog
from yt_dlp import YoutubeDL

def detect_platform(url):
    if re.match(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+', url):
        return "YouTube"
    elif re.match(r'(https?://)?(www\.)?instagram\.com/.+', url):
        return "Instagram"
    elif re.match(r'(https?://)?(www\.)?tiktok\.com/.+', url):
        return "TikTok"
    else:
        return None

def download_video_with_ytdlp(url, save_path):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'quiet': True,
            'progress_hooks': [progress_hook],
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"Video downloaded to {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {str(e)}")


# Progress hook for download feedback
def progress_hook(d):
    if d['status'] == 'downloading':
        download_button.config(text="Downloading...")
    elif d['status'] == 'finished':
        download_button.config(text="Download")


# Main function to handle download
def download_video():
    url = url_entry.get()
    save_path = filedialog.askdirectory(title="Select Download Folder") or os.path.expanduser(
        "~/Downloads")

    if not url:
        messagebox.showwarning("Input Error", "Please enter a valid URL.")
        return

    platform = detect_platform(url)
    if platform in ["YouTube", "Instagram", "TikTok"]:
        download_video_with_ytdlp(url, save_path)
    else:
        messagebox.showerror("Error",
                             "Unsupported URL. Please provide a YouTube, Instagram, or TikTok link.")


# Tkinter GUI setup
root = Tk()
root.title("Video Downloader")
root.geometry("500x300")

Label(root, text="Enter Video URL:", font=("Arial", 14)).pack(pady=10)
url_entry = Entry(root, width=50, font=("Arial", 12))
url_entry.pack(pady=5)

download_button = Button(root, text="Download", font=("Arial", 14), bg="blue", fg="white",
                         command=download_video)
download_button.pack(pady=20)

root.mainloop()