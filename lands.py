DUAL_LANDS = [
    {"name": "Tundra", "colors": {"W", "U"}},
    {"name": "Underground Sea", "colors": {"U", "B"}},
    {"name": "Badlands", "colors": {"B", "R"}},
    {"name": "Taiga", "colors": {"R", "G"}},
    {"name": "Savannah", "colors": {"G", "W"}},
    {"name": "Scrubland", "colors": {"W", "B"}},
    {"name": "Volcanic Island", "colors": {"U", "R"}},
    {"name": "Bayou", "colors": {"B", "G"}},
    {"name": "Plateau", "colors": {"W", "R"}},
    {"name": "Tropical Island", "colors": {"G", "U"}}
]

SHOCK_LANDS = [
    {"name": "Hallowed Fountain", "colors": {"W", "U"}},
    {"name": "Watery Grave", "colors": {"U", "B"}},
    {"name": "Blood Crypt", "colors": {"B", "R"}},
    {"name": "Stomping Ground", "colors": {"R", "G"}},
    {"name": "Temple Garden", "colors": {"G", "W"}},
    {"name": "Godless Shrine", "colors": {"W", "B"}},
    {"name": "Steam Vents", "colors": {"U", "R"}},
    {"name": "Overgrown Tomb", "colors": {"B", "G"}},
    {"name": "Sacred Foundry", "colors": {"W", "R"}},
    {"name": "Breeding Pool", "colors": {"G", "U"}}
]

FETCH_LANDS = [
    {"name": "Flooded Strand", "colors": {"W", "U"}},
    {"name": "Polluted Delta", "colors": {"U", "B"}},
    {"name": "Bloodstained Mire", "colors": {"B", "R"}},
    {"name": "Wooded Foothills", "colors": {"R", "G"}},
    {"name": "Windswept Heath", "colors": {"G", "W"}},
    {"name": "Marsh Flats", "colors": {"W", "B"}},
    {"name": "Scalding Tarn", "colors": {"U", "R"}},
    {"name": "Verdant Catacombs", "colors": {"B", "G"}},
    {"name": "Arid Mesa", "colors": {"W", "R"}},
    {"name": "Misty Rainforest", "colors": {"G", "U"}}
]

SLOW_LANDS = [
    {"name": "Deserted Beach", "colors": {"W", "U"}},
    {"name": "Shipwreck Marsh", "colors": {"U", "B"}},
    {"name": "Haunted Ridge", "colors": {"B", "R"}},
    {"name": "Rockfall Vale", "colors": {"R", "G"}},
    {"name": "Overgrown Farmland", "colors": {"G", "W"}},
    {"name": "Shattered Sanctum", "colors": {"W", "B"}},
    {"name": "Stormcarved Coast", "colors": {"U", "R"}},
    {"name": "Deathcap Glade", "colors": {"B", "G"}},
    {"name": "Sundown Pass", "colors": {"W", "R"}},
    {"name": "Dreamroot Canal", "colors": {"G", "U"}}
]

TRIOMES = [
    {"name": "Indatha Triome", "colors": {"W", "B", "G"}},
    {"name": "Raugrin Triome", "colors": {"U", "R", "W"}},
    {"name": "Zagoth Triome", "colors": {"B", "G", "U"}},
    {"name": "Savai Triome", "colors": {"R", "W", "B"}},
    {"name": "Ketria Triome", "colors": {"G", "U", "R"}},
    {"name": "Jetmir's Garden", "colors": {"W", "G", "R"}},
    {"name": "Ziatora's Proving Ground", "colors": {"B", "R", "G"}},
    {"name": "Xander's Lounge", "colors": {"U", "B", "R"}},
    {"name": "Raffine's Tower", "colors": {"W", "U", "B"}},
    {"name": "Spara's Headquarters", "colors": {"G", "W", "U"}}
]

def get_fetch_lands(colors: [str]) -> [str]:
    fetch_lands = []
    for land in FETCH_LANDS:
        if any(color in land["colors"] for color in colors):
            fetch_lands.append(land["name"])

    return fetch_lands

def get_dual_lands(colors: [str]) -> [str]:
    dual_lands = []
    colors_set = set(colors)
    for land in DUAL_LANDS:
        if land["colors"].issubset(colors_set):
            dual_lands.append(land["name"])

    return dual_lands

def get_shock_lands(colors: [str]) -> [str]:
    shock_lands = []
    colors_set = set(colors)
    for land in SHOCK_LANDS:
        if land["colors"].issubset(colors_set):
            shock_lands.append(land["name"])

    return shock_lands
