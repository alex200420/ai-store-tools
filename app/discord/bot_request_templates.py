import app.core.config as cfg


class MidJourneyRequestTemplate(object):
    def __init__(self, prompt):
        self.prompt = prompt

        self.headers = {
            'authorization' : cfg.DISCORD_ACCOUNT_TOKEN
        }
    
    def get_imagine_template(self):
        imagine_template = self.parse_imagine_template(self.prompt)
        return imagine_template
    
    @staticmethod
    def get_headers():
        return {
            'authorization' : cfg.DISCORD_ACCOUNT_TOKEN
        }
    
    @staticmethod
    def get_imagine_template(prompt):
        imagine_template = {
            "type":2,
            "application_id": cfg.discord_midjourney_app_id,
            "guild_id": cfg.DISCORD_SERVER_ID,
            "channel_id": cfg.DISCORD_CHANNEL_ID,
            "session_id": cfg.discord_midjourney_app_session,
            "data":{
                "version":cfg.discord_midjourney_img_cmd_version,
                "id": cfg.discord_midjourney_img_cmd_id,
                "name": cfg.discord_midjourney_img_cmd_name,
                "type":1,
                "options":[
                    {
                        "type":3,
                        "name":"prompt",
                        "value": prompt
                    }
                ],
                "application_command":{
                    "id": cfg.discord_midjourney_img_cmd_id,
                    "application_id": cfg.discord_midjourney_app_id,
                    "version": cfg.discord_midjourney_img_cmd_version,
                    "default_permission":True,
                    "default_member_permissions":None,
                    "type":1,
                    "nsfw":False,
                    "name":"imagine",
                    "description": cfg.discord_midjourney_img_cmd_description,
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