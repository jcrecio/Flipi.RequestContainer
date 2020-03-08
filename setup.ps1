// It requires python3 to work (including pip)

// Install virtualvenv
python -m pip install virtualenv

// Create virtual environment
py -3 -m venv vRequestContainer

 // You need to make sure you have execution policies enabled in powershell
 // Run as an administrator:
 Set-ExecutionPolicy RemoteSigned

// Activate the environment
./vRequestContainer/Scripts/Activate.ps1

// Install flask
pip install Flask

// Install mongo
pip install mongo

// Install pymongo
pip install pymongo

