states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()
while states_needed:
    best_station = None
    states_covered  = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        print(station)
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
    print(states_covered, final_stations)

print(final_stations)



# countries = set(["mne", "srb", "mcd", "bih", "hr", "slo", "rom", "alb"])

# couriers = {}
# couriers["c1"] = set(["mne", "srb", "bih"])
# couriers["c2"] = set(["mne", "alb"])
# couriers["c3"] = set(["alb", "rom"])
# couriers["c4"] = set(["slo", "mcd", "rom"])
# couriers["c5"] = set(["hr", "srb", "mcd"])

# final_couriers = set()
# while countries:
#    best_courier = None
#    countries_covered = set()
#    for courier, courier_countries in couriers.items():
#       courier_covers = courier_countries & countries
#       if len(courier_covers) > len(countries_covered):
#          best_courier = courier
#          countries_covered = courier_covers
#    countries -= countries_covered
#    final_couriers.add(best_courier)

# print(final_couriers)