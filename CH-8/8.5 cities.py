def describe_city(city, country='bangladesh'):

    msg = f"{city.title()} is in {country.title()}."
    print(msg)


describe_city('dhaka')
describe_city('sakai', 'lithunia')
describe_city('khulna')
