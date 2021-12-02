# Calculate the numbers in the order shown, do not change the order of the numbers.
# Replace each question mark with a mathematical sign. Plus, minus, multiply and divide can each be used once only.
# In which order should they be used to score 25? 6?5?7?2?3=25
import itertools

if __name__ == '__main__':
    for ops in itertools.permutations(['+', '-', '*', '/']):
        sum_str = ''.join([''.join(c) for c in zip(['6', '5', '7', '2'], ops)])

        step1 = eval(''.join(sum_str[0:3]))
        step2 = eval(str(step1) + ''.join(sum_str[3:5]))
        step3 = eval(str(step2) + ''.join(sum_str[5:7]))
        step4 = eval(str(step3) + str(sum_str[7]) + '3')

        if float(step4) == 25.0:
            print(''.join(sum_str) + '3==25')
