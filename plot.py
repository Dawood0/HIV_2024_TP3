

import matplotlib.pyplot as plt
with open('plt/tnrnmthtml.txt') as f:
# with open('plt/tnrnmt.txt') as f:
    trnmnt=list(map(lambda x:float(x),f.read().split()))
    print(trnmnt)


# with open('plt/rndhtml.txt') as f:
# # with open('plt/rnd.txt') as f:
#     rnd=list(map(lambda x:float(x),f.read().split()))


# plt.plot(range(len(trnmnt)), trnmnt, label=f'TournmantSelection')
# plt.plot(range(len(rnd)), rnd, label=f'RandomSelection')
# print('-------------------')

# # Add labels and legend
# plt.xlabel('Iteration')
# plt.ylabel('Best Metric')
# plt.legend()

# # Show the plot
# plt.show() 


# with open('tnrnmt.txt','w') as f:
#     f.write('')

# with open('rnd.txt','w') as f:
#     f.write('')