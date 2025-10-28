from behave import *

from app.calc import Calculator


@given('I open the calculator')
def step_impl(context):
    context.calc = Calculator()

# ADD
@when('I type 2 + 2')
def step_impl(context):
    context.result = context.calc.add(2, 2)


@when('I type {op1} + {op2}')
def step_impl(context, op1, op2):
    context.result = context.calc.add(float(op1), float(op2))


# SUBSTRACT
@when('I type {op1} - {op2}')
def step_impl(context, op1, op2):
    context.result = context.calc.substract(float(op1), float(op2))


# MULTIPLY
@when('I type {op1} * {op2}')
def step_impl(context, op1, op2):
    context.result = context.calc.multiply(float(op1), float(op2))


# DIVIDE
@when('I type {op1} / {op2}')
def step_impl(context, op1, op2):
    context.result = context.calc.divide(float(op1), float(op2))


# POWER
@when('I type {op1} ^ {op2}')
def step_impl(context, op1, op2):
    context.result = context.calc.power(float(op1), float(op2))


# SQUARE ROOT
@when('I type sqrt({op1})')
def step_impl(context, op1):
    context.result = context.calc.square_root(float(op1))


# LOG10
@when('I type log10({op1})')
def step_impl(context, op1):
    context.result = context.calc.log10(float(op1))


# ASSERTIONS
@then('the result is 4')
def step_impl(context):
    assert context.result == 4


@then('the result is {res}')
def step_impl(context, res):
    # Intenta convertir a int primero, si falla usa float
    try:
        expected = int(res)
        # Para enteros, compara exactamente
        assert context.result == expected, f"Expected {expected}, got {context.result}"
    except ValueError:
        # Si tiene punto decimal, usa float con tolerancia
        expected = float(res)
        assert abs(context.result - expected) < 0.0001, f"Expected {expected}, got {context.result}"