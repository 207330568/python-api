from webexteamssdk import WebexTeamsAPI
import json

api = WebexTeamsAPI()

card = '''
{
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.2",
    "body": [
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "width": 2,
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Abrir ticket en Service Now",
                            "weight": "Bolder",
                            "size": "Medium"
                        },
                        {
                            "type": "TextBlock",
                            "text": "Por favor introduzca la siguiente información para abrir el tickete en ServiceNow",
                            "isSubtle": true,
                            "wrap": true
                        },
                        {
                            "type": "TextBlock",
                            "text": "Descripción corta",
                            "wrap": true
                        },
                        {
                            "type": "Input.Text",
                            "id": "short_description",
                            "placeholder": "Descripción corta"
                        },
                        {
                            "type": "TextBlock",
                            "text": "Descripción",
                            "wrap": true
                        },
                        {
                            "type": "Input.Text",
                            "id": "description",
                            "placeholder": "Descripción",
                            "isMultiline": true
                        },
                        {
                            "type": "TextBlock",
                            "text": "Categoría"
                        }
                    ]
                },
                {
                    "type": "Column",
                    "width": 1,
                    "items": [
                        {
                            "type": "Image",
                            "url": "https://play-lh.googleusercontent.com/YbqEETD_H3qJanIFk8BzRP_jXEnJTPG9zmYEJyKwdTNMd34GHVZRyV8eOMbOQqhn3f0",
                            "size": "auto"
                        }
                    ]
                }
            ]
        },
        {
            "type": "Input.ChoiceSet",
            "choices": [
                {
                    "title": "Inquiry / Help",
                    "value": "inquiry"
                },
                {
                    "title": "Software",
                    "value": "software"
                }
            ],
            "placeholder": "Categoría",
            "id": "category"
        }
    ],
    "actions": [
        {
            "type": "Action.Submit",
            "title": "Submit"
        }
    ]
} 
'''