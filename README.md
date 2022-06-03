# nets-tcp-framing

Directory `simple-echo` includes a simple tcp echo server & client

Directory `lib` includes the params package required for many of the programs

Directory `stammer-proxy` includes stammerProxy, which is useful for demonstrating and testing framing

## Functionality 

Protocol to frame byte-array messages in a manner that they will arrive intact even if they are fragmented during transmission.    

*   `stammerProxy.py` forwards tcp streams. It may delay the transmission of data but ensures all data will be forwarded, eventually.
   By default,
   it listens on port 50000 and forwards to localhost:50001.  Use the -?
   option for help.
