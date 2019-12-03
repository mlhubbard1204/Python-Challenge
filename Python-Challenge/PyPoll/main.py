
import os
import csv

voters = os.path.join('Desktop','Python-Challenge','PyPoll','election_data.csv')


vote_count = {}


vote_percentage = {}


vote_total = 0

with open(voters, newline="") as csvfile:
    voterreader = csv.reader(csvfile, delimiter=",")

  
    next(voterreader)

    
    for row in voterreader:

        
        vote_total += 1

        
        if row[2] in vote_count:
            vote_count[row[2]] += 1

         
        else:
            vote_count[row[2]] = 1


winner_count = 0


for candidate in vote_count:
    

    vote_percentage[candidate] = (vote_count[candidate] / vote_total) * 100


    if vote_count[candidate] > winner_count:
        winner_count = vote_count[candidate]
        winner = candidate


results_path = os.path.join('election_results.txt')

with open(results_path, 'w', newline="") as txtfile:

    txtfile.write(f'''
Election Results

Total Votes: {vote_total}
\n''')

    print(f'''\nElection Results

Total Votes: {vote_total}
''')

    for candidate, votes in vote_count.items():
        txtfile.write(f'{candidate}: {vote_percentage[candidate]}% ({votes})\n')
        print(f'''{candidate}: {vote_percentage[candidate]}% ({votes})''')
    
    txtfile.write(f'''
Winner: {winner}
''')

    print(f'''
Winner: {winner}
''')

txtfile.close()