# python-lambda-rekognition-example

- AWS Lambda(Python3.8)から AWS rekognition を使用する実装例
- Docker run で lambda にアップロードするための zip ファイルを自動生成する

## 実行手順

```bash
cd python-lambda-rekognition-example
docker build -t <Dockerイメージ名> .
docker run -v "$PWD":/var/task <Dockerイメージ名>
```

（例）Docker イメージ名を「myImage」として実行する場合

```bash
cd python-lambda-rekognition-example
docker build -t myImage .
docker run -v "$PWD":/var/task myImage
```
