---
title: lm
---

A hastily made terminal command to ask chatgpt questions about using the terminal -- with message history.

![demo](demo.gif)

# Usage

```
lm how do i search for any file in this dir that has the text "test"
```
```
lm okay same command but this time search for text "test2"
```
```
lm how do i create a softlink?
```
```
lm how do i install htop?
```

# Installation

```bash
git clone https://github.com/mw3i/lm
cd lm
```

Set path to "$PYTHON" in `env` file

Download dependencies:
```bash
# Download dependencies
./init
```
(may need to run `chmod +x ./init`)

Add shortcut to your bashrc:
```bash
echo "alias lm=$(pwd)/run" >> ~/.bashrc
source ~/.bashrc
```
(^ once you move this dir the alias will be incorrect)

# Notes

- `./os` folder would be a symlink to the appropriate config location for the os, if this were to be crossplatform
