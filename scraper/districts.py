"""
Chautauqua County, NY — School District Configuration
18 public school districts with known staff directory URLs.

CMS types:
  "finalsite"  — uses Finalsite CMS; JSON API attempted first
  "wnyric"     — hosted on wnyric.org regional portal
  "stier"      — hosted on stier.org regional portal
  "html"       — plain HTML/WordPress; HTML parser used
  "unknown"    — CMS unknown; both strategies attempted
"""

DISTRICTS = [
    {
        "name": "Jamestown City SD",
        "base_url": "https://www.jpsny.org",
        "staff_url": "https://www.jpsny.org/facultystaff-directory",
        "cms": "finalsite",
    },
    {
        "name": "Fredonia CSD",
        "base_url": "https://www.fredonia.wnyric.org",
        "staff_url": "https://www.fredonia.wnyric.org/staff",
        "cms": "wnyric",
    },
    {
        "name": "Dunkirk City SD",
        "base_url": "https://www.dunkirkcsd.org",
        "staff_url": "https://www.dunkirkcsd.org/staff",
        "cms": "unknown",
    },
    {
        "name": "Bemus Point CSD",
        "base_url": "https://www.bemuspointcsd.org",
        "staff_url": "https://www.bemuspointcsd.org/staff",
        "cms": "unknown",
    },
    {
        "name": "Brocton CSD",
        "base_url": "https://www.broctoncsd.org",
        "staff_url": "https://www.broctoncsd.org/staff",
        "cms": "unknown",
    },
    {
        "name": "Cassadaga Valley CSD",
        "base_url": "https://www.cvcsd.stier.org",
        "staff_url": "https://www.cvcsd.stier.org/staff",
        "cms": "stier",
    },
    {
        "name": "Chautauqua Lake CSD",
        "base_url": "https://www.chautauqualakecs.org",
        "staff_url": "https://www.chautauqualakecs.org/staff",
        "cms": "unknown",
    },
    {
        "name": "Clymer CSD",
        "base_url": "https://www.clymercsd.org",
        "staff_url": "https://www.clymercsd.org/staff",
        "cms": "unknown",
    },
    {
        "name": "Falconer CSD",
        "base_url": "https://www.falconercsd.org",
        "staff_url": "https://www.falconercsd.org/staff",
        "cms": "unknown",
    },
    {
        "name": "Forestville CSD",
        "base_url": "https://www.forestvillecsd.org",
        "staff_url": "https://www.forestvillecsd.org/staff",
        "cms": "unknown",
    },
    {
        "name": "Frewsburg CSD",
        "base_url": "https://www.frewsburgcsd.org",
        "staff_url": "https://www.frewsburgcsd.org/staff",
        "cms": "unknown",
    },
    {
        "name": "Panama CSD",
        "base_url": "https://www.panamacsd.org",
        "staff_url": "https://www.panamacsd.org/staff",
        "cms": "unknown",
    },
    {
        "name": "Pine Valley CSD",
        "base_url": "https://www.pvcsd.org",
        "staff_url": "https://www.pvcsd.org/staff",
        "cms": "unknown",
    },
    {
        "name": "Southwestern CSD",
        "base_url": "https://www.swcsk12.org",
        "staff_url": "https://www.swcsk12.org/staff",
        "cms": "unknown",
    },
    {
        "name": "Ripley CSD",
        "base_url": "https://www.ripleycsd.org",
        "staff_url": "https://www.ripleycsd.org/staff",
        "cms": "unknown",
    },
    {
        "name": "Sherman CSD",
        "base_url": "https://www.shermancsd.org",
        "staff_url": "https://www.shermancsd.org/staff",
        "cms": "unknown",
    },
    {
        "name": "Silver Creek CSD",
        "base_url": "https://www.silvercreekschools.org",
        "staff_url": "https://www.silvercreekschools.org/staff",
        "cms": "unknown",
    },
    {
        "name": "Westfield CSD",
        "base_url": "https://www.westfieldacademy.org",
        "staff_url": "https://www.westfieldacademy.org/staff",
        "cms": "unknown",
    },
]

# Common staff directory path suffixes to try when the primary URL fails
STAFF_PATH_CANDIDATES = [
    "/staff",
    "/staff-directory",
    "/faculty-staff",
    "/facultystaff-directory",
    "/about/staff",
    "/about/staff-directory",
    "/district/staff-directory",
    "/directory",
    "/our-staff",
]
