import logging
logging.basicConfig(level=logging.INFO)

def add(a, b):
    result = a + b
    logging.info(f"Adding {a} + {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logging.info(f"Multiplying {a} * {b} = {result}")
    return result
