import spacy
from models import Profile, User
from backend.settings import DEFAULT_RANK_TOLERANCE, GOAL_SIMILARITY_THRESH

import csv
with open(r'C:\Users\Jacob\Documents\LaddrBase\laddr\backend\matching\LolDuoCsv.csv','r') as f:
    reader = csv.reader(f)
    bios = list(reader)

nlp = spacy.load('en_core_web_md')

doc1=nlp(u"I hate to play chess.")
doc2=nlp(u"I love to play chess.")

goals=nlp(bios)

with open(r'C:\Users\Jacob\Documents\LaddrBase\laddr\backend\matching\nlpresults.csv',mode='w') as nlpresults:
    nlp_writer = csv.writer(nlpresults,delimiter=",")
    for bio in bios:
        for bio2 in bios:
            biostr = ''.join(bio)
            bio2str = ''.join(bio2)
            bionlp = nlp(biostr)
            bio2nlp = nlp(bio2str)
            biosims=bionlp.similarity(bio2nlp)
            nlp_writer.writerow([biostr,bio2str,biosims])


#sorting test
 #The skeleton of this function would basically be to load in the current user's goal, and compare it against all other filtered user goals.
        #Then, you would sort the filtered_matches list by the goal similarity score. 
        print("Considering goal")
        # nlp = spacy.load('en_core_web_md')

        filtered_matches = Profile.objects.all()

        user_goal = Profile.objects.all()[1]
        user_goal_text = user_goal.goal
        user_nlp=nlp(user_goal_text)
        goallist = []

        for p in filtered_matches:
           match_goal = p.goal
           match_nlp = nlp(match_goal)
           goal_sim = user_nlp.similarity(match_nlp)
           #now add profile uuid and similarity to an array as a tuple
           goal_tuple = (p.uuid, goal_sim)
           #append each tuple to the goal list
           goallist.append(goal_tuple)
      
       # Now we order the filtered matches by goal similarity score
        goallist_asc=sorted(goallist,key=lambda x: x[1],reverse=True)
        goallist_asc_indexed=[]

        for idx,g in enumerate(goallist_asc):
            gi = g + (idx,)
            goallist_asc_indexed.append(gi)


        #sort (can't sort a query set by the results of a list so FFFFF. Left off here. 
        # #)
        filtered_matches.sort(key= lambda x: goallist_asc.index(x[1]))

        mapping = dict(filtered_matches)

        filtered_matches[:]=[(uuid,mapping[uuid]) for uuid in goallist]

        #attempt 2
        ids = [goallist_asc_indexed[:][2] for goal_sim in goallist_asc_indexed]
        
        #attmpt 3 (this works!)
        uuid_list=[]
        for u in goallist_asc_indexed:
            uuid_list.append(u[0])
        
         from django.db.models import Case,When
         preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(uuid_list)])
         filtered_matches_ordered = Profile.objects.filter(pk__in=uuid_list).order_by(preserved)

        #final code for matching:
        filtered_matches = Profile.objects.all()

        user_goal = Profile.objects.all()[1]
        user_goal_text = user_goal.goal
        user_nlp=nlp(user_goal_text)
        goallist = []
        
        for p in filtered_matches:
           match_goal = p.goal
           match_nlp = nlp(match_goal)
           goal_sim = user_nlp.similarity(match_nlp)
           #now add profile uuid and similarity to an array as a tuple
           goal_tuple = (p.uuid, goal_sim)
           #append each tuple to the goal list IF MATCH IS GREATER THAN THRESHOLD.
           if (goal_sim>GOAL_SIMILARITY_THRESH):
               goallist.append(goal_tuple)
    
        # Now we order the filtered matches by goal similarity score
        goallist_asc=sorted(goallist,key=lambda x: x[1],reverse=True)

        
        #Then we grab the uuids in order
        uuid_list=[]
        for u in goallist_asc_indexed:
            uuid_list.append(u[0])
        
        #Finally, use django Case,When to build a new queryset that preserves the order from the uuid_list which has been ordered by similarity score
        from django.db.models import Case,When
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(uuid_list)])
        filtered_matches_goal_ordered = Profile.objects.filter(pk__in=uuid_list).order_by(preserved)
        




