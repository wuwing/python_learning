django 基本命令

1. 新建project
django-admin.py startproject project_name

2. 新建app
python manage.py startapp app_name

3. 同步数据库
python manage.py syncdb

4. 清空数据库
python manage.py flush

5. 创建超级管理员
python manage.py createsuperuser

6. 导出数据 导入数据
python manage.py dumpdata appname > appname.json
python manage.py loaddata appname.json

7. django 项目环境终端
python manage.py shell

8. 数据库命令行
python manage.py dbshell
