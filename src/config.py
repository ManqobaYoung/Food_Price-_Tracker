"""Configuration for Food Price Tracker

Contains store list and essential products used by scrapers and collector.
"""

STORES = ["Spar", "Checkers", "Boxer", "Shoprite", "Woolworths"]

ESSENTIAL_PRODUCTS = {
    "Staples": [
        "White bread (loaf)",
        "Maize meal (2.5 kg)",
        "Rice (2 kg)",
        "All-purpose flour (1-2 kg)",
        "Sugar (2 kg)",
    ],
    "Dairy & Eggs": [
        "Milk (1 L)",
        "Eggs (dozen)",
        "Butter / Margarine (250 g)",
        "Cheese (block)",
    ],
    "Proteins": [
        "Chicken portions (1 kg)",
        "Beef mince (1 kg)",
        "Canned pilchards (400 g)",
        "Dried beans / lentils (1 kg)",
    ],
    "Fresh produce": [
        "Potatoes (1 kg)",
        "Onions (1 kg)",
        "Tomatoes (1 kg)",
        "Carrots (1 kg)",
    ],
    "Cooking & condiments": [
        "Cooking oil (2 L)",
        "Salt (500 g)",
        "Instant coffee / tea",
    ],
    "Pantry & convenience": [
        "Pasta (500 g)",
        "Canned tomatoes (410 g)",
        "Breakfast cereal (medium box)",
    ],
    "Household & personal care": [
        "Toilet paper (4 pack)",
        "Bar soap / liquid soap",
        "Dishwashing liquid (750 ml)",
    ],
}
