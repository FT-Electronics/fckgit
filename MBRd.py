import time,asyncio
import datetime
from pymodbus.client import ModbusTcpClient
from pymodbus.utilities import checkCRC, computeCRC

client = ModbusTcpClient(host="10.0.88.105", port=502, timeout=2)
while True:
    try:
        result = client.read_input_registers(address=0, count=24, slave=75)

        if not result.isError():
            print(result.registers)
        else:
            print(result)
    except:
        err_count+=1
        print("err")
    time.sleep(1)
