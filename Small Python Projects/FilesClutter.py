import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

if __name__ == "__main__":

    files = os.listdir()
    files.remove("main.py")
    # print(files)

    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')

    imgExts = [".png", ".jpg", "jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".txt", ".docx", ".doc", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    medExts = [".mp4", ".mp3", ".mkv", ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in medExts]

    others = []

    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in medExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            others.append(file)

    # print(others)
    move("Media", medias)
    move("Images", images)
    move("Docs", docs)
    move("Others", others)