import petpy 

pf = Petfinder(JgABEROxapfiLrb1pjAHvsoZibygsYhpKiQ1WlmYZgqDxVAou8)

wa_female_cats = pf.pet_find(location='Seattle', 
                             animal='cat', 
                             sex='Female', 
                             count=100, 
                             return_df=True) 