& .\env\Scripts\activate.ps1

#python -m pytest -v -s -m "launch" .\test_functionality\test_app_launching.py
#pytest -v -s -m "launch" .\test_functionality\test_app_launching.py --template=html1/index.html --report=Results/report.html
#pytest -v -s -m "launch" .\test_functionality\test_app_launching.py --html=Results/report.html
#pytest -v -s -m "ui_valid" .\test_functionality\test_morevalidation.py --html=Results/report.html


pytest -v -s -m "ui_valid" .\test_functionality\test_morevalidation.py --html=Results/report.html

# pytest -v -s -m "launch" .\test_utils\test_generic_methods.py

