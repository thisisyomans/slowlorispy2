from distutils.core import setup
setup(
    name = "Slowloris",
    py_modules = ["slowloris"],
    entry_points = {"console_scripts": ["slowloris=slowloris:main"]},
    version = "0.1.4",
    description = "Low bandwidth DoS tool. Slowloris rewrite in Python.",
    author = "Manas Taneja",
    author_email = "tanejamm@gmail.com",
    url = "https://github.com/thisisyomans/slowlorispy",
    keywords = ["dos", "http", "slowloris"]
)
