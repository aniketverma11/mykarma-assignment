
# Mock Database of Mobile Phones

PHONES = [
    {
        "id": "pixel_8a",
        "name": "Google Pixel 8a",
        "brand": "Google",
        "price": 49999,
        "specs": {
            "processor": "Google Tensor G3",
            "ram": "8GB",
            "storage": "128GB",
            "display": "6.1-inch Actua display (OLED), 120Hz",
            "camera": "64MP Main, 13MP Ultrawide, 13MP Front",
            "battery": "4492 mAh, 18W charging",
            "os": "Android 14"
        },
        "features": ["Best-in-class camera AI", "7 years of updates", "VPN by Google One", "IP67 water resistance"],
        "description": "The AI-first phone at a lower price point. Great for photography enthusiasts."
    },
    {
        "id": "oneplus_12r",
        "name": "OnePlus 12R",
        "brand": "OnePlus",
        "price": 39999,
        "specs": {
            "processor": "Snapdragon 8 Gen 2",
            "ram": "8GB/16GB",
            "storage": "128GB/256GB",
            "display": "6.78-inch AMOLED ProXDR, 120Hz LTPO",
            "camera": "50MP Main (Sony IMX890), 8MP Ultrawide",
            "battery": "5500 mAh, 100W SUPERVOOC charging",
            "os": "OxygenOS 14 based on Android 14"
        },
        "features": ["Incredible battery life", "Super fast charging", "Smooth performance", "Trinity Engine"],
        "description": "Performance flagship killer with massive battery and top-tier display."
    },
    {
        "id": "samsung_s23_fe",
        "name": "Samsung Galaxy S23 FE",
        "brand": "Samsung",
        "price": 35000,
        "specs": {
            "processor": "Exynos 2200",
            "ram": "8GB",
            "storage": "128GB",
            "display": "6.4-inch Dynamic AMOLED 2X, 120Hz",
            "camera": "50MP Main, 12MP Ultrawide, 8MP Telephoto (3x)",
            "battery": "4500 mAh, 25W charging",
            "os": "One UI 6 (Android 14)"
        },
        "features": ["Telephoto lens", "Premium build", "Samsung DeX", "IP68 rating"],
        "description": "The fan edition bringing flagship features like telephoto camera to a mid-range price."
    },
    {
        "id": "nothing_phone_2a",
        "name": "Nothing Phone (2a)",
        "brand": "Nothing",
        "price": 23999,
        "specs": {
            "processor": "Dimensity 7200 Pro",
            "ram": "8GB",
            "storage": "128GB",
            "display": "6.7-inch Flexible AMOLED, 120Hz",
            "camera": "50MP Main, 50MP Ultrawide",
            "battery": "5000 mAh, 45W charging",
            "os": "Nothing OS 2.5 (Android 14)"
        },
        "features": ["Unique Glyph Interface", "Clean software experience", "Symmetrical bezels"],
        "description": "A design-focused phone with clean software and unique aesthetics."
    },
   {
        "id": "iphone_13",
        "name": "Apple iPhone 13",
        "brand": "Apple",
        "price": 48999,
        "specs": {
            "processor": "A15 Bionic",
            "ram": "4GB",
            "storage": "128GB",
            "display": "6.1-inch Super Retina XDR OLED",
            "camera": "12MP Main, 12MP Ultrawide",
            "battery": "3240 mAh",
            "os": "iOS 17"
        },
        "features": ["Cinematic mode", "Ceramic Shield", "FaceID", "Reliable ecosystem"],
        "description": "The reliable choice for entering the Apple ecosystem with great video capabilities."
    },
    {
        "id": "moto_edge_50_pro",
        "name": "Motorola Edge 50 Pro",
        "brand": "Motorola",
        "price": 29999,
        "specs": {
            "processor": "Snapdragon 7 Gen 3",
            "ram": "8GB/12GB",
            "storage": "256GB",
            "display": "6.7-inch pOLED 1.5K, 144Hz",
            "camera": "50MP Main, 13MP Ultrawide, 10MP Telephoto",
            "battery": "4500 mAh, 125W charging",
            "os": "Hello UI (Android 14)"
        },
        "features": ["Pantone Validated Camera & Display", "IP68 water resistance", "Wireless charging"],
        "description": "A stylish phone with Pantone validation and rapid charging."
    },
    {
        "id": "realme_12_pro_plus",
        "name": "Realme 12 Pro+",
        "brand": "Realme",
        "price": 29999,
        "specs": {
            "processor": "Snapdragon 7s Gen 2",
            "ram": "8GB",
            "storage": "128GB",
            "display": "6.7-inch Curved AMOLED, 120Hz",
            "camera": "50MP Main, 64MP Periscope Telephoto (3x)",
            "battery": "5000 mAh, 67W charging",
            "os": "Realme UI 5.0"
        },
        "features": ["Periscope portrait camera", "Luxury watch design", "Curved display"],
        "description": "Brings periscope zoom capabilities to the sub-30k segment."
    },
     {
        "id": "redmi_note_13_pro_plus",
        "name": "Redmi Note 13 Pro+",
        "brand": "Xiaomi",
        "price": 31999,
        "specs": {
            "processor": "Dimensity 7200 Ultra",
            "ram": "8GB",
            "storage": "256GB",
            "display": "6.67-inch Curved AMOLED 1.5K, 120Hz",
            "camera": "200MP Main, 8MP Ultrawide",
            "battery": "5000 mAh, 120W charging",
            "os": "MIUI 14 / HyperOS"
        },
        "features": ["200MP Camera", "IP68 rating", "Curved display", "Leather back option"],
        "description": "Feature-packed mid-ranger with high resolution camera and fast charging."
    },
    {
        "id": "iqoo_neo_9_pro",
        "name": "iQOO Neo 9 Pro",
        "brand": "iQOO",
        "price": 34999,
        "specs": {
            "processor": "Snapdragon 8 Gen 2",
            "ram": "8GB",
            "storage": "128GB",
            "display": "6.78-inch LTPO AMOLED, 144Hz",
            "camera": "50MP Main (IMX920), 8MP Ultrawide",
            "battery": "5160 mAh, 120W charging",
            "os": "Funtouch OS 14"
        },
        "features": ["Dedicated gaming chip Q1", "Dual tone design", "Excellent performance"],
        "description": "Performance monster targeted at gamers and power users."
    },
    {
        "id": "poco_x6_pro",
        "name": "POCO X6 Pro",
        "brand": "POCO",
        "price": 26999,
        "specs": {
            "processor": "Dimensity 8300 Ultra",
            "ram": "8GB",
            "storage": "256GB",
            "display": "6.67-inch AMOLED 1.5K, 120Hz",
            "camera": "64MP Main, 8MP Ultrawide",
            "battery": "5000 mAh, 67W charging",
            "os": "HyperOS (Android 14)"
        },
        "features": ["Flagship level performance", "Slim bezels", "Wild Boost 2.0"],
        "description": "Unmatched performance in the under 30k segment."
    }
]
