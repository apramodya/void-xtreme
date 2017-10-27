def base62(a):
    baseit = (lambda a=a, b=62: (not a) and '0' or
        baseit(a-a%b, b*62) + '0123456789abcdefghijklmnopqrstuvwxyz'
                              'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[a%b%61 or -1*bool(a%b)])
    return baseit()


