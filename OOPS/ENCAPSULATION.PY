# class Sonnetai:

#     __privateapikey="rtghyuik5678"

#     def info(self):



#         return f"your api key {self.__privateapikey}"
    

# ai=Sonnetai()

# print(ai.info())



class Sonnetai:

    def __init__(self):
        self.__privateapikey = "rtghyuik5678"   # private variable

    # Getter method
    def get_api_key(self):
        return self.__privateapikey

    # Setter method with validation
    def set_api_key(self, new_key):
        if isinstance(new_key, str) and len(new_key) >= 5:
            self.__privateapikey = new_key
            print("API key updated successfully ✅")
        else:
            print("Invalid API key ❌ (minimum 5 characters required)")


# Object create
ai = Sonnetai()

# Getter use (read value)
print("Old API Key:", ai.get_api_key())

# Setter use (update value)
ai.set_api_key(1234)

# Again check
print("Updated API Key:", ai.get_api_key())