favorite_places = {
    'khari': ['cumilla', 'barishal', 'bhula'],
    'rahat': ['rangunia', 'noakhlai'],
    'mahir': ['dhaka', 'rangpur', 'rajshahi']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")