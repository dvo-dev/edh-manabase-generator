from lands import get_fetch_lands, get_dual_lands, get_shock_lands, get_utility_lands
from get_card import get_card_by_name

if __name__ == "__main__":
    commander_name = input("Please enter the name of an EDH commander: ")
    colors = get_card_by_name(card_name=commander_name)["color_identity"]

    fetches = get_fetch_lands(colors=colors)
    duals = get_dual_lands(colors=colors)
    shocks = get_shock_lands(colors=colors)
    utilities = get_utility_lands(colors=colors)

    for land in (fetches + duals + shocks + utilities):
        print(land)
