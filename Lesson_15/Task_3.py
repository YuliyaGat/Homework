CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
   #current_ch = 0
   def __init__(self, channel_list):
       self.channel_list = channel_list
       TVController.current_ch = 0

   def  first_channel(self):
       TVController.current_ch = 0
       return self.channel_list[0]

   def last_channel(self):
       TVController.current_ch = len(self.channel_list)-1
       return self.channel_list[-1]

   def turn_channel(self, N):
       TVController.current_ch = N-1
       return self.channel_list[N-1]

   def next_channel(self):
       if TVController.current_ch == len(self.channel_list)-1:
          TVController.current_ch = 0
       else:
          TVController.current_ch += 1
       return self.channel_list[TVController.current_ch]

   def previous_channel(self):
       if TVController.current_ch == 0:
          TVController.current_ch = len(self.channel_list)-1
       else:
          TVController.current_ch -= 1
       return self.channel_list[TVController.current_ch]

   def current_channel(self):
       return self.channel_list[TVController.current_ch]

   def is_exist(self, channel):
       if str(channel) in self.channel_list or channel in range(1,len(self.channel_list)+1):
         return 'Yes'
       else:
         return 'No'


controller = TVController(CHANNELS)
print(controller.next_channel())
print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel() )
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist('BBC'))