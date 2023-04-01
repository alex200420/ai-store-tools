from app.core.config import DISCORD, DISCORD_ACCOUNT_TOKEN, DISCORD_SERVER_ID, DISCORD_CHANNEL_ID


class MidJourneyRequestTemplate(object):
    def __init__(self, prompt):
        self.prompt = prompt

    def get_imagine_template(self):
        imagine_template = self.parse_imagine_template(self.prompt)
        return imagine_template
    
    @staticmethod
    def get_headers(auth = DISCORD_ACCOUNT_TOKEN):
        return {
            'authorization' : auth.strip()
        }
    
    @staticmethod
    def parse_imagine_template(prompt):
        imagine_template = {
            "type":2,
            "application_id": DISCORD.mj.id,
            "guild_id": DISCORD_SERVER_ID,
            "channel_id": DISCORD_CHANNEL_ID,
            "session_id": DISCORD.mj.session,
            "data":{
                "version": DISCORD.mj.imagine.version,
                "id": DISCORD.mj.imagine.id,
                "name": DISCORD.mj.imagine.name,
                "type":1,
                "options":[
                    {
                        "type":3,
                        "name":"prompt",
                        "value": prompt
                    }
                ],
                "application_command":{
                    "id": DISCORD.mj.imagine.id,
                    "application_id": DISCORD.mj.id,
                    "version": DISCORD.mj.imagine.version,
                    "default_permission":True,
                    "default_member_permissions":None,
                    "type":1,
                    "nsfw":False,
                    "name":"imagine",
                    "description": DISCORD.mj.imagine.description,
                    "dm_permission":True,
                    "options":[
                        {
                        "type":3,
                        "name":"prompt",
                        "description":"The prompt to imagine",
                        "required":True
                        }
                    ]
                },
                "attachments":[
                    
                ]
            }
        }
        return imagine_template