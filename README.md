# VaultApp
VaultApp is a desktop password manager my partner and I made for our final project. It lets you safely store your passwords for different websites locally on your computer.

### 1. Once I Hit Play, What Should I Do?
1. Create a Master Password in the setup box that pops up first.
2. Type a website, username, and password into the text boxes.
3. Click **Re-check Strength** to see your password rating, or click **API Security Scan** to see if your password has ever been leaked on the internet.
4. Click **Save Password** to lock your encrypted password into the vault.
5. Scroll to the bottom to see your saved passwords. Click the eye button and type your master password to reveal the password, copy it, or delete it.

### 2. Known Bugs or Errors and How to Avoid Them
1. The API scan will crash the app if you don't have the requests library installed. Fix this by running `pip install requests` in your terminal before playing.
2. The app lets you save an entry without a username since usernames are optional. Just make sure you don't accidentally leave it blank if you wanted to save one.

### 3. Partner Responsibilities and Project Concepts
1. **Joey's part:** I did data saving, file paths, and making sure our data manager script reads and writes the JSON arrays correctly. I also added the Base64 encryption to hide the passwords better.
2. **Vincents part:** I designed the GUI window and set up the 8 to 9 character strength checker bar. They also handled the web API connection for the security scanner.
