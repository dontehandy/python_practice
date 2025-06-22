# Exercise 1: Manipulate Text

# In the paragraph below, write a script to identify the longest sentence by word count.

# answer sheet: 

'''
* **Sentence 1:** 17 words
* **Sentence 2:** 27 words
* **Sentence 3:** 20 words
* **Sentence 4:** 27 words
* **Sentence 5:** 35 words
* **Sentence 6:** 27 words
* **Sentence 7:** 33 words
'''


unformatted_paragraph = """Nestled in the heart of the Pacific Northwest, Washington State is a mesmerizing blend of natural wonders and urban sophistication. 
Its geography is a tapestry of contrasts, stretching from the rugged Pacific coastlines to the dense, verdant rainforests of the Olympic Peninsula, culminating in the majestic Cascade Mountains. 
Among these peaks, Mt. Rainier stands as a sentinel, an active volcano and the pinnacle of the state’s natural beauty. 
This diverse terrain provides a playground for adventurers and nature lovers alike, offering an array of activities from serene hiking trails and challenging ski slopes to tranquil kayaking routes. 
Beyond its scenic landscapes, Washington's ecological diversity is a testament to its environmental richness, hosting an array of wildlife that includes the majestic orcas navigating the Puget Sound and elusive elk roaming the shadowy rainforests. 
This harmonious blend of natural beauty and wildlife creates a unique backdrop for the state, inviting both residents and visitors to immerse themselves in its outdoor wonders. 
Washington State, through its stunning geography and vibrant ecosystems, stands as a beacon of the Pacific Northwest's splendor, embodying the essence of adventure and the tranquility of nature in one cohesive landscape."""

replace_mt = unformatted_paragraph.replace("Mt.", "Mountain")

split_at_space = replace_mt.split(" ")

print(len(split_at_space)) 

    



