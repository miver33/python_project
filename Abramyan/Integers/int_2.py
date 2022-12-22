BYTES_IN_KB: int = 1024

bytes_: int = int(input("enter bytes: "))

kb: int = bytes_ // BYTES_IN_KB

print(f"{bytes_} bytes is {kb} kilobytes")
