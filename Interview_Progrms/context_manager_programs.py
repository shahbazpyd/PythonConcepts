# f = open("data.txt", "r")
# data = f.read()
# f.close()

# with open("data.txt", "r") as f:
#     data = f.read()


# class FileOpener:
#     def __init__(self, filename):
#         self.filename = filename

#     def __enter__(self):
#         print("opening file...")
#         self.f = open(self.filename)
#         return self.f
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("closing file...")
#         self.f.close()
#         return False
    
# with FileOpener("data.txt") as f:
#     data = f.read()


# from contextlib import contextmanager

# @contextmanager
# def file_opener(filename):
#     print("opening file...")
#     f = open(filename)
#     try:
#         yield f
#     finally:
#         print("closing file...")
#         f.close()

# with file_opener("data.txt") as f:
#     data = f.read()


# from contextlib import contextmanager

# @contextmanager
# def db_transaction(connection):
#     try:
#         yield connection
#         connection.commit()

#     except Exception:
#         connection.rollback()
#         raise

# with db_transaction(conn) as db:
#     db.execute("INSERT INTO users VALUES ('Ravi')")
#     db.execute("rtjtrhetwrq456gf")


from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time() 
    yield 
    end = time.time()  
    print(f"took {end - start:.2f} seconds")

with timer():
    time.sleep(2)