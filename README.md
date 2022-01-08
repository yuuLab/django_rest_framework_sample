# This is a sample project for Django REST framework
## Set Up
下記コマンドを順に実行し、APIプロジェクトを起動する。
```
docker-compose up -d
```
```
docker-compose exec web python3 manage.py migrate
```
```
docker-compose exec web python3 manage.py createsuperuser
```


## Access
1. 管理画面 (http://localhost:8000/admin)

1. APIコンソール画面 (http://localhost:8000/api)

1. 作成したアカウント一覧取得 (http://localhost:8000/api/userAccount)