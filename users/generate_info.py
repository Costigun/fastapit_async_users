from database import get_db
import models
db = next(get_db())

super_role = models.Permission(rights='superuser')
read_only = models.Permission(rights='ro')

superuser = models.User(username='maksim',email='maximneveraa@gmail.com',
                        password='123456',permissions=super_role
                        )
ro_user = models.User(username='alexey',email='alexey@gmail.com',
                        password='123456',permissions=read_only
                        )
db.add(super_role)
db.add(read_only)
db.add(superuser)
db.add(ro_user)
db.commit()