import pickle

# datalog = [totalXP, list of logs]
def save(dateTime, timeSpentMinutes, xpGained):
    dataLog = [0, []]
    sessionData = {
        'dateTime': dateTime,
        'timeSpentMinutes': timeSpentMinutes,
        'xpGained': xpGained
    }
    try:
        with open('log.pkl', 'rb') as f:
            dataLog = pickle.load(f)
            dataLog[0] += xpGained
            dataLog[1].append(sessionData)
        with open('log.pkl', 'wb') as f:
            pickle.dump(dataLog, f)
    except FileNotFoundError:
        with open('log.pkl', 'wb') as f:
            dataLog[0] = xpGained
            dataLog[1].append(sessionData)
            pickle.dump(dataLog, f)

def read():
    dataLog = [5, []]
    try:
        with open('log.pkl', 'rb') as f:
            dataLog = pickle.load(f)
        with open('log.pkl', 'wb') as f:
            pickle.dump(dataLog, f)
    except FileNotFoundError:
        pass
    return dataLog
