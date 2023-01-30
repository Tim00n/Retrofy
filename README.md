# Retrofy
Retrofy is a cross-platform retro gaming service, which lets you play, view and store all of your retro games in one place with upscaled resolution.

![image](https://user-images.githubusercontent.com/103383767/215564729-1692a3d3-8a63-4318-a9da-06e1a3bf6c85.png)
<p align="center"> 
Login screen
</p>

![image](https://user-images.githubusercontent.com/103383767/215565571-f9e056b3-f2c8-4dd3-bf12-9ebb28566f50.png)
<p align="center"> 
Library (Work in progress)
</p>

![image](https://user-images.githubusercontent.com/103383767/215565951-379ae868-d990-442b-a81b-584760df9803.png)
<p align="center"> 
Running already dumped games via Dolphin Emulator from Retrofy
</p>

Planned features include:
- An integrated hub for accessing your games, account information and configuration all in one easy to use interface
- Support for the major platforms: Windows 11, Windows 10, macOS and Linux
- Universal controller support
- Save and load states
- Screenshot media library and achievements manager
- Ability to track play time per game


# Requirements

Currently, Retrofy is by and large a solo project. All help - especially in the form of pull requests or direct help - is greatly appreciated. For ease of communication, here are some components that need to be overhauled and/or coded:

- UI/UX: Better color gradients, shades, borders and transitions. Focus on minimalism and not so "in your face"
- A solution for the login form so a database of hundreds of thousands of usernames can be input and queried
- A display method for all of the games in a users library
- Natively integrating Dolphin Emulator and Citra Emulator into the codebase so that it can run game files from inside of Retrofy

# Summary of Retrofy's technical workings

At its core Retroy is an amalgamation of multiple different emulator engines, which emulate different home video game consoles depending on the input source (i.e game) that is being played. Retrofy itself only ever unites all of these different emulators into one singular interface for ease of use so that the user can access any game at any time without having to swap between applications.


# Supported video game consoles

At launch Retrofy will focus on the following systems first:
1. Nintendo GameCube
2. Nintendo Wii
3. Nintendo 3ds


After a long initial trial and error / test phase Retrofy will add the following additional systems:
1. Playstation 1-3
2. Sega Saturn
3. GBA/GBC
4. N64
5. NES
6. SNES
7. Nintendo DS
8. Atari

Eventually Retrofy should be able to run most older systems.
