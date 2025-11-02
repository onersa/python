# first_name = "vusi"
# last_name = "molapisi"
# full_name = first_name + " " +  last_name

# print(full_name)
# print(full_name.upper())
# print(full_name.lower())
# print(full_name.title())

# print(f"Hello, {full_name}. Welcome to the Python class")

# author = "albert einstein"
# quote = f"{author.title()} once said \"A person who never made"
# quote += " a mistake never tried anything new\""
# print(quote)

# USING STRIP() LSTRP() RSTRIP()
# first_name = "vusi   "
# last_name = "\tmolapisi"
# full_name = first_name.rstrip() + " " +  last_name.lstrip()
# print(full_name)

# REMOVING USING REMOVEPREFIX() AND REMOVESUFFIX() AND REPLACE()
my_url = "https://www.bokamoso.co.za/index.html"
print(my_url)
print(my_url.removeprefix("https://"))
print(my_url.removesuffix(".html"))
print(my_url.replace(".html",".HTMX"))