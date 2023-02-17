import requests_oauthlib
from requests_oauthlib import OAuth2Session

client_id = "Mother Dairy Farms"
client_secret = "9ea39a6e2fb7a58b879f832b41346a1b"
access_scope = ['barn-unlock', 'toiletseat-down', 'chickens-feed', 'eggs-collect', 'eggs-count', 'profile']
grant_type = "Client Credentials"
access_token_url = "http://coop.apps.symfonycasts.com/token"
redirect_uri = "https://www.toycart.com"

oath = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri, scope=access_scope)
token = oath.fetch_token(access_token_url, client_secret=client_secret, authorization_response=access_token_url)
print(token)