from flightGroupClassMk2 import flightGroup
import exampleGroupGenerator

origin_Sample = [('MSP', 3),('YYZ', 1),('BOS', 2)]
def origin_list_test_protocol(choice):
    if choice == 1:
        copy1 = create_sample_save()
    elif choice == 2:
        copy1 = create_input_save()
    else:
        print("INVALID CHOICE FOR COMPARISON ROUTE")

    
    copy2 = load_file_return()
    if copy1 == copy2:
        print("Origin list protocol Successful")
        print("---------------------------------")
        print("\n \n Your group consists of:  \n")
        for travelers in copy1:
            print(str(travelers[1]) + "  Travelers from " + travelers[0])
        del copy1
        del copy2

    else:
        print(copy2)
        print("Test Failure")



def create_input_save():
    tempGroup = flightGroup.from_input()
    tempGroup.save()
    temp = tempGroup.groupOrigins
    del tempGroup
    return temp

def load_file_return():
    tempGroup = flightGroup.from_file()
    temp = tempGroup.groupOrigins
    del tempGroup
    return temp


def create_sample_save():
    orig_dest_pair = exampleGroupGenerator.random_group_maker()
    tempGroup = flightGroup(orig_dest_pair[1], '12-01-2022', '12-15-2022', 14, orig_dest_pair[0])
    tempGroup.save()
    temp = tempGroup.groupOrigins
    del tempGroup
    return temp