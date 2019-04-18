#!/bin/bash
#
# Created by: Letícia Bernardo
# Github: github.com/leticiabernardo
# License: MIT
# Copyright 2019
#
# Bash script to install the requirements of the project

PREVPWD=$(pwd)

if ! [ -x "$(command -v pip)" ]; then
  echo 'Error: pip is not installed.' >&2
  sudo python-pip
fi

sudo pip install --upgrade pip

if ! [ -x "$(command -v pip3)" ]; then
  sudo dnf reinstall python3-pip

  if ! [ -x "$(command -v pip3)" ]; then
    echo 'Error: pip3 is not installed. Checks your version of python3'
    exit
  fi
fi

if ! [ -x "$(command -v virtualenv)" ]; then
  sudo pip3 install virtualenv

  if ! [ -x "$(command -v virtualenv)" ]; then
    echo 'Error: virtualenv is not installed. Checks your version of pip3.'
    exit
  fi
fi


if [ ! -d "venv" ]; then
  sudo virtualenv venv

  if [ ! -d "venv" ]; then
    echo 'Error: The folder venv wasnt created. Try again.'
  fi
fi



if [ ! -f "config.py" ]; then
  #sudo cp config-dist.py config.py
  #sudo chmod +x config.py

  echo "# -------------------"
  echo
  echo "# Configurações: "
  echo
  echo "# -------------------"
  echo
  echo
  read -p "Digite seu INSTA_USERNAME []: "  insta_username
  read -p "Digite seu INSTA_PASSWORD []: " -s insta_pass
  echo
  read -p "Digite seu INSTA_TAGS_FOLLOW [amazing, beautiful, adventure]: " insta_tags
  read -p "Digite seu INSTA_UNFOLLOW_DISABLED [leh.ellen01]: "  insta_unfollow_disabled
  read -p "Digite seu INSTA_COPY_FOLLOWERS_FROM [leh.ellen01]: "  insta_copy_followers
  echo
  read -p "Digite seu FACEBOOK_USERNAME []: "  facebook_username
  read -p "Digite seu FACEBOOK_PASSWORD []: " -s facebook_pass
  echo

  insta_pass="$(echo -n "$insta_pass" | base64)"
  facebook_pass="$(echo -n "$facebook_pass" | base64)"

  if [ -z "$insta_tags" ]
  then
    insta_tags="amazing, beautiful, adventure"
  fi

  if [ -z "$insta_unfollow_disabled" ]
  then
    insta_unfollow_disabled="leh.ellen"
  fi

  if [ -z "$insta_copy_followers" ]
  then
    insta_copy_followers="leh.ellen"
  fi

cat > config.py <<-EOF
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Instagram Access and Configurations
"""
INSTA_USERNAME = "${insta_username}"
INSTA_PASSWORD = "${insta_pass}"
INSTA_TAGS_FOLLOW = "${insta_tags}"
INSTA_UNFOLLOW_DISABLED = "${insta_unfollow_disabled}"
INSTA_COPY_FOLLOWERS_FROM = "${insta_copy_followers}"
"""
Facebook Access and Configurations
"""
FACEBOOK_USERNAME = "${facebook_username}"
FACEBOOK_PASSWORD = "${facebook_pass}"
EOF

  #sudo vi config.py
fi


$PREVPWD/venv/bin/pip install -r requirements.txt
clear
$PREVPWD/venv/bin/python run.py


echo "Fim da execução..."

exit