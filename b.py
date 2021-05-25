import socket

sock= socket.socket(socket.AF_BLUETOOTH,type=socket.SOCK_STREAM,proto=socket.BTPROTO_RFCOMM )




mybluetooth_address='A0:AF:BD:9A:AA:E1'

myphoneaddress='70:5e:55:60:19:72'
sock.connect((myphoneaddress,3))

#sock.listen(5)

#socket2,address	=sock.accept()
#rint(socket2,address)

sock.close()
          
