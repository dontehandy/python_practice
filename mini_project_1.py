# Exercise 1: Manipulate Text

# In the paragraph below, write a script to identify the longest sentence by word count.

'''
index0 - 20 words
index1 - 29 words
index2 - 21 words
index3 - 30 words
index4 - 36 words
index5 - 28 words
index6 - 33 words
index7 - 1 words ** ??

'''

unformatted_paragraph = """Nestled in the heart of the Pacific Northwest, Washington State is a mesmerizing blend of natural wonders and urban sophistication. 
Its geography is a tapestry of contrasts, stretching from the rugged Pacific coastlines to the dense, verdant rainforests of the Olympic Peninsula, culminating in the majestic Cascade Mountains. 
Among these peaks, Mt. Rainier stands as a sentinel, an active volcano and the pinnacle of the state’s natural beauty. 
This diverse terrain provides a playground for adventurers and nature lovers alike, offering an array of activities from serene hiking trails and challenging ski slopes to tranquil kayaking routes. 
Beyond its scenic landscapes, Washington's ecological diversity is a testament to its environmental richness, hosting an array of wildlife that includes the majestic orcas navigating the Puget Sound and elusive elk roaming the shadowy rainforests. 
This harmonious blend of natural beauty and wildlife creates a unique backdrop for the state, inviting both residents and visitors to immerse themselves in its outdoor wonders. 
Washington State, through its stunning geography and vibrant ecosystems, stands as a beacon of the Pacific Northwest's splendor, embodying the essence of adventure and the tranquility of nature in one cohesive landscape."""

replace_mt = unformatted_paragraph.replace("Mt.", "Mount") #turn mt to mount to target "."

each_sent = replace_mt.split(".") #split at "." - --the_list

word_counter = [] #emp list being built to put the space count into

for words in each_sent:
    count = words.count(" ") + 1
    word_counter.append(count)

word_counter.sort()

print(word_counter[-1])