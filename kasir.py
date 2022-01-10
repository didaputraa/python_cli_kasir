import os;

list_menu    = ["BAKSO LAVA", "SATE KUDA", "BIAWAK KRENGSENGAN"];
list_harga   = [20000, 27000, 10000];
select_menu  = [];
select_count = [];
error_msg    = "";
loop_status  = True;
status       = False;
dots         = "-----------------------------------------";


def menu_count():
    count = input("Jumlah porsi: ");
    return count;
    
def checkExist_menu(item):
    if item in select_menu:
        position = select_menu.index(item);
        select_count[position] = str(int(select_count[position]) + int(menu_count()));
    else:
        select_menu.append(item);
        select_count.append(menu_count());
    
def repeat(n):
    return " " * n;


while loop_status == True:
    os.system("cls");
    print("\n|-----------------------------------------|");
    print("|        Menu           |       harga     |");
    print("|-----------------------------------------|");
    print("|\t\t\t|\t\t  |");
    print("| 1. BAKSO LAVA\t\t| Rp 20.000       |");
    print("| 2. SATE KUDA\t\t| Rp 27.000       |");
    print("| 3. BIAWAK KRENGSENGAN\t| Rp 10.000\t  |");
    print("|\t\t\t|\t\t  |");
    print("|\t\t\t|\t\t  |");
    print("|-----------------------------------------|");
    
    menuCase = input("pilih menu (1 s/d 3): ");
    menu     = int(menuCase);
    
    if menu in [1,2,3]:
        menu_list_select = list_menu[menu-1];
        checkExist_menu(menu_list_select);
        
    else:
        loop_status = False;
        error_msg   = "Menu tidak ada";
        status      = False;
        
    loop = input("Pesan lagi(y/n): ");
    
    if loop.lower() == "n":
        loop_status = False;
        status      = True;


if status == True:
    print("\nMENU YG DI PESAN")
    print(dots);
    
    index = 0;
    iHarga= 0;
    tot   = 0;
    dot   = len(dots);
    dotX  = 0;
    dotL1 = 0;
    dotL2 = 0;
    
    for item in select_menu:
        dotL1 = dot - (len(item) + 3) - 10;
        dotL2 = 6 - len(select_count[index]);
        iHarga= list_harga[list_menu.index(item)];
        
        result = "| {}" + repeat(dotL1) + "{}" + repeat(dotL2) + "{}|";
        
        print(result.format(item, select_count[index], str(iHarga)));
        print(dots);
        
        tot += int(select_count[index]) * int(iHarga);
        index += 1;
        
    print("Total:", tot);
    
else:
    print(error_msg);
