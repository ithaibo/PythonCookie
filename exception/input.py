while True:
    try:
        x = input('Enter the first number: ')
        y = input('Enter the second number: ')
        value = x/y
        print 'x/y is ', value
    except:
        print 'Invalid input, Please try again.'
    else:
        break

# except后面不指定异常类型，即捕捉所有异常
# 为try/except增加else，如上面所示，只有当正确执行后才推出循环