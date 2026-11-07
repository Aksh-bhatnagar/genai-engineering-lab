def get_destinations(country):
    destinations = {
        "India": [
            "Goa", "Kerala", "Manali", "Jaipur", "Udaipur",
            "Mumbai", "Delhi", "Agra", "Rishikesh", "Shimla",
            "Darjeeling", "Ooty", "Munnar", "Leh", "Varanasi",
            "Andaman and Nicobar Islands", "Srinagar", "Coorg",
            "Amritsar", "Pondicherry"
        ],
        "Japan": [
            "Tokyo", "Kyoto", "Osaka", "Hiroshima", "Nara",
            "Sapporo", "Fukuoka", "Yokohama", "Hakone", "Okinawa",
            "Nagoya", "Kobe", "Nikko", "Kamakura"
        ],
        "France": [
            "Paris", "Nice", "Lyon", "Marseille", "Bordeaux",
            "Strasbourg", "Cannes", "Toulouse", "Lille",
            "Montpellier", "Avignon", "Annecy", "Colmar"
        ],
        "Italy": [
            "Rome", "Venice", "Florence", "Milan", "Naples",
            "Amalfi Coast", "Pisa", "Verona", "Bologna",
            "Siena", "Cinque Terre", "Turin"
        ],
        "United States": [
            "New York", "Los Angeles", "San Francisco", "Las Vegas",
            "Miami", "Chicago", "Seattle", "Boston", "Orlando",
            "Washington DC", "Honolulu", "San Diego", "Nashville"
        ],
        "United Kingdom": [
            "London", "Edinburgh", "Manchester", "Liverpool",
            "Oxford", "Cambridge", "Bath", "York", "Bristol",
            "Glasgow", "Birmingham", "Lake District"
        ],
        "Australia": [
            "Sydney", "Melbourne", "Brisbane", "Perth",
            "Gold Coast", "Adelaide", "Canberra", "Cairns",
            "Hobart", "Great Barrier Reef"
        ],
        "Switzerland": [
            "Zurich", "Geneva", "Lucerne", "Interlaken",
            "Zermatt", "Bern", "Lausanne", "Grindelwald",
            "Lauterbrunnen", "Montreux"
        ],
        "Thailand": [
            "Bangkok", "Phuket", "Pattaya", "Chiang Mai",
            "Krabi", "Koh Samui", "Ayutthaya", "Phi Phi Islands",
            "Hua Hin", "Chiang Rai"
        ],
        "Indonesia": [
            "Bali", "Jakarta", "Yogyakarta", "Lombok",
            "Ubud", "Bandung", "Komodo Island",
            "Gili Islands", "Surabaya"
        ],
        "Spain": [
            "Barcelona", "Madrid", "Seville", "Valencia",
            "Granada", "Malaga", "Ibiza", "Mallorca",
            "Bilbao", "Cordoba", "San Sebastian"
        ],
        "Germany": [
            "Berlin", "Munich", "Hamburg", "Frankfurt",
            "Cologne", "Dresden", "Heidelberg", "Stuttgart",
            "Nuremberg", "Black Forest"
        ],
        "United Arab Emirates": [
            "Dubai", "Abu Dhabi", "Sharjah", "Fujairah",
            "Ras Al Khaimah", "Al Ain"
        ],
        "Singapore": [
            "Marina Bay", "Sentosa Island", "Chinatown",
            "Little India", "Gardens by the Bay",
            "Orchard Road", "Clarke Quay"
        ],
        "Canada": [
            "Toronto", "Vancouver", "Montreal", "Ottawa",
            "Quebec City", "Banff", "Calgary", "Victoria",
            "Niagara Falls", "Whistler"
        ],
        "New Zealand": [
            "Auckland", "Queenstown", "Wellington", "Christchurch",
            "Rotorua", "Milford Sound", "Wanaka", "Dunedin"
        ],
        "South Korea": [
            "Seoul", "Busan", "Jeju Island", "Incheon",
            "Gyeongju", "Daegu", "Suwon"
        ],
        "Turkey": [
            "Istanbul", "Cappadocia", "Antalya", "Izmir",
            "Pamukkale", "Ankara", "Bodrum", "Fethiye"
        ],
        "Greece": [
            "Athens", "Santorini", "Mykonos", "Crete",
            "Rhodes", "Corfu", "Thessaloniki", "Zakynthos"
        ],
        "Egypt": [
            "Cairo", "Luxor", "Aswan", "Sharm El Sheikh",
            "Hurghada", "Alexandria", "Giza"
        ],
        "South Africa": [
            "Cape Town", "Johannesburg", "Durban",
            "Pretoria", "Kruger National Park",
            "Stellenbosch", "Garden Route"
        ],
        "Brazil": [
            "Rio de Janeiro", "Sao Paulo", "Salvador",
            "Brasilia", "Florianopolis", "Iguazu Falls",
            "Manaus"
        ],
        "Mexico": [
            "Mexico City", "Cancun", "Tulum", "Playa del Carmen",
            "Guadalajara", "Oaxaca", "Puerto Vallarta",
            "Merida", "Cabo San Lucas"
        ],
        "Maldives": [
            "Male", "Maafushi", "Hulhumale", "Addu City",
            "Baa Atoll", "Ari Atoll"
        ],
        "Nepal": [
            "Kathmandu", "Pokhara", "Chitwan", "Lumbini",
            "Nagarkot", "Everest Base Camp", "Bandipur"
        ],
        "Sri Lanka": [
            "Colombo", "Kandy", "Galle", "Ella",
            "Sigiriya", "Nuwara Eliya", "Mirissa",
            "Bentota", "Trincomalee"
        ]
    }

    return destinations.get(country.strip().title(), [])