# Internet-experiment-backend
该仓库为大四上互联网实验大项目后端

## 数据库

```shell
docker run --name Internet-experiment -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:8.0
```

```shell
docker exec -it Internet-experiment bash
```

```sql
 create database internet_experiment
```

```python
from django.db import models

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    sn = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    is_speak = models.BooleanField()
    
    class Meta:
        db_table = 'device'
```

