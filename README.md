# search_completion
A simple program to autocomplete searches based on what Shakespeare would write.

---  
# Try it out  
Visit http://search.notincluded.org in your web-browser.  

---

# Quick Start
1. Install npm/nvm
```
brew install nvm 
brew install npm
```
2. Install node
```
brew install node@14
```
3. Install modules
```
npm cache clear --force
npm install
```
4. In a new terminal, start the back-end
```
source setup.sh
```

5. Start the front-end
```
npm start
```

6. In a new terminal, test the back-end is running
```
curl http://127.0.0.1:5000/prefix/fl/7
# note if this doesnt work on mac, you may need to disable airplay.
```
7. Now that both services are running, navigate in web-browser to http://localhost:3000
---
