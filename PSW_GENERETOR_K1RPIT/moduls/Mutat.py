import secrets
import uuid

num = list(range(1,4))

def mutat_pwd(*,pwd: str) -> str:
   pwd_old = pwd
   random_byt = secrets.randbits(10)
   random_byt = hex(int(random_byt))
   pwd=pwd.capitalize()
   pwd *= secrets.choice(num)
   uuid_str = str(uuid.uuid4())[28:]
   pwd += uuid_str + random_byt


   print('='*50)
   print('new:',pwd)
   print('old:',pwd_old)
   print('='*50)

