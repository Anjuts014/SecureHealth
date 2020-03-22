import random
from secureHealth.sh_encryption import file_encrypt
def encrypt(input_d):
    in_data=input_d
    n=187
    e=7

    encrypted_info=file_encrypt.data_encrypt(in_data,e,n)
    print(encrypted_info)
    def double_en(to_double):
        double_encrypt = ""
        for item in to_double:
            add_encrypt=random.randint(1,9)
            add_encrypt=str(add_encrypt)
            double_encrypt=double_encrypt+item
            double_encrypt=double_encrypt+add_encrypt
            
        return(double_encrypt)

    double_encrypted_data=double_en(encrypted_info)
    return(double_encrypted_data)

def decrypt(output_d):
    n=187
    def double_decr(from_double):
        set_value = 2
        double_decrypt = ""
        for data in from_double:
            if (set_value % 2 == 0):
                double_decrypt = double_decrypt + data
            set_value = set_value + 1

        return (double_decrypt)

    encrypted_code=output_d
    double_decrypted_data=double_decr(encrypted_code)

    d=23
    decrypted_info=file_encrypt.data_decrypt(double_decrypted_data,d,n)



    return(decrypted_info)