# eCrew Development Program (eCDP) Italian Translation
This is a repository of the Italian translation of McDonald's [eCrew Development Program](https://en.wikipedia.org/wiki/ECrew_Development_Program).

Original repo and scripts are taken from [eCDP-English](https://github.com/eCDP-English/translation).

## Usage
1. Grab an original, unmodified ROM of McDonald's eCDP (SHA-1: `136aacc9d3d7c8567381cd4e735ff3c004a018d0`)
2. Download the [latest xdelta patch](https://github.com/eCDP-translations/eCDP-Italian/releases/download/v1.0.0/eCDP_Italian_v_1_0_0.xdelta)
3. Download [XDelta patcher](https://www.romhacking.net/download/utilities/704/) and place it into a folder.
4. In the same folder, place the unmodified ROM and the XDelta patch you have just downloaded. The original file will be overwritten by the patched one.
5. Enjoy!

## Manual patching
This section is for developers, to use the patch, just follow the instructions above.

### Requirements
1. [Python3.9+](https://www.python.org/downloads/), if unsure download the latest version
2. An original, unmodified ROM of McDonald's eCDP (SHA-1: `136aacc9d3d7c8567381cd4e735ff3c004a018d0`)
3. (optional) Git

### Usage
This guide is for patching all translations to your ROM. For patching individual sections, please check instructions inside corresponding directories.

0. Clone [or download](https://github.com/eCDP-translations/eCDP-Italian/archive/refs/heads/master.zip) this repository
```
git clone https://github.com/eCDP-translations/eCDP-Italian.git
```
1. (Optional) Create a new virtual environment and activate it. If unsure, skip this step.
2. Run  `pip install -r requirements.txt`
3. Place the NDS file into the root of this repository. The file could be named as you please, but through the guide, for the sake of simplicity, we'll refer to it as "eCDP.nds"
4. Run `patch_all.py` with the desired language code and ROM file specified

For any language, the command is:
```
python patch_all.py -l [LANG_CODE] eCDP.nds
```

For the Italian language, the command is:
```
python patch_all.py -l it eCDP.nds
```
5. The script will patch strings of all sections, and it will create a file named `\<ROM Filename\>-patched.nds`.
6. Enjoy your game! Bravo! 🎉 🇮🇹

## Repository Structure
The repository consists of 4 sections, one directory for each section:
- `arm9` - Translates ARM9 sections.
- `overlay` - Translates overlay files, which contain UI texts, as well as the game's compiled code.
- `bin` - Translates bin files, containing texts mainly for SOC Guides and Self Check.
- `cmcd` - Translates the "Challenge the McDonald's" section. Also replaces the font used there.
