class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

    def get_count(self):
        return self.__secretCount

# Example: Tracking user login attempts
login_counter = JustCounter()

# Simulating user login attempts
login_counter.count()  # User attempts to log in
login_counter.count()  # User attempts to log in again

print("Total Login Attempts: ", login_counter.get_count())
