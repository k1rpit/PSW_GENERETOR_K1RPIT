from moduls import generator as gen
from moduls import Mutat as Mut
import sys
import json


def json_dumps(*,p: str):
    data_json = json.dumps({'passworld':p})

    with open('pwd.json','w') as f:
        f.write(data_json)


if __name__ == "__main__":
    print('--'*32)
    print(f'[1]:\tonly int passworld')
    print(f'[2]:\tbasic passworld')
    print(f'[3]:\thard passworld')
    print(f'[4]:\tmutat passworld')
    print('--'*32)

    user_input = int(input('>>>'))

    if user_input == 1:
        pwd=gen.generator_pwd_only_int()
        print(f'{pwd=}')

        json_dumps(p=pwd)
    elif user_input == 2:
        pwd=gen.generator_pwd_basic()
        print(f'{pwd=}')

        json_dumps(p=pwd)
    elif user_input == 3:
        pwd=gen.generator_pwd_difficult()
        print(f'{pwd=}')

        json_dumps(p=pwd)
    elif user_input == 4:
        user_pwd = input('passworld>>>')
        Mut.mutat_pwd(pwd=user_pwd)
    else:
        sys.exit(1)


    