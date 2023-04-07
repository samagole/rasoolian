phrase='!salam va vaght bekheyr !'
ph_list=list(phrase)
print(phrase)
print(ph_list)

new_phrase=''.join(ph_list[1:3])
new_phrase=new_phrase+''.join([ph_list[18],ph_list[19],ph_list[14],
                              ph_list[8],ph_list[22]])
#bayad sakhtar tak tak bashad dar join
print(ph_list)
print(new_phrase)
