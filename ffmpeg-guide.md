# FFmpeg Installation Guide

## Windows
1. Download FFmpeg:
   - Visit [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
   - Select a Windows build provider, such as [Gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
   - Download the **Essentials** ZIP file.

2. Extract the ZIP:
   - Extract the downloaded file.
   - Inside the extracted folder, locate the `bin` directory.

3. Add FFmpeg to PATH:
   - Copy the path to the `bin` directory (e.g., `C:\ffmpeg\bin`).
   - Search for "Environment Variables" in the Start menu.
   - Edit the `Path` variable and add the copied path.

4. Verify Installation:
   - Open Command Prompt and run:
     ```bash
     ffmpeg -version
     ```
   - You should see FFmpeg version details.

## macOS/Linux
This guide is for Windows users. For macOS/Linux, install FFmpeg using Homebrew or your package manager.
