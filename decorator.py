def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"正在调用函数: {func.__name__}，参数: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"函数 {func.__name__} 执行完毕，结果: {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(3, 5)

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行耗时: {end_time - start_time:.4f} 秒")
        return result
    return wrapper

@measure_time
def long_running_task():
    time.sleep(1)
    return "任务完成"

long_running_task()

def password_required(func):
    def wrapper(*args, **kwargs):
        while True:
            password = input("请输入密码: ")
            if password == "secret":
                break
            else:
                print("密码错误，请重试。")
        return func(*args, **kwargs)
    return wrapper

@password_required
def sensitive_function():
    print("访问敏感函数")

sensitive_function()