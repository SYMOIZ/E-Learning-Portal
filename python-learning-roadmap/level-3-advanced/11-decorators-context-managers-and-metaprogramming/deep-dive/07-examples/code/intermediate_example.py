from contextlib import contextmanager

@contextmanager
def managed_message():
    print("start")
    try:
        yield
    finally:
        print("end")

with managed_message():
    print("working")
