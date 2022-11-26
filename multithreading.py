from threading import Thread

#hw: questions 1-3 on multithreading 

# def print_double(num):
#     print('The double of {} is {} '.format(num, num*2))
# double_maker = Thread(target = print_double, args = (10,))
# double_maker.start()
# print('Thread ended')

# def get_squares(start, end):
#     for num in range(start, end+1, 1):
#         print('The square of {} is {} '.format(num, num*num))
# square_thread = Thread(target = get_squares, args = (10,20))
# square_thread.start()
# square_thread.join()
# print('Message 1')
# print('Message 2')
# print('Message 3')

def prime_checker(num):
    prime = True
    for d in range(2, int(num**0.5) +1, 1):
        print('{} checked with {}'.format(num,d))
        if num % d == 0:
            prime = False
        if prime == True: 
            print('{} is a prime number'.format(num))
        else:
            print('{} is not a prime number'.format(num))

def primes(numbers):
    for num in numbers:
        t = Thread(target = prime_checker, args = (num,))
        t.start()
        # t.join()
        print('Completed task for {}!'.format(num))

prime_thread = Thread(target = primes, args = ([4483,4493,4507,4561,4567,4583,4591],))
prime_thread.start()
# prime_thread.join()
print('The program ended')