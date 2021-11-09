# mysql-python-client
mysql-python-client は、pythonで動作する(マイクロサービス)ランタイムにおいて、mysql を使用する際に用いる、メタライブラリです。  
本ライブラリのインストールは、各システム環境やエッジコンピューティングデバイス内におけるランタイムの特性に応じて、必要に応じて行ってください。    

## 動作環境

* OS: Linux  
* CPU: ARM/AMD/Intel  
* Python Runtime  

## 導入方法
本リポジトリを pipでインストールしてください。
```
pip install "git+https://github.com/latonaio/mysql-python-client.git@main#egg=mysql_client"
```

以下に記載されているコードで、設定を行ってください。  

```python
setup(
	name='mysql-python-client',
	version='0.1.0',
	description='mysql client',
	long_description='mysql client',
	packages=['mysql_client'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'mysqlclient==2.0.3', # この箇所に適切なバージョンに変更してください
	],
	entry_points='''
''')
```