def test_function():
    print("Я тут")

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
inner_function()#внутренняя функция" не определена
