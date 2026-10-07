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
RELEASE = "Top Gear"
firmware_str = "1.00.0000-b000"   # hard‑coded in the demo
component = "extronlib.interface"
feature = "EthernetClientInterface"