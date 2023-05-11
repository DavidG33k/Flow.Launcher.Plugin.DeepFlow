# Flow.Launcher.Plugin.DeepFlow

This plugin allows you to exploit the potential of [DeepL](https://www.deepl.com/) translations quickly using [FlowLauncher](https://www.flowlauncher.com/).

## How to use it:DeepFlow
1. Install the plugin with the command `pm install DeepFlow` or via the official FlowLauncher marketplace.

2. First you need to set your DeepL API key with the command `dp set-key <API-KEY>`. If you don't have one, you can get it for free at the link "https://www.deepl.com/pro-api" with some limitations, or by subscribing to the paid plan. You can change it as many times as you want.

3. After setting your API key you can translate with the following syntax:
    - `dp en:it Hello, World!` to translate the sentence "Hello, World!" from english to italian.  
    - `dp :it Hello, World!` to translate the sentence "Hello, World!" to italian, with autodetection of the initial language.
    - `dp : Hello, World!` to translate the sentence "Hello, World!" automatically to the default language english, with autodetection of the initial language.