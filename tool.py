import cantools

from pprint import pprint

def encode_signal():
    for i in mg:
        for j in i.signals:
            pprint(j.name)
        break



mg = []
def list_message_group(db):
    for i in range(len(db.messages)):
        mg.append(db.messages[i])

def read_file():
    db = cantools.database.load_file("/home/jainy007/Downloads/PWL23_E2A_R11_FDCAN3_MPADinsteadCADM.dbc")

    list_message_group(db)
    
    # pprint(dir(mg[0].signals[0]))
    encode_signal()

    #     print("name - ".ljust(20),mg.signals[i].name)
        # print("length - ".ljust(20),db.messages[0].signals[i].length)
        # print("maximum - ".ljust(20),db.messages[0].signals[i].maximum)
        # print("minimum - ".ljust(20),db.messages[0].signals[i].minimum)
        # print("multiplexer_ids - ".ljust(20),db.messages[0].signals[i].multiplexer_ids)
        # print("multiplexer_signal - ".ljust(20),db.messages[0].signals[i].multiplexer_signal)
        # print("offset - ".ljust(20),db.messages[0].signals[i].offset)
        # print("receivers - ".ljust(20),db.messages[0].signals[i].receivers)
        # print("scale - ".ljust(20),db.messages[0].signals[i].scale)
        # print("spn - ".ljust(20),db.messages[0].signals[i].spn)
        # print("start - ".ljust(20),db.messages[0].signals[i].start)
        # print("unit - ".ljust(20),db.messages[0].signals[i].unit)
        # print("byte_order - ".ljust(20),db.messages[0].signals[i].byte_order)
        # print("comment - ".ljust(20),db.messages[0].signals[i].comment)
        # print("dbc - ".ljust(20),db.messages[0].signals[i].dbc)
        # print("decimal - ".ljust(20),db.messages[0].signals[i].decimal)
        # print("initial - ".ljust(20),db.messages[0].signals[i].initial)
        # print("invalid - ".ljust(20),db.messages[0].signals[i].invalid)
        # print("is_float - ".ljust(20),db.messages[0].signals[i].is_float)
        # print("is_multiplexer - ".ljust(20),db.messages[0].signals[i].is_multiplexer)
        # print("is_signed - ".ljust(20),db.messages[0].signals[i].is_signed)


if __name__ == "__main__":
    read_file()