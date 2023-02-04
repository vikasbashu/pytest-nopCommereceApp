"# pytest-nopCommereceApp" 
# addopts = -m "smoke" testCases\ --alluredir="Reports\" --html=Reports\report.html --browser edge


# pytest flags
# -r ->  shows extra test summary
# -v -> verbose. use to get more information
# -n -> parallel count
# -m -> marker
# -k -> keyword driven
# -s -> console output
# -rE -> test summary with Error only. default flag
 
# run parallel execution in suits mode
#py.test -v -n=2 -m "api or smoke" testCases\ --dist loadgroup 

# important xdist commands
# --dist load -> send pending task to any available worker
# --dist loadscope -> tests are grouped by module/class/methods. Groups are distributed to available worker as whole unit.
# --dist loadfile -> Tests are grouped by their containing file. Groups are distributed to available worker as whole unit.
# --dist loadgroup -> Tests are grouped by given group/suite name. Groups are distributed to available worker as whole unit.
# --dist worksteal -> Tests are distributed evenly among all available workers.
# --dist no -> one by one execution. No distribution at all.
