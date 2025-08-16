# Simulator Configuration File

SIMULATOR_NAME = "DataDrivenWebAppSimulator"

# Data Sources
DATA_SOURCES = {
    "user_data": {
        "type": "csv",
        "file": "data/users.csv"
    },
    "product_data": {
        "type": "json",
        "file": "data/products.json"
    }
}

# Web App Settings
WEB_APP_SETTINGS = {
    "title": "Data Driven Web App Simulator",
    "description": "A simulator for building data-driven web applications",
    "base_url": "http://localhost:5000"
}

# Simulator Settings
SIMULATOR_SETTINGS = {
    "num_users": 1000,
    "num_products": 500,
    " simulation_duration": 3600,  # in seconds
    "update_interval": 10  # in seconds
}

# Metrics to Collect
METRICS = {
    "user_engagement": {
        "type": "counter",
        "description": "Total user engagement"
    },
    "product_views": {
        "type": "counter",
        "description": "Total product views"
    },
    "average_session_length": {
        "type": "timer",
        "description": "Average session length"
    }
}