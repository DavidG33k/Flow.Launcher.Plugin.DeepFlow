# -*- coding: utf-8 -*-
"""

DeepFlow: DeepL Plugin for Flow Launcher.

Dev By Davide Gena (https://github.com/DavidG33k)

"""

import re
import json
import urllib.parse
import urllib.request
import subprocess

from flowlauncher import FlowLauncher, FlowLauncherAPI



with open('plugin/config.json', 'r') as f:
    config = json.load(f)

def translate(to_translate, to_language="en", from_language=""):

    if 'data' not in config or 'api-key' not in config['data']:
        API_KEY = ""
    else:
        API_KEY = config['data']['api-key']

    url_api_freeplan = 'https://api-free.deepl.com/v2/translate'
    url_api_proplan = 'https://api.deepl.com/v2/translate'
    agent = {'User-Agent': "Edge, Brave, Firefox, Chrome, Opera"}
    params = {
        'auth_key': API_KEY,
        'text': to_translate,
        'source_lang': from_language,
        'target_lang': 'en' if to_language == "" else to_language 
    }
    data = urllib.parse.urlencode(params).encode('utf-8')

    translation = ""

    try:
        request = urllib.request.Request(url_api_proplan, data=data ,headers=agent)
        response = urllib.request.urlopen(request)
        result = response.read()
    except:
        try:
            request = urllib.request.Request(url_api_freeplan, data=data ,headers=agent)
            response = urllib.request.urlopen(request)
            result = response.read()
        except:
            result = None

    if result is not None:
        json_result = json.loads(result)
        translation = json_result['translations'][0]['text']

    return translation
   


def copy2clip(txt):
    """Put translation into clipboard."""
    cmd = 'echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)


class deepL(FlowLauncher):

    def query(self, query):
        results = []

        # Online
        try:
            urllib.request.urlopen("https://www.deepl.com/translator")

            # print initial tutorial
            if len(query.strip()) == 0:
                results.append({
                    "Title": ":en text to translate",
                    "SubTitle": "Notation: 'dp :en your sentence' or 'dp it:en your sentence'\nRemember to set your API key with 'dp set-key <API-KEY>'",
                    "IcoPath": "Images/ico.png", "ContextData": "ctxData"})
                
            # API key setter with tutorial
            elif query.startswith('set-key'):
                if len(query.split()) == 2:
                    new_apikey = query[len("set-key"):].strip()
                    config['data']['api-key'] = new_apikey
                    with open('plugin/config.json', 'w') as f:
                        json.dump(config, f)

                    results.append({
                        "Title": "API key set successfully",
                        "SubTitle": "Your new API key: " + new_apikey,
                        "IcoPath": "Images/ico.png", "ContextData": "ctxData"})
                else:
                    results.append({
                        "Title": "Use 'set-key <API-KEY>' to set your DeepL API key\n(free or pro plan).",
                        "SubTitle": "You can get one for free at the link 'https://www.deepl.com/pro-api'.",
                        "IcoPath": "Images/ico.png", "ContextData": "ctxData"})

            # normal translation flow
            else:
                match = re.match(r'^(\w{0,2}):(\w{0,2})\s(.+)$', query)
                
                from_language=match.group(1)
                to_language=match.group(2)
                to_translate=match.group(3)

                translation = translate(
                    to_translate=to_translate, to_language=to_language, from_language=from_language)

                if translation == "":
                    results.append({
                        "Title": "Unable to translate! Invalid notation or incorrect API key or\ncharacters limit of the free plan exceeded.",
                        "SubTitle": "Please, Verify and try again.",
                        "IcoPath": "Images/ico.png", "ContextData": "ctxData"})
                else:    
                    results.append({
                        "Title": to_language + ": " + translation,
                        "SubTitle": from_language + ": " + to_translate,
                        "IcoPath": "Images/ico.png",
                        "ContextData": "ctxData",
                        "JsonRPCAction": {"method": "copy", "parameters": [translation], }})
        
        # Offline or invalid notation
        except:
            results.append({
                "Title": "Invalid Notation or No Internet Connection!",
                "SubTitle": "Please, Verify and try again.",
                "IcoPath": "Images/ico.png", "ContextData": "ctxData"})

        return results

    def copy(self, ans):
        """Copy translation to clipboard."""
        FlowLauncherAPI.show_msg("Copied to clipboard", copy2clip(ans))


if __name__ == "__main__":
    deepL()
