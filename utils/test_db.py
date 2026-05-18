start_hour = 8
stop_hour = 18

def get_period_limits():
    return start_hour, stop_hour


courses = [
    {
        "id":"mth111",
        "department":["general"],
        "host_department":"mth",
        "level":100,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"phy111",
        "department":["general"],
        "host_department":"phy",
        "level":100,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"gst111",
        "department":["general"],
        "host_department":"gst",
        "level":100,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc101",
        "department":["general"],
        "host_department":"csc",
        "level":100,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc111",
        "department":["csc"],
        "host_department":"csc",
        "level":100,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc121",
        "department":["csc", "css"],
        "host_department":"csc",
        "level":100,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc181",
        "department":["general"],
        "host_department":"csc",
        "level":100,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"css101",
        "department":["css"],
        "host_department":"css",
        "level":100,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"css111",
        "department":["css"],
        "host_department":"css",
        "level":100,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"css121",
        "department":["css", "swe"],
        "host_department":"csc",
        "level":100,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"css181",
        "department":["css"],
        "host_department":"css",
        "level":100,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"int101",
        "department":["int"],
        "host_department":"int",
        "level":100,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"int111",
        "department":["int"],
        "host_department":"int",
        "level":100,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"int121",
        "department":["int", "csc"],
        "host_department":"int",
        "level":100,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"int181",
        "department":["int"],
        "host_department":"int",
        "level":100,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"swe101",
        "department":["swe"],
        "host_department":"swe",
        "level":100,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"swe111",
        "department":["swe"],
        "host_department":"swe",
        "level":100,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"swe121",
        "department":["swe", "csc"],
        "host_department":"swe",
        "level":100,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"swe181",
        "department":["swe"],
        "host_department":"swe",
        "level":100,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc201",
        "department":["csc"],
        "host_department":"csc",
        "level":200,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc211",
        "department":["csc"],
        "host_department":"csc",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc281",
        "department":["general"],
        "host_department":"csc",
        "level":200,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"css201",
        "department":["css"],
        "host_department":"css",
        "level":200,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"css211",
        "department":["css"],
        "host_department":"css",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"css281",
        "department":["css"],
        "host_department":"css",
        "level":200,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"int201",
        "department":["int"],
        "host_department":"int",
        "level":200,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"int211",
        "department":["int"],
        "host_department":"int",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"int281",
        "department":["int"],
        "host_department":"int",
        "level":200,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"swe201",
        "department":["swe"],
        "host_department":"swe",
        "level":200,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"swe211",
        "department":["swe"],
        "host_department":"swe",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"swe281",
        "department":["swe"],
        "host_department":"swe",
        "level":200,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc301",
        "department":["csc"],
        "host_department":"csc",
        "level":300,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc311",
        "department":["csc"],
        "host_department":"csc",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc381",
        "department":["csc"],
        "host_department":"csc",
        "level":300,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"css301",
        "department":["css"],
        "host_department":"css",
        "level":300,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"css311",
        "department":["css"],
        "host_department":"css",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"css381",
        "department":["css"],
        "host_department":"css",
        "level":300,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"int301",
        "department":["int"],
        "host_department":"int",
        "level":300,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"int311",
        "department":["int"],
        "host_department":"int",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"int381",
        "department":["int"],
        "host_department":"int",
        "level":300,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"swe301",
        "department":["swe"],
        "host_department":"swe",
        "level":300,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"swe311",
        "department":["swe"],
        "host_department":"swe",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"swe381",
        "department":["swe"],
        "host_department":"swe",
        "level":300,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc401",
        "department":["csc"],
        "host_department":"csc",
        "level":400,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc411",
        "department":["csc"],
        "host_department":"csc",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc481",
        "department":["csc"],
        "host_department":"csc",
        "level":400,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"css401",
        "department":["css"],
        "host_department":"css",
        "level":400,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"css411",
        "department":["css"],
        "host_department":"css",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"css481",
        "department":["css"],
        "host_department":"css",
        "level":400,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"int401",
        "department":["int"],
        "host_department":"int",
        "level":400,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"int411",
        "department":["int"],
        "host_department":"int",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"int481",
        "department":["int"],
        "host_department":"int",
        "level":400,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"swe401",
        "department":["swe"],
        "host_department":"swe",
        "level":400,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"swe411",
        "department":["swe"],
        "host_department":"swe",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"swe481",
        "department":["swe"],
        "host_department":"swe",
        "level":400,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc491",
        "department":["csc"],
        "host_department":"csc",
        "level":400,
        "frequency":2,
        "is_elective":True,
        "elective_group":"csc_400"
    },
    {
        "id":"css491",
        "department":["css"],
        "host_department":"css",
        "level":400,
        "frequency":2,
        "is_elective":True,
        "elective_group":"css_400"
    },
]

rooms = [
    {
        "id": "rm001",
        "name":"Computer Laboratory A",
        "department":"csc",
        "capacity":250,
        "is_shared":False
    },
    {
        "id": "rm002",
        "name":"Information Technology lab A",
        "department":"int",
        "capacity":250,
        "is_shared":False
    },
    {
        "id": "rm003",
        "name":"Software Engineering Lab A",
        "department":"swe",
        "capacity":250,
        "is_shared":False
    },
    {
        "id": "rm004",
        "name":"Cybersecurity lab A",
        "department":"css",
        "capacity":250,
        "is_shared":False
    },
    {
        "id": "rm005",
        "name":"Computing Auditorium",
        "department":"csc",
        "capacity":600,
        "is_shared":True
    },
    {
        "id": "rm006",
        "name":"Information Auditorium",
        "department":"int",
        "capacity":600,
        "is_shared":True
    },
    {
        "id": "rm007",
        "name":"Software Auditorium",
        "department":"swe",
        "capacity":600,
        "is_shared":True
    },
    {
        "id": "rm008",
        "name":"Cybersecurity Auditorium",
        "department":"css",
        "capacity":600,
        "is_shared":True
    },
    {
        "id": "rm009",
        "name": "General Lecture Hall A",
        "department": None,
        "capacity": 500,
        "is_shared": True
    }
]

lecturers = [
    {
        "id": "l001",
        "name":"John Doe",
        "workload":4,
        "tod":0
    },
    {
        "id": "l002",
        "name":"Jane Doe",
        "workload":5,
        "tod":1
    },
    {
        "id": "l003",
        "name":"Jack Doe",
        "workload":4,
        "tod":0
    },
    {
        "id": "l004",
        "name":"Mary Cainne",
        "workload":4,
        "tod":1
    },
    {
        "id": "l005",
        "name":"Max Lenner",
        "workload":5,
        "tod":1
    },
    {
        "id": "l006",
        "name":"John Damian",
        "workload":5,
        "tod":0
    },
    {
        "id": "l007",
        "name":"Jonathan Calmmer",
        "workload":4,
        "tod":0
    },
    {
        "id": "l008",
        "name":"Nathan Dam",
        "workload":4,
        "tod":1
    },
    {
        "id": "l009",
        "name":"Megan Keller",
        "workload":4,
        "tod":0
    },
    {
        "id": "l010",
        "name":"Vivian Sadist",
        "workload":5,
        "tod":1
    },
    {
        "id": "l011",
        "name":"Veronica Fisher",
        "workload":5,
        "tod":0
    },
    {
        "id": "l012",
        "name":"Sam Chaser",
        "workload":5,
        "tod":1
    },
    {
        "id": "l013",
        "name":"Ruth Veren",
        "workload":5,
        "tod":1
    },
    {
        "id": "l014",
        "name":"James Ryder",
        "workload":5,
        "tod":0
    }
]

assignments = {
    0:0,
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:10,
    11:11,
    12:12,
    13:13,
    14:0,
    15:1,
    16:2,
    17:3,
    18:4,
    19:5,
    20:6,
    21:7,
    22:8,
    23:9,
    24:10,
    25:11,
    26:12,
    27:13,
    28:0,
    29:1,
    30:2,
    31:3,
    32:4,
    33:5,
    34:6,
    35:7,
    36:8,
    37:9,
    38:10,
    39:11,
    40:12,
    41:13,
    42:0,
    43:1,
    44:2,
    45:3,
    46:4,
    47:5,
    48:6,
    49:7,
    50:8,
    51:9,
    52:10,
    53:11,
    54:12,
    55:13,
    56:0
}
departments = [
    "csc",
    "css",
    "swe",
    "int"
]

departments_2 = [
    "ift","csc", "cyb", "sen"
]

level_list = {
    "csc": {
            100: 150,
            200: 120,
            300: 100,
            400: 90
        },
    "css": {
            100: 120,
            200: 100,
            300: 95,
            400: 78
        },
    "int": {
            100: 140,
            200: 130,
            300: 115,
            400: 100
        },
    "swe": {
            100: 120,
            200: 105,
            300: 100,
            400: 90
        }
}

level_list_2 = {
    "csc":{
            100: 150,
            200: 120,
            300: 100,
            400: 90
        },
    "cyb": {
            100: 120,
            200: 100,
            300: 95,
            400: 78
        },
    "ift": {
            100: 140,
            200: 130,
            300: 115,
            400: 100
        },
    "sen": {
            100: 120,
            200: 105,
            300: 100,
            400: 90
        }
}

global_settings = {
    "timeslot_data": {
        "start_hour": 8,
        "stop_hour": 18
    },
    "level_list": {
        "csc": {
            100: 150,
            200: 120,
            300: 100,
            400: 90
        },
        "css": {
            100: 120,
            200: 100,
            300: 95,
            400: 78
        },
        "int": {
            100: 140,
            200: 130,
            300: 115,
            400: 100
        },
        "swe": {
            100: 120,
            200: 105,
            300: 100,
            400: 90
        }
    },
    "days": 5
}

courses_2 = [
    {
        "id":"cos101",
        "department":["general"],
        "host_department":"csc",
        "level":100,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"gst111",
        "department":["general"],
        "host_department":"gst",
        "level":100,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"mth101",
        "department":["general"],
        "host_department":"mth",
        "level":100,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"phy101",
        "department":["general"],
        "host_department":"phy",
        "level":100,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"phy107",
        "department":["general"],
        "host_department":"phy",
        "level":100,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"sta111",
        "department":["general"],
        "host_department":"mth",
        "level":100,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"num_cos103",
        "department":["cyb", "csc"],
        "host_department":"int",
        "level":100,
        "frequency":2,
        "is_elective":True,
        "elective_group":"cyb"
    },
    {
        "id":"num_ift101",
        "department":["cyb", "ift"],
        "host_department":"csc",
        "level":100,
        "frequency":3,
        "is_elective":True,
        "elective_group":"cyb"
    },
    {
        "id":"cos201",
        "department":["general"],
        "host_department":"csc",
        "level":200,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"cyb201",
        "department":["cyb"],
        "host_department":"cyb",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"cyb203",
        "department":["cyb"],
        "host_department":"cyb",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ent211",
        "department":["general"],
        "host_department":"gst",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"num_cyb205",
        "department":["cyb"],
        "host_department":"cyb",
        "level":200,
        "frequency":2,
        "is_elective":True,
        "elective_group":"cyb_200"
    },
    {
        "id":"num_cyb207",
        "department":["cyb"],
        "host_department":"cyb",
        "level":200,
        "frequency":2,
        "is_elective":True,
        "elective_group":"cyb_200"
    },
    {
        "id":"num_ift201",
        "department":["cyb"],
        "host_department":"cyb",
        "level":200,
        "frequency":2,
        "is_elective":True,
        "elective_group":"cyb_200"
    },
    {
        "id":"sen201",
        "department":["csc", "cyb", "sen"],
        "host_department":"sen",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc309",
        "department":["general"],
        "host_department":"csc",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"cyb301",
        "department":["cyb"],
        "host_department":"cyb",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"cyb303",
        "department":["cyb"],
        "host_department":"cyb",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"cyb305",
        "department":["cyb"],
        "host_department":"cyb",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"num_cyb313",
        "department":["cyb"],
        "host_department":"cyb",
        "level":300,
        "frequency":2,
        "is_elective":True,
        "elective_group":"cyb_300"
    },
    {
        "id":"num_cyb309",
        "department":["cyb"],
        "host_department":"cyb",
        "level":300,
        "frequency":2,
        "is_elective":True,
        "elective_group":"cyb_300"
    },
    {
        "id":"num_cyb307",
        "department":["cyb"],
        "host_department":"cyb",
        "level":300,
        "frequency":2,
        "is_elective":True,
        "elective_group":"cyb_300"
    },
    {
        "id":"cyb409",
        "department":["cyb"],
        "host_department":"cyb",
        "level":400,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"cyb401",
        "department":["cyb"],
        "host_department":"cyb",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"cyb403",
        "department":["cyb"],
        "host_department":"cyb",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"cyb405",
        "department":["cyb"],
        "host_department":"cyb",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"num_cyb407",
        "department":["cyb"],
        "host_department":"cyb",
        "level":400,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc181",
        "department":["csc"],
        "host_department":"csc",
        "level":100,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc201",
        "department":["csc"],
        "host_department":"csc",
        "level":200,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc211",
        "department":["csc", "cyb"],
        "host_department":"csc",
        "level":200,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc221",
        "department":["csc", "cyb"],
        "host_department":"csc",
        "level":200,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc241",
        "department":["csc"],
        "host_department":"csc",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc281",
        "department":["csc"],
        "host_department":"csc",
        "level":200,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"mth231",
        "department":["csc"],
        "host_department":"mth",
        "level":200,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"mth211",
        "department":["csc", "sen"],
        "host_department":"mth",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"mth261",
        "department":["csc", "ift"],
        "host_department":"csc",
        "level":100,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc301",
        "department":["csc", "sen"],
        "host_department":"csc",
        "level":300,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc311",
        "department":["csc", "sen"],
        "host_department":"csc",
        "level":300,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc321",
        "department":["csc"],
        "host_department":"csc",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc331",
        "department":["general"],
        "host_department":"csc",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc341",
        "department":["csc", "sen", "ift"],
        "host_department":"csc",
        "level":300,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc351",
        "department":["csc"],
        "host_department":"csc",
        "level":300,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc361",
        "department":["csc"],
        "host_department":"csc",
        "level":300,
        "frequency":2,
        "is_elective":True,
        "elective_group":"csc_300"
    },
    {
        "id":"csc371",
        "department":["csc"],
        "host_department":"csc",
        "level":300,
        "frequency":2,
        "is_elective":True,
        "elective_group":"csc_300"
    },
    {
        "id":"csc381",
        "department":["csc"],
        "host_department":"csc",
        "level":300,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc401",
        "department":["csc"],
        "host_department":"csc",
        "level":400,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc411",
        "department":["general"],
        "host_department":"csc",
        "level":400,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc421",
        "department":["csc", "sen"],
        "host_department":"csc",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc431",
        "department":["csc", "sen", "ift"],
        "host_department":"csc",
        "level":400,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc441",
        "department":["csc"],
        "host_department":"csc",
        "level":100,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc451",
        "department":["csc", "ift"],
        "host_department":"csc",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc461",
        "department":["csc"],
        "host_department":"csc",
        "level":400,
        "frequency":2,
        "is_elective":True,
        "elective_group":"csc_400"
    },
    {
        "id":"csc471",
        "department":["csc"],
        "host_department":"csc",
        "level":400,
        "frequency":2,
        "is_elective":True,
        "elective_group":"csc_400"
    },
    {
        "id":"csc481",
        "department":["csc"],
        "host_department":"csc",
        "level":400,
        "frequency":1,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"csc491",
        "department":["csc"],
        "host_department":"csc",
        "level":400,
        "frequency":2,
        "is_elective":True,
        "elective_group":"csc_400"
    },
    {
        "id":"sen301",
        "department":["sen"],
        "host_department":"sen",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"sen201",
        "department":["sen"],
        "host_department":"sen",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"sen401",
        "department":["sen"],
        "host_department":"sen",
        "level":400,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"sen211",
        "department":["sen"],
        "host_department":"sen",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"sen221",
        "department":["sen"],
        "host_department":"sen",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"sen311",
        "department":["sen"],
        "host_department":"sen",
        "level":300,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"sen321",
        "department":["sen"],
        "host_department":"sen",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"sen351",
        "department":["sen"],
        "host_department":"sen",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"sen361",
        "department":["sen"],
        "host_department":"sen",
        "level":300,
        "frequency":2,
        "is_elective":True,
        "elective_group":"sen_300"
    },
    {
        "id":"sen371",
        "department":["sen"],
        "host_department":"sen",
        "level":300,
        "frequency":2,
        "is_elective":True,
        "elective_group":"sen_300"
    },
    {
        "id":"sen421",
        "department":["sen"],
        "host_department":"sen",
        "level":400,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"sen431",
        "department":["sen"],
        "host_department":"sen",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"sen441",
        "department":["sen"],
        "host_department":"sen",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"sen461",
        "department":["sen"],
        "host_department":"sen",
        "level":400,
        "frequency":2,
        "is_elective":True,
        "elective_group":"sen_400"
    },
    {
        "id":"sen471",
        "department":["sen"],
        "host_department":"sen",
        "level":400,
        "frequency":2,
        "is_elective":True,
        "elective_group":"sen_400"
    },
    {
        "id":"sen481",
        "department":["sen"],
        "host_department":"sen",
        "level":400,
        "frequency":2,
        "is_elective":True,
        "elective_group":"sen_400"
    },
    {
        "id":"ift221",
        "department":["ift"],
        "host_department":"ift",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ift241",
        "department":["ift"],
        "host_department":"ift",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ift251",
        "department":["ift"],
        "host_department":"ift",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ift251",
        "department":["ift"],
        "host_department":"ift",
        "level":200,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ift301",
        "department":["ift"],
        "host_department":"ift",
        "level":300,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ift321",
        "department":["ift"],
        "host_department":"ift",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ift331",
        "department":["ift"],
        "host_department":"ift",
        "level":300,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ift341",
        "department":["ift"],
        "host_department":"ift",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ift351",
        "department":["ift"],
        "host_department":"ift",
        "level":300,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ift361",
        "department":["ift"],
        "host_department":"ift",
        "level":300,
        "frequency":2,
        "is_elective":True,
        "elective_group":"ift_300"
    },
    {
        "id":"ift371",
        "department":["ift"],
        "host_department":"ift",
        "level":300,
        "frequency":2,
        "is_elective":True,
        "elective_group":"ift_300"
    },
    {
        "id":"ift401",
        "department":["ift"],
        "host_department":"ift",
        "level":400,
        "frequency":3,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ift421",
        "department":["ift"],
        "host_department":"ift",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ift431",
        "department":["ift"],
        "host_department":"ift",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ift441",
        "department":["ift"],
        "host_department":"ift",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ift451",
        "department":["ift"],
        "host_department":"ift",
        "level":400,
        "frequency":2,
        "is_elective":False,
        "elective_group":None
    },
    {
        "id":"ift461",
        "department":["ift"],
        "host_department":"ift",
        "level":400,
        "frequency":2,
        "is_elective":True,
        "elective_group":"ift_400"
    },
    {
        "id":"ift471",
        "department":["ift"],
        "host_department":"ift",
        "level":400,
        "frequency":2,
        "is_elective":True,
        "elective_group":"ift_400"
    },
]

rooms_2 = [
    {
        "name":"Computer Laboratory A",
        "department":"csc",
        "capacity":250,
        "is_shared":False
    },
    {
        "name":"Computer Laboratory B",
        "department":"csc",
        "capacity":180,
        "is_shared":False
    },
    {
        "name":"Cybersecurity Laboratory A",
        "department":"cyb",
        "capacity":250,
        "is_shared":False
    },
    {
        "name":"Cybersecurity Laboratory B",
        "department":"cyb",
        "capacity":250,
        "is_shared":False
    },
    {
        "name":"IFT Laboratory A",
        "department":"ift",
        "capacity":250,
        "is_shared":False
    },
    {
        "name":"IFT Laboratory B",
        "department":"ift",
        "capacity":250,
        "is_shared":False
    },
    {
        "name":"SWE Laboratory A",
        "department":"sen",
        "capacity":250,
        "is_shared":False
    },
    {
        "name":"SWE Laboratory B",
        "department":"sen",
        "capacity":250,
        "is_shared":False
    },
    {
        "name":"Math room 1",
        "department":"mth",
        "capacity":250,
        "is_shared":False
    },
    {
        "name":"Physics Room 1",
        "department":"phy",
        "capacity":250,
        "is_shared":False
    },
    {
        "name":"GST room 1",
        "department":"gst",
        "capacity":450,
        "is_shared":True
    },
    {
        "name":"Computer Auditorium 1",
        "department":"csc",
        "capacity":500,
        "is_shared":True
    },
    {
        "name":"IFT Auditorium 1",
        "department":"ift",
        "capacity":500,
        "is_shared":True
    },
    {
        "name":"SWE Auditorium 1",
        "department":"sen",
        "capacity":500,
        "is_shared":True
    },
    {
        "name":"CYB Auditorium 1",
        "department":"cyb",
        "capacity":500,
        "is_shared":True
    },
    {
        "name":"NSLT5",
        "department":None,
        "capacity":550,
        "is_shared":True
    },
    {
        "name":"NSLT4",
        "department":None,
        "capacity":480,
        "is_shared":True
    },
    {
        "name":"Pav D",
        "department":None,
        "capacity":550,
        "is_shared":True
    },
    {
        "name":"Pav 2C",
        "department":None,
        "capacity":550,
        "is_shared":True
    },
]

assignments_2 = {
    0:1,
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:10,
    11:11,
    12:12,
    13:13,
    14:0,
    15:1,
    16:2,
    17:3,
    18:4,
    19:5,
    20:6,
    21:7,
    22:8,
    23:9,
    24:10,
    25:11,
    26:12,
    27:13,
    28:0,
    29:1,
    30:2,
    31:3,
    32:4,
    33:5,
    34:6,
    35:7,
    36:8,
    37:9,
    38:10,
    39:11,
    40:12,
    41:13,
    42:0,
    43:1,
    44:2,
    45:3,
    46:4,
    47:5,
    48:6,
    49:7,
    50:8,
    51:9,
    52:10,
    53:11,
    54:12,
    55:13,
    56:0,
    57:1,
    58:2,
    59:3,
    60:4,
    61:5,
    62:6,
    63:7,
    64:8,
    65:9,
    66:10,
    67:11,
    68:12,
    69:13,
    70:0,
    71:1,
    72:2,
    73:3,
    74:4,
    75:5,
    76:6,
    77:7,
    78:8,
    79:9,
    80:10,
    81:11,
    82:12,
    83:13,
    84:0,
    85:1,
    86:2,
    87:3,
    88:4,
    89:5,
}

time_size = 10

max_gen = 120
max_iter = 500
days = 5

#-------- advanced details-------

def get_iter_data():
    return max_iter

def get_table_details():
    return courses, lecturers, rooms, assignments, departments, time_size, max_gen, max_iter

#def get_dept():
    return departments


#def get_data():
    return courses, lecturers, rooms
def fetch_gen_data():
    return max_gen

def get_assignment():
    return assignments




def get_level_list():
    return level_list

def get_num_timeslots():
    num_timeslots = stop_hour - start_hour

    return num_timeslots

def get_days():
    return days

def get_mid_day():
    i = -1
    x = start_hour
    while x <= 12:
        i += 1
        x += 1
    return i
