import functions_framework


@functions_framework.errorhandler(ZeroDivisionError)
def handle_zero_division(e):
    return "I'm a teapot", 418


def function(request):
    1 / 0
    return "Success", 200


@functions_framework.http
def hello(request):
    return "Hello world!"


@functions_framework.http
def error_test(request):
    return function(request)
