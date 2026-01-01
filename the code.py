code = "1234"
is_vip = "yes"
ask_if_vip = input("are you vip (yes/no) ? ".lower())
if ask_if_vip == is_vip:
    print("you can go")
else:
    check_code = code
    has_invitation = input("do you have an invitation (yes/no) ?: ".lower())
    is_formal = input("are wearing formal (yes/no) ?: ".lower())
    if has_invitation == "yes" and is_formal == "yes":
        check_code = input("ok then show ur code ")
    
        if check_code == code:    
            print("you can go in ")
        else:
            print("sorry ur code is incorrect")
    elif has_invitation == "yes" or is_formal == "yes":
        if has_invitation == "yes":
            check_code = input("ok then show me your code ")
        
            if check_code == code:
                print("your code is correct\nI will ask if I can let you in")
            else:
                print("your code is not correct")
        elif has_invitation == "no":
            print("you DO NOT HAVE INVITATION")
        elif is_formal == "no":
            print("please change your clothes")
    elif has_invitation == "no" and is_formal == "no":
        print("you can not go in")
