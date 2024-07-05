# What Is This
判別のつかない(拡張子がない等)バイナリファイルのヘッダーを読み取り、種類ごとに分類するプログラムです。

# How To Use
`config.json`に、判別したいバイナリのあるフォルダと判別するヘッダー、分類後の出力先を書き込みます。

以下の場合、`png`,`jpeg`の画像と`mp4`の動画ファイルと`ogg`の音声ファイルを分類します
```json
{
    "targetPath": "./binaries",
    "sortTargets": [
        {
            "type": "PNG",
            "extension": "png"
        },
        {
            "type": "JFIF",
            "extension": "jpeg"
        },
        {
            "type": "Ogg",
            "extension": "ogg"
        },
        {
            "type": "ftyp",
            "extension": "mp4"
        }
    ],
    "distPath": "./assets"
}
```