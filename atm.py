while True:
    class Atm:
        def __init__(self):
            # self.name = ''
            self.pin = ''
            self.amount = 0
            self.new()
        def new(self):
                user_id = input(
            
                '''
                    1 - enter your pin
                    2 - add amount 
                    3 - send amount 
                    4 - chek amount
                    5 - exit

                '''
                )
                if user_id == '1':
                        self.creat_pin()
                elif user_id == '2':
                        self.add_amount()
                elif user_id  == '3':
                        self.send_amount()
                elif user_id == '4':
                        self.chek()
                elif user_id == '5':
                      self.exit()
                else:
                        print('invalid info')
        def creat_pin(self):
            pin = input('enter your pin = ')
            if pin == input('agane enter your pin'):
                print('pin code created')
            else:
                print('your cord is invalid')
        def add_amount(self):
            tmp_pin = input('enter your pin = ')
            if  self.creat_pin == tmp_pin:
                self.amount  = input('enter your aamout  = ')
                print('added amount')
            else:
                    print('your pin is not same')
        def send_amount(self):
              send_amount = int(input('enter your amount'))
              self.amount = self.amount-send_amount
              if self.amount >= send_amount:
                    print('send amount finly',self.amount)
              else:
                    print('your amount is less then')
        def chek(self):
              temp_pin = input('enter your pin = ')
              if self.pin == temp_pin:
                    print('your totel amount is: ',self.amount)
              else:
                    print("invalid pin plz try ")
        def exit(self):
              print("complete process")            
    obj=Atm()
                            


                
