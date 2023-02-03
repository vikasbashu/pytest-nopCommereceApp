rem py.test -v -s -m "sanity or regression" --html=Reports/report.html testCases/ --browser edge
rem py.test -v -s -m "regression" --html=Reports/report.html testCases/ --browser edge
rem py.test -v -s -m "sanity and regression" --html=Reports/report.html testCases/ --browser edge
rem py.test -v -s -m "smoke or regression" --html=Reports/report.html testCases/ --browser edge
rem py.test -v -s -m "smoke" --html=Reports/report.html testCases/ --browser edge
rem py.test -v -s -m "sanity" --html=Reports/report.html testCases/ --browser edge
rem py.test -v -s -m "smoke or sanity" --html=Reports/report.html testCases/ --browser edge
py.test -v -s -m "smoke and sanity" --html=Reports/report.html testCases/ --browser edge