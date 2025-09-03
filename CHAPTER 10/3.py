class change:
    a = 10

object = change()
print(object.a)
object.a = 0
print(object.a)
print(change.a)