from bnsh import BNSHRuntime
from bnsh.backends import EchoBackend

runtime = BNSHRuntime(model="development", backend=EchoBackend())
print(runtime.chat("Hello from BNSH AI"))
