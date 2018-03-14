# encoding=utf-8

# doctest模块用于函数测试，结合函数的文档（doc）
def square(x):
    '''
    squares a number and return the results
    在函数的文档中给出实例！！！
    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x ** 2


# 使用doctest测试，它会检查文档中类似给出的实例，运行函数，看是否正确，正确的话成功运行，否则出错
if __name__ == '__main__':
    import doctest, my_math

    doctest.testmod(my_math)
