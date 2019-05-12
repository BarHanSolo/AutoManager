import pickle

# An arbitrary collection of objects supported by pickle.
data = {
    "seed": "3815637451969779999516610984202742488888",
    "numberofteams": 10,
    "numberofraces": 20,
    "playercolors": [(0,0,7) ,(255,152,152) ,(120,52,70)],
    "driverscolors": [(148,0,211) ,(175,238,238) ,(139,0,139),
(255,228,196), (0,0,0), (123,104,238),
(0,0,0), (34,139,34) ,(0,0,0)]
}

with open('sav2', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
