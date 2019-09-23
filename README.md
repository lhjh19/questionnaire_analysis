# questionnaire_analysis
This repository is for collecting, analysing and presenting questionnaire data for LingHangJiHua project.

# preparations for successfully running python scripts
1. install pip
	sudo python get-pip.py
2. install libraries if first time user
	recommend python3 on mac os, since python 2.x is system pre-installed and has a lot of permission issues during installation
	(python3 -m) pip install xlrd
    (python3 -m) pip install openpyxl
	(python3 -m) pip install pandas
3. run python main.py
	3.1 if you failed with following error, run this "sudo pip install --upgrade six --user"
		File "/Library/Python/2.7/site-packages/retrying.py", line 47, in wrap
    		@six.wraps(f)
		AttributeError: 'module' object has no attribute 'wraps'
