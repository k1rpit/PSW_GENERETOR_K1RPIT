import secrets
import uuid


number_list=  list(range(1,191))

letters_list = [
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 
    'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 
    'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z'
]

symbols_list = [
    '!', '#', '$', '(', ')', '*', '+', ',', '-', '.', '/', ':', 
    ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '{', '|', '}', 
    '~'
]


def generator_pwd_basic(*,num=number_list,let=letters_list,sym=symbols_list) -> str:
    number = secrets.choice(num)
    letters = secrets.choice(let)
    symbols = secrets.choice(sym)

    return f'{secrets.choice(let)}{secrets.choice(let)}{secrets.choice(let)}{secrets.choice(let)}{secrets.choice(let)}{secrets.choice(sym)}{secrets.choice(num)}'



def generator_pwd_only_int(*,num=number_list) -> str:
    return f'{ secrets.choice(num)}{ secrets.choice(num)}{ secrets.choice(num)}{ secrets.choice(num)}'


def generator_pwd_difficult(*,sym=symbols_list) -> str:
    uuid_str_1 = str(uuid.uuid4())[1:6]
    uuid_str_2 = str(uuid.uuid4())[::5]
    uuid_str_3 = str(uuid.uuid4())[25:]
    symbols = secrets.choice(sym)
    return f'{uuid_str_2}{uuid_str_1}{symbols}{uuid_str_3}'.capitalize()
