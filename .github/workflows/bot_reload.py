name: Auto Commit Bot

on:
  schedule:
    - cron:  '0 */4 * * *'

jobs:
  bot-docker:
    runs-on: ubuntu-latest
    container:
      image: ubuntu:18.04
    steps:
         - name: Git Auto Commit TEST
           env:
             GIT_USER: ${{ secrets.GIT_USER }}
             GIT_PASSWORD: ${{ secrets.GIT_PASSWORD }}
           run: |
             apt update && apt install git -y
             git clone https://github.com/BobbySJohnson/bot.git
             sleep 4
             cd bot
             sleep 3
             echo "Done at ==> $(date)" >> time.txt
             sleep 3
             git config --global user.email "BOBBYS.JOHNSON@student.csn.edu"
             sleep 4
             git config credential.helper '!f() { sleep 1; echo "username=${GIT_USER}"; echo "password=${GIT_PASSWORD}"; }; f'
             sleep 2
             git branch -m master
             sleep 2
             git add .
             sleep 3
             git commit -am "Add time"
             sleep 5
             git push origin main
