from itertools import combinations
# function to calculate the intersection and percentage of all the combinations
def intersection_calculate(artist1,artist2):
    common_artist=artist1.intersection(artist2)
    percentage=len(common_artist)*10
    return percentage
kevin_artist={"Hasley",'Taylor Swift','Mitski','Joji','Shawn Mendes','Sabrina Carpenter',
       'Nicky Minaj','Conan Gray','One Direction','Justin Beiber'}
Stuart_artist={'Kendrick Lamar','Steve Lacy','Tyler the Creator','Joji','TheWeeknd','ColdPlay'
        'Kanye West','Travis Scott','Frank Ocean','Brent Faiyaz'}
Bob_artist={'Conan Gray','Joji','Dove Cameron','Mitski','ArcticMonkeys','Steve Lacy',
     'Kendrick Lamar','Isabel LaRosa','Shawn Mendes','Coldplay'}
Edith_artist={'Metallica','Billie Eilish','TheWeeknd','Mitski','NF','Conan Gray','Kendrick Lamar','Nicky Minaj','Kanye West','Coldplay'}

Djs={
    "Kevin":kevin_artist,
    "Stuart":Stuart_artist,
    "Bob":Bob_artist,
    'Edith':Edith_artist
}

pairs=list(combinations(Djs.keys(),2))
imp=[]

# verifying if the percentage is valid or not
for Dj1,Dj2 in pairs:
     cal=intersection_calculate(Djs[Dj1],Djs[Dj2])
     if(cal>=30):
          imp.append((Dj1,Dj2,cal))

imp.sort(key=lambda pair: pair[2], reverse=True)


# output the result
for Dj1,Dj2,cal in imp:
     print(f"pair:{Dj1,Dj2} has a overlap percentage of:{cal}"  )


