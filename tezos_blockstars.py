import json, requests

def getMaximumOutfits(outfits, money):
    outfits_bought = 0
    for o in outfits:
        if o < money:
            money = money - o
            outfits_bought = outfits_bought + 1
        elif o == money:
            outfits_bought = outfits_bought + 1
            return outfits_bought
            break
        else:
            return outfits_bought
            break

def getCountries(s,p):
    criterion_met_count = 0
    base_url = "https://jsonmock.hackerrank.com/api/countries/search?name="
    paginated_country_api = base_url + s
    query_countries0 = requests.get(paginated_country_api)
    jsonified_country0 = query_countries0.json()
    total_pages = jsonified_country0.get('total_pages')
    if total_pages == 0:
        return criterion_met_count
    elif total_pages == 1:
        data_solopage1 = jsonified_country0.get('data')
        j = 0
        while j < len(data_solopage1):
            populace_val = data_solopage1[j]['population']
            if populace_val > p:
                criterion_met_count += 1
            j += 1
        return criterion_met_count
    else:
        for num in range(1, total_pages + 1):
            country_api = paginated_country_api + "&page=" + str(num)
            page_queried_countries = requests.get(country_api)
            jsonified_page_country = page_queried_countries.json()
            datalist_inpage = jsonified_page_country.get('data')
            i = 0
            while i < len(datalist_inpage):
                population_value = datalist_inpage[i]['population']
                if population_value > p:
                    criterion_met_count += 1
                i += 1
        return criterion_met_count

def arrangeEquipments(equipments):
    array_elements = equipments[0]

    return null

if __name__== "__main__":
    question10_sample_input_money = 5
    question10_sample_case0_input_outfits = [10,10,10]
    question10_sample_case1_input_outfits = [5,10,10]
    question10_sample_output0 = getMaximumOutfits(question10_sample_case0_input_outfits, question10_sample_input_money)
    question10_sample_output1 = getMaximumOutfits(question10_sample_case1_input_outfits, question10_sample_input_money)
    print (question10_sample_output0)
    print (question10_sample_output1)

    question11_sample_case0_input_s = "un"
    question11_sample_case0_input_p = 100090
    question11_sample_output = getCountries(question11_sample_case0_input_s, question11_sample_case0_input_p)
    print (question11_sample_output)
