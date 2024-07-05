import os
import shutil
import json

def sortBinary(targetPath, sortTargets, distPath):
    # 指定したディレクトリ内のすべてのファイルを取得
    count = 0
    for fileName in os.listdir(targetPath):
        filePath = os.path.join(targetPath, fileName)
        
        # ファイルが通常のファイルであることを確認
        if os.path.isfile(filePath):
            with open(filePath, 'rb') as file:
                # 最初の16バイトを読み込む
                firstTenBytes = file.read(16)
                
                # sortTargets 状のファイルタイプを探す
                for config in sortTargets:
                    fileType = config['type']
                    fileExtension = config['extension']
                    
                    # バイトデータを文字列に変換して検索
                    if fileType.encode() in firstTenBytes:
                        # 新しいファイル名を生成
                        newFileName = f"{os.path.splitext(fileName)[0]}.{fileExtension}"
                        newFilePath = os.path.join(distPath, fileType, newFileName)
                        
                        # 出力ディレクトリが存在しない場合作成
                        if not os.path.exists(os.path.join(distPath, fileType)):
                            os.makedirs(os.path.join(distPath, fileType))

                        # 該当するファイルを指定したディレクトリにコピー
                        shutil.copy(filePath, newFilePath)
                        print(f'File-{count} Sorted "{fileName}" as "{newFilePath}/{newFileName}"')
        count += 1

if __name__ ==  '__main__':
    with open('config.json', 'r') as configFile:
        config = json.load(configFile)

    directoryPath = config['targetPath']
    sortTargets = config['sortTargets']
    distPath = config['distPath']

    sortBinary(directoryPath, sortTargets, distPath)
