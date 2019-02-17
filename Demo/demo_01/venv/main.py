#enconding:utf-8
# 装饰器使用

# def debug(func):
#     def wrapper(*args, **kwargs):
#         print("[DEBUG]: enter {} ()". format(func.__name__))
#         print("Prepare and say")
#         return func(*args, **kwargs)
#     return wrapper
#
# @debug
# def say(something):
#     print("hello {}!".format(something))

# 带参数的装饰器
# def logging(level):
#     def wrapper(func):
#         def inner_wrapper(*args, **kwargs):
#             print("[{level}]; enter function {func} ()".format(level=level, func=func.__name__))
#             return func(*args, **kwargs)
#         return inner_wrapper
#     return wrapper
#
# @logging(level='INFO')
# def say(something):
#     print("say {}!".format(something))
#
# @logging(level='DEBUG')
# def do(something):
#     print("do {}!...".format(something))


# #基于类实现的装饰器
# class logging(object):
#     def __init__(self, func):
#         self.func=func
#     def __call__(self, *args, **kwargs):
#         print("[DEBUG]: enter function {func}()".format(func=self.func.__name__))
#         return self.func(*args, **kwargs)
#
# @logging
# def say(something):
#     print("say {}!".format(something))


# #带参数类实现的装饰器
# class logging(object):
#     def __init__(self, level="INFO"):
#         self.level=level
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print("[{level}]: enter function {func}()".format(level=self.level, func=func.__name__))
#             func(*args, **kwargs)
#             return wrapper()
#
# @logging(level="INFO")
# def say(something):
#     print("say {}!".format(something))

# 内置装饰器
def getx(self):
    return self._x
def setx(self, value):
    self._x=value
def delx(self):
    del self._x
x = property(getx, setx, delx, "I am doc for x property")




if __name__ == '__main__':
    say("hello")


