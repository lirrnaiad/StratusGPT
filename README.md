# StratusGPT: Your AI Weather Companion

#### Video Demo:  https://youtu.be/VDBA5NHK-Oo

#### Description:
StratusGPT is a Discord bot created as a final project for CS50P: Introduction to Programming with Python. This bot provides weather information and access to an LLM (Dolphin 3.0 R1 Mistral 24b) with various commands.

## Files
- **project.py**: Where the main function is located, this file runs the bot and makes it online on Discord
- **utils/personality.py**: Stores the initial prompts or the "personality" prommpts for StratusGPT, one is for !prompt made for general questions, and the other one is for !wprompt and is used for prompts that are given weather data
- **cogs folder**: This folder is where the code of the commands are located
- **utils folder**: This folder is where .py files that interact with the API are stored

## Commands
- ``!stratusgpt``: Displays information about the bot and its commands.
- ``!weather [location]``: Provides weather information for a given location using the OpenWeatherMap API.
- ``!prompt [prompt]``: Prompts the LLM with a given prompt.
- ``!wprompt [location]; [prompt]``: Prompts the LLM with a given prompt along with the weather info of a specified location.

## Usage
To add StratusGPT to your Discord server, use the following link:
[Add StratusGPT to your server](https://discord.com/oauth2/authorize?client_id=1338457849638027316&permissions=2048&integration_type=0&scope=bot)

## License
This project is licensed under the MIT License.
