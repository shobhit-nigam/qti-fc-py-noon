"""module for understanding the
concept of modules"""

print("hello from colours")

def blue():
    print("cool blue")

def yellow():
    print("bright yellow")

def green():
    """green needs blue & yellow functions"""
    print("green has:")
    blue()
    yellow()



