def test_function():
    def inner_function():
        print('Я в зоне видимости test_function')
    inner_function()
    return
test_function()



# def test_function():
#     def inner_function():
#         print('Я в зоне видимости test_function')
#     return
# inner_function(): # ВАРИАНТ ВЫЗОВА ФУНКЦИИ inner_function ВНЕ ФУНКЦИИ test_function


