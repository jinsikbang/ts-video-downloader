import os
import requests

def download(url, file_name:str = None):
    if not file_name:
        file_name = url.split('/')[-1]
    
    with open(file_name, "wb") as file:
        file.write(requests.get(url).content)
    
if __name__ == "__main__":
    print(">> ", end="")
    url = input()
    
    media_count = 0
    download(f"{url}media_{media_count}.ts")
    while os.path.getsize(f"media_{media_count}.ts") != 0:
        os.system("copy /b *.ts media.ts")
        os.remove(f"media_{media_count}.ts")
        media_count += 1
        download(f"{url}media_{media_count}.ts")
    
    os.remove(f"media_{media_count}.ts")
    print("Done")