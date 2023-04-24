import re
class Emails:

    def __init__(self, email : str):
        self.email = email
        self.validate(email)

    @classmethod
    def validate(cls, email : str):
        if '@' not in email:
            print('There are no "@" - incorrect email')
        else:
            prefix, domain = email.split('@')
            p = 0
            d = 0
            e = 0
            for i in prefix:
                if i.isalnum() or i in ['.','_','-']:
                    pass
                else:
                    p += 1
            if p != 0 or prefix[0].isalnum() != True or prefix[len(prefix)-1].isalnum() != True:
               print('The prefix is incorrect')
               e += 1
            for j in domain:
                if j.isalnum() or j in ['.', '-']:
                    pass
                else:
                    d += 1
            if d != 0 or domain.count('.') != 1 or domain[0].isalnum() != True or domain[len(domain) - 2:len(domain)].isalpha() != True:
                print('The domain is incorrect')
                e += 1
            if e == 0:
                print('The email is correct')


    def __str__(self):
        return f'({self.email})'
    def __repr__(self):
        return self.__str__()

a = Emails('kery@gma-il.vb')
print(a)
