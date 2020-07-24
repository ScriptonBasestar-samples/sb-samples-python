from celery import current_app
from tasks_amqp import add

# app = current_app.__get_current_object()
r = add.delay(1, 1)
print(r.get())
print(r.ready())
print(r.get())
print(r.ready())

# add.delay(1,1)
# add.delay(1,1)
# add.delay(1,1)
# add.delay(1,1)
