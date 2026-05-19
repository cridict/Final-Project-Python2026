# VaultApp
VaultApp is a python program my partner and I made for our final project. It is a desktop app that lets you save your passwords for different websites on your computer so they are organized and safe. All the data stays on your machine so no one else can see it.
(We reccommend putting it onto a USB drive incase of anything happening incase of losing any data)
# Features
* **Password Scrambling:** Automatically obfuscates passwords using Base64 before saving them so if someone opens the file, they can't read them easily.
* **Master Password:** Keeps the app locked with a main password you make when you first open it. You need it to see or delete passwords.
* **Password Tips:** Shows a list of guidelines right in the window to help you think of a good password.
* **Strength Meter:** Checks how long and complicated your password is and fills up a colored bar to show if it is weak or strong.
* **Hacker Check:** Connects to a safe internet API (Have I Been Pwned) to check if your password was ever leaked in a big data breach.
* **Copy Button:** Adds a clipboard button next to your saved password so you can copy it quickly, but it only shows up after you type the master password.
* **Delete and Clear:** Lets you delete just one password entry with the trash icon, or wipe the whole file if you want to start over.
* **Password Counter:** Keeps track of how many total passwords you have saved in your vault.

# How It Works
1. **Setup:** The very first time you run the app, it asks you to type a Master Password. Remember this because you need it later!
2. **Typing Data:** Type in the website name, your username, and the password you want to save. You can look at the **Guidelines** list to make sure your password follows good safety rules.
3. **Testing:** Click **Re-check Strength** to see the bar fill up, or click **API Security Scan** to see if hackers ever stole that password before.
4. **Saving:** Click **Save Password** and the program will scramble it and add it to a JSON file inside a folder called database.
5. **Viewing:** Your passwords will show up at the bottom as dots. Click the **Eye (👁)** button and type your master password to reveal it. Once it's revealed, you can click the **Clipboard (📋)** button to copy it, or the **Trash (🗑)** button to delete it.

# Installation
This app needs the requests library so it can check the internet for password data breaches. You can install it by typing this in your terminal:

pip install requests

# Running the Program
Run the main file:

python VaultApp.py
