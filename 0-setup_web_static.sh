#!/usr/bin/env bash
# setup web server to deploy web_static

# Install server
sudo apt-get update -y
sudo apt-get install nginx -y

# Make web directories
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/

# Make simple HTML file
sudo touch /data/web_static/releases/test/index.html
sudo echo -e "<html>
<body>
This is a website
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic links
LINK="/data/web_static/current"
if [ -e $LINK ]; then
   # echo "File $LINK exists."
   sudo rm /data/web_static/current
   sudo ln -s /data/web_static/releases/test/ /data/web_static/current
else
   # echo "File $LINK does not exist."
   sudo ln -s /data/web_static/releases/test/ /data/web_static/current
fi

# Change ownership
sudo chown -R ubuntu:ubuntu /data/

# Alias hbnb_static
ALIAS='location \/hbnb_static\/ {\n                 alias \/data\/web_static\/current\/;\n                 autoindex off;\n         }\n'
sudo sed -i "30i$ALIAS" /etc/nginx/sites-available/default

# Restart nginx service
sudo service nginx restart
