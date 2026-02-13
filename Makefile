setup:
	py -m pip install -r requirements.txt"C:\Users\Usama\AppData\Local\Programs\Python\Python313\python.exe" -m pip install --upgrade pip./make.exe setup
download-data:
	"C:\Users\Usama\AppData\Local\Programs\Python\Python313\python.exe" scripts/download_data.py
preprocess: 
	"C:\Users\Usama\AppData\Local\Programs\Python\Python313\python.exe" scripts/preprocess.py
feature:
	"C:\Users\Usama\AppData\Local\Programs\Python\Python313\python.exe" scripts/feature_engineering.py
train:
	"C:\Users\Usama\AppData\Local\Programs\Python\Python313\python.exe" scripts/train_model.py
