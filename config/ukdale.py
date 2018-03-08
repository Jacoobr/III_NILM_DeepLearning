""" Config for the III dataset """


# Windows (training, validation, testing)
WINDOWS = {
    'train': {
        1: ("2013-04-12", "2015-07-01"),
        2: ("2013-05-22", "2013-10-03 06:16:00"),
        3: ("2013-02-27", "2013-04-01 06:15:05"),
        4: ("2013-03-09", "2013-09-24 06:15:14"),
        5: ("2014-06-29", "2014-09-01")
    },
    'unseen_activations_of_seen_appliances': {
        1: ("2015-07-02", None),
        2: ("2013-10-03 06:16:00", None),
        3: ("2013-04-01 06:15:05", None),
        4: ("2013-09-24 06:15:14", None),
        5: ("2014-09-01", None)
    },
    'unseen_appliances': {
        2: ("2013-05-22", None),
        5: ("2014-06-29", None),
    }
}
# Appliances
APPLIANCES = [
    'kettle',
    'microwave',
    'dish washer',
    'washing machine',
    'fridge',
]


# Training & validation buildings, and testing buildings
BUILDINGS = {
    'kettle': {
        'train_buildings': [1, 2 , 4],
        'unseen_buildings': [5],
    },
    'microwave': {
        'train_buildings': [ 1,2],
        'unseen_buildings': [5],
    },
    'washing machine': {
        'train_buildings': [1, 5],
        'unseen_buildings': [2],
    },
    'dish washer': {
        'train_buildings': [1,2],
        'unseen_buildings': [5],
    },
    'fridge': {
        'train_buildings': [ 1,2, 4],
        'unseen_buildings': [5],
    },
}
