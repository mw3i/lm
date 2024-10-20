---
title: ok
---

A hastily made terminal command to ask chatgpt questions about using the terminal -- with message history.

# Usage

```bash
ok how do i search for any file in this dir that has the text "test"
```
```bash
ok okay same command but this time search for text "test2"
```
```bash
ok how do i create a softlink?
```
```bash
ok how do i install htop?
```

# Installation

```bash
git clone "repo-url"
cd okay
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
echo "alias ok=$(pwd)/run" >> ~/.bashrc
source ~/.bashrc
```
(^ once you move this dir the alias will be incorrect)

# Notes

- `./os` folder would be a symlink to the appropriate config location for the os

