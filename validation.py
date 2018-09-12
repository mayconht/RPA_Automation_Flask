

def __validator__(file):
    if "extend_demands" in file.lower():
        return __extenddemands__(file)
    elif "pop_mailers" in file.lower():
        return __popmailers__(file)
    elif "edit_seats" in file.lower():
        return __editseats__(file)


def __popmailers__(file):
    problems = []
    if(file.lower().endswith(('.csv'))):
        problems.append(True)
        return problems
    else:
        problems.append(False)
        problems.append("File extension not supported on popmailers, please upload a csv file")
        return problems

def __extenddemands__(file):
    problems = []
    if(file.lower().endswith(('.csv'))):
        problems.append(True)
        return problems
    else:
        problems.append(False)
        problems.append("File extension not supported on Extend Demands, please upload a csv file")
        return problems

def  __editseats__(file):
    problems = []
    if(file.lower().endswith(('.xls', 'xlsx'))):
        problems.append(True)
        return problems
    else:
        problems.append(False)
        problems.append("File extension not supported on Edit Seats, please upload a xls or xlsx file")
        return problems
