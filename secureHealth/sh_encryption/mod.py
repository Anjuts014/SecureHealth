def asym_enc(x,e,n):
      enc=(x**e)%n
      enc=str(enc)
      return(enc)



def asym_dec(enc,d,n):
    dec = (enc**d) % n
    return(dec)
