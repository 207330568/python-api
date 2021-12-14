from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI()
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vYzg2ZjljMDAtNTY5Yi0xMWVjLThjNmUtYjE2MmM5MjUxYmVl"

api.messages.create(roomId = room_id, text = "Enviado desde el SDK de Python")