# Installation

### NVM - Node Version Manager
This will help us keep track of what version of nodejs we are using and it'll make upgrading versions much easier.

Or goal will be to keep the website compatable with the current LTS release posted on the nodejs.org website.

`git clone https://github.com/creationix/nvm.git ~/nvm`

`source ~/nvm/nvm.sh`

Now install the targeted version of Node, currently v8.9.4.

`nvm install 8.9.4`

### Cloning the website

Clone the website repo.

`git clone https://github.com/USUFSLC/website.git`

Now if you're just going to test or run this locally you can go ahead and run 'node server.js' go to localhost:1337 and you're all set.

If it's going live you'll need to go in and edit the port number to port 80. It's just in the server.js file right after the require() statements.
