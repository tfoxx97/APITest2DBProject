'''This file represents everything the test project will share with the client 
(i.e commands to run for each scenario in the CLI, firmware version, release name, component, and feature)'''

ECIE_commands = [
    b"Get info\r\n" # use this command to get need info to write to db (fw version, extronlib component, feature)
    b"scenario ECIE_Instantiation 0\r\n",
    b"scenario ECIE_Instantiation 1\r\n",
    b"scenario ECIE_Instantiation 2\r\n",
    b"scenario ECIE_Connect 0\r\n",
    b"scenario ECIE_Connect 1\r\n",
    b"scenario ECIE_Connect 2\r\n",
    b"scenario ECIE_Connect 3\r\n",
    b"scenario ECIE_Connect 4\r\n",
    b"scenario ECIE_Connect 5\r\n",
    b"scenario ECIE_Connected 0\r\n",
    b"scenario ECIE_Disconnected 0\r\n",
    b"scenario ECIE_ReadOnlyProperties 0\r\n",
    b"scenario ECIE_ReadOnlyProperties 1\r\n",
    b"scenario ECIE_ReceiveData 0\r\n",
    b"scenario ECIE_ReceiveData 1\r\n",
    b"scenario ECIE_Send 0\r\n",
    b"scenario ECIE_Send 1\r\n",
    b"scenario ECIE_Send 2\r\n",
    b"scenario SendAndWait 0\r\n",
    b"scenario SendAndWait 1\r\n",
    b"scenario SendAndWait 4\r\n",
    b"scenario SendAndWait 6\r\n",
    b"scenario SetBufferSize 0\r\n",
    b"scenario SetBufferSize 1\r\n",
    b"scenario SetBufferSize 2\r\n",
    b"scenario StartKeepAlive 0\r\n",
    b"scenario StopKeepAlive 0\r\n",
    b"The end\r\n"
]

# Server replies with firmware/component/feature
# hard coded data that will be provided in the test suite
RELEASE = "Release_name"
firmware_str = "1.00.0000-b000"   # hard‑coded in the demo
component = "extronlib.interface"
feature = "EthernetClientInterface"
IP_ADDRESS = '192.168.254.250'
device = None
if IP_ADDRESS == '192.168.254.250':
    device = 'Xi'
elif IP_ADDRESS == '192.168.254.254':
    device = 'QXi'

ECIE_Init_0 = [
    'Given: extronlib.interface is available in the current firmware ✅'
    'And host is a valid IP Address ✅'
    'And port is set to a valid str ✅'
    'When the constructor is called ✅'
    'Then an instance of EthernetClientInterface is successfully created ✅'
]

ECIE_Init_1 = [
    'Given: extronlib.interface is available in the current firmware ✅'
    'And host is a valid IP Address ✅'
    'And port is not set to a valid str ✅'
    'When the constructor is called ✅'
    'Then a ValueError is raised ❌'
    'Unexpected error: Expected a ValueError, got AssertionError'
]

run_through_scenarios = {
    b"scenario ECIE_Instantiation 0\r\n": ECIE_Init_0,
    b"scenario ECIE_Instantiation 1\r\n": ECIE_Init_1,
}