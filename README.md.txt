# Universal Web-Based Video Downloader

A simple, self-hosted web tool that allows you to download videos from hundreds of websites. Built with Python, Flask, and yt-dlp, and designed for easy, free deployment on Render.com.

---

### ✨ Features

*   **Universal Support:** Works with hundreds of websites supported by `yt-dlp` (YouTube, Vimeo, Dailymotion, etc.).
*   **Format Selection:** Displays a list of available video and audio formats.
*   **Detailed Information:** Shows quality, file extension, and estimated file size for each option.
*   **Direct Actions:** Provides "Watch" and "Download" buttons for each format.
*   **Self-Hosted & Free:** Can be deployed entirely for free on Render's hobby tier.
*   **Simple Interface:** Clean, responsive, and easy-to-use user interface.

---

### 🚀 Deployment to Render

This repository is configured for one-click deployment on Render.

1.  **Fork this Repository:** Click the "Fork" button at the top-right of this page to create your own copy.
2.  **Deploy with Render:** Click the button below to deploy your forked repository.

   [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

3.  **Configuration:**
    *   Connect your GitHub account.
    *   Give your new service a unique **Service Name** (e.g., `my-cool-video-app`).
    *   Render will automatically read the `render.yaml` file and fill in all the settings.
    *   Make sure the **Free** plan is selected.
4.  **Create Service:** Click **"Create Web Service"**. Render will build and deploy your application. This may take 5-10 minutes.
5.  **Done!** Your service will be live at the URL provided by Render.

---

### 🛠️ Tech Stack

*   **Backend:** Python 3
*   **Web Framework:** Flask
*   **WSGI Server:** Gunicorn
*   **Video Scraping:** yt-dlp
*   **Frontend:** HTML, CSS, JavaScript (no frameworks)
*   **Hosting:** Render.com

---

### ⚠️ Disclaimer

This tool is for educational purposes and for downloading content that you have a legal right to access (e.g., your own videos, public domain content, or videos with a Creative Commons license). Downloading copyrighted material without permission from the copyright holder may be illegal in your country. The user of this tool is solely responsible for their actions.