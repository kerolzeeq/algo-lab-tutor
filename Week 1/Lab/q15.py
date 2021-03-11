import time
import random
import string

start_time=time.time()
def password(user_input):
    special_character = [random.choice(string.punctuation) for character in range(user_input)]
    word_lower = [random.choice(string.ascii_lowercase) for lower in range(user_input)]
    word_upper = [random.choice(string.ascii_uppercase) for upper in range(user_input)]
    numbers = [random.choice(string.digits) for number in range(user_input)]
    generated_password = ''.join(special_character + word_lower + word_upper + numbers)
    generated_password = ''.join(random.choice(generated_password) for value in range(user_input))
    return generated_password

question = eval(input('Please enter the password length: '))
answer = password(question)
print(answer)
end_time = time.time()
print(f'Time-Complexity : {end_time-start_time}')