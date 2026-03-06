# How to Install and Run the Auto-Uploader

Follow these simple steps to get your Outplayed clips uploading to YouTube automatically!

### Step 1: Install Python
1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest version for Windows.
2. Run the installer. **CRITICAL:** At the bottom of the installer window, check the box that says **"Add python.exe to PATH"** before clicking Install.

### Step 2: Download this Folder
1. Click the green "Code" button at the top of this page and select **"Download ZIP"**.
2. Extract the ZIP folder to somewhere safe on your computer (like your Documents folder).
3. will need to go to the Google Cloud Console, enable the YouTube Data API v3, create Desktop OAuth 2.0 credentials, download the client_secret.json file
### Step 3: Install Requirements
1. Open the extracted folder.
2. Click on the address bar at the top of the folder window, type `cmd`, and press Enter. A black window will open.
3. Type the following command and press Enter:
   `pip install -r requirements.txt`

### Step 4: Configure Your Folder
1. Open `main.py` using Notepad.
2. Find the line that says `OUTPLAYED_FOLDER = ...`
3. Change the path inside the quotes to exactly where your Outplayed videos are saved. 
4. Save and close Notepad.

### Step 5: The First Run (Important!)
1. Double-click `main.py` to run it.
2. A web browser will open asking you to log into your Google Account. Log in and click "Allow" so the script can upload videos to your YouTube channel.
3. It will now upload any clips currently in your folder. Let it finish!

### Step 6: Make it Run on Startup
1. Double-click the file named `setup_startup.bat`.
2. This will automatically place a shortcut in your Windows Startup folder. 
3. You're done! Every time you turn on your PC, it will quickly check for new videos and upload them.
