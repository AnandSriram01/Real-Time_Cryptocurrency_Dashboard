from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DashConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.groupname='dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self,close_code):

        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )


    async def receive(self, text_data):
        current_tick = json.loads(text_data)
        # print(current_tick['product_id'])
        # coin_id = current_tick['product_id']
        # price = current_tick['price']
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'deprocessing',
                'data':current_tick
            }
        )

        # print ('>>>>',text_data)

        # pass

    async def deprocessing(self,event):
        # print(event)
        # print(event.keys())
        if (event['data']['type'] == 'ticker'):
            print(event['data']['product_id'])
        await self.send(text_data=json.dumps(event['data']))
