# 简介

Django数据库连接超过wait_timeout导致连接丢失时自动重新连接数据库

# 安装

```sh
pip install django_db_reconnect
```
> 注意仅支持`pymysql`，使django使用`pymysql`需要先安装包并在settings.py所在目录的__init__.py增加如下代码：
> ```
> import pymysql
> pymysql.install_as_MySQLdb()
> ```

# 使用

添加`django_db_reconnect`到settings.py的INSTALLED_APPS
```python
INSTALLED_APPS = (
    # 省略其他配置
    'django_db_reconnect',
)
```

# 其他问题
1. 事务或者其他autocommit=False非自动提交情况下将不会自动重连，否则可能导致连接丢失前的写入没有commit被丢弃