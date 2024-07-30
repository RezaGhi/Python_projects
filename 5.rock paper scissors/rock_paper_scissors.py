import random
def play():
    print(f'hi !!!!\nwe wanna play rock paper scissors together.')
    your_point,pc_point=0,0
    while True:
        print(f'your point= {your_point}\npc point= {pc_point}\n')
        you=input("if you want rock enter 'R',paper enter 'P',scissors enter 'S': ").lower()
        pc=random.choice(['r','p','s'])
        print(f"pc's choice= {pc}")
        if you==pc:
            print(f'pc={pc}, you={you}\nyour choices is same please try again ')
            continue
        if (pc=='r' and you=='s') or (pc=='p' and you=='r') or (pc=='s' and you=='p'):
            pc_point +=1
        else:
            your_point +=1

        print(f'your point= {your_point}\npc point= {pc_point}\n')
        if pc_point==3:
            print('you lose!!!!')
            break
        elif your_point==3:
            print('you woooooooooooooon')
            break
        
play()   