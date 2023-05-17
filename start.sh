if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/HS-BOTZ/test1.git /Sita
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Sita
fi
cd /Sita
pip3 install -U -r requirements.txt
echo "ꜱɪᴛᴀ🧚ꜱᴛᴀʀᴛ⚡...."
python3 bot.py
