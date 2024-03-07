pytest -v -s .\testCases\test_LoginMercury.py -m sanity
rem pytest -v -s -m 'sanity or regression'  --html = ./Reports/report.html  --browser chrome