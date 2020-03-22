import re
import random
from secureHealth.sh_encryption import mod


def data_encrypt(x,e_in,n_in):

    data_toencrypt=x
    input_data=""
    add_data=""


# ASSIGNING A .........LETTER(SMALL AND CAPITAL) ,NUMBER,SPACE,DOT...... TO A NUMBER
    data_inputs={"a":"13","b":"23","c":"33","d":"43","e":"53","f":"63","g":"73","h":"83","i":"93","j":"04",
                 "k":"14","l":"24","m":"34","n":"44","o":"54","p":"64","q":"74","r":"84","s":"94","t":"05",
                 "u":"15","v":"25","w":"35","x":"45","y":"55","z":"65","A":"75","B":"85","C":"95","D":"06",
                 "E":"16","F":"26","G":"36","H":"46","I":"56","J":"66","K":"76","L":"86","M":"96","N":"07",
                 "O":"17","P":"27","Q":"37","R":"47","S":"57","T":"67","U":"77","V":"87","W":"97","X":"08",
                 "Y":"18","Z":"28","0":"38","1":"48","2":"58","3":"68","4":"78","5":"88","6":"98","7":"09",
                 "8":"19","9":"29",".":"39"," ":"59"}


    for letter in data_toencrypt:
        limit_set = random.randint(1,5)    #INCLUDING LIMIT ON THE NUMBER OF DUMMY DATA TO BE INCLUDED
        add_data = "" #DECLARING THE VARIABLE FOR FINAL ENCODED O/P

        #CREATING DUMMY DATA AND ASSIGNUNG IT TO VARIABLE add_data
        for num in range(0,limit_set):
            add_num=0
            add_num = random.randint(1, 9) # DUMMY DATA - A RANDOM NUMBER FROM 1-9
            add_num = str(add_num)
            add_data = add_data + add_num #ADDING DUMMY NUMBER TO add_data
            sym=["&","$","@","!","^"] # DUMMY DATA - SYMBOLS
            sym_set=random.choice(sym) # TO SELECT A RANDOM SYMBOL(DUMMY DATA) FROM THE ABOVE SYMBOL SET
            sym_guess=random.randint(1,9)
            if sym_guess%2==0: # HENCE THE DUMMY SYMBOL MAY OR MAY NOT BE ADDED TO add_data
                add_data=add_data+sym_set

        for data in data_inputs:
            if letter==data:
                data_inputs_new=mod.asym_enc(int(data_inputs[data]),e_in,n_in)
                mark = ["%", "."]
                mark_set = random.choice(mark)
                input_data=input_data+ mark_set
                input_data=input_data+data_inputs_new
                input_data=input_data+"*"
                input_data=input_data+add_data #ADDING DUMMY DATA, NOTE:DUMMY DATA FOR THE SAME LETTER WOULD BE DIFFERENT EACH TIME
    return(input_data)

def data_decrypt(y,d_in,n_in):
    data_todecrypt = y
    complaint_data = ""
    u = re.findall("[%,.][0-9]+[*]", data_todecrypt)
    u_2=[]
    u_3=[]
    for code in u:
        u_1=re.findall("[0-9]+",code)
        u_2=u_2+u_1
    for code_1 in u_2:
        code_1=int(code_1)
        code_2=mod.asym_dec(code_1,d_in,n_in)
        code_2=str(code_2)
        u_3.append(code_2)

    data_output = {"13":"a","23":"b","33":"c","43":"d","53":"e","63":"f","73":"g","83":"h",
                   "93":"i","4":"j","14":"k","24":"l","34":"m","44":"n","54":"o","64":"p",
                   "74":"q","84":"r","94":"s","5":"t","15":"u","25":"v","35":"w","45":"x",
                   "55":"y","65":"z","75":"A","85":"B","95":"C","6":"D","16":"E","26":"F",
                   "36":"G","46":"H","56":"I","66":"J","76":"K","86":"L","96":"M","7":"N",
                   "17":"O","27":"P","37":"Q","47":"R","57":"S","67":"T","77":"U","87":"V",
                   "97":"W","8":"X","18":"Y","28":"Z","38":"0","48":"1","58":"2","68":"3",
                   "78":"4","88":"5","98":"6","9":"7","19":"8","29":"9","39":".","59":" "}
    out_data=""
    for item in u_3:
        for item_2 in data_output:
            if item==item_2:
                out_data=out_data+data_output[item_2]



    return(out_data)


