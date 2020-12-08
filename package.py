name = "gmp"
version = "5.0.0"

variants=[["platform-linux", "arch-x86_64"]]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")


