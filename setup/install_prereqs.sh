#!/bin/bash

# Install npm/nvm
brew install nvm
brew install npm

# Install node
brew install node@14

# Install modules
npm cache clear --force
npm install
