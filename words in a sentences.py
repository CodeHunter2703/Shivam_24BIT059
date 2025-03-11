sentence="""Artificial Intelligence is a joke. People keep going on and on about how it's going to revolutionize 
everything, from the way we work to the way we live. But guess what? It’s not. AI is being shoved down our throats as 
if it’s the savior of the modern world, when in reality, it’s just a bunch of algorithms that barely know what 
they’re doing.First of all, let’s talk about this obsession with "machine learning" and how it’s going to "change 
everything." Machine learning? More like machine confusion. Sure, some algorithms can make predictions based on data, 
but that doesn’t mean they actually understand anything. People have the nerve to call these machines "smart" just 
because they can identify a cat in a picture or beat a human at chess. Really? That’s intelligence? If that’s all it 
takes to be called "smart" these days, then I guess my toaster is a genius too because it knows how to heat bread. 
Then there’s the constant parade of "AI experts" acting like they’re on the cutting edge of something that matters. 
Let me tell you, these people have no clue what they’re doing. They slap some fancy code together, throw in a few 
neural networks, and boom — suddenly they’re saving the world with their algorithms. But what they don’t tell you is 
that AI is riddled with flaws. It's biased, it's unreliable, and it’s anything but trustworthy. Great job, geniuses, 
let’s trust a system that can’t even recognize a human face without making a mistake 30% of the time. Brilliant. And 
don’t even get me started on the so-called "AI jobs" that everyone’s raving about. The idea that AI will create jobs 
while simultaneously eliminating others is laughable. These so-called advancements are going to put people out of 
work, not help them. More automation, more machines taking over tasks that humans have been doing for centuries. 
Great, we’ll all be unemployed, but hey, at least we’ll have AI bots to "assist" us in our misery. We’ll be sitting 
at home, staring at our screens, wondering why we bothered to get an education when machines can do it all. But let’s 
not forget the tech companies that are driving this AI frenzy. They sell us this fantasy of a utopian world where 
robots take care of everything, but they’re only doing it for their own benefit. The truth is, these companies are 
just looking for ways to exploit AI to increase their profits. They’re not building AI to help you; they’re building 
it to control you. These corporations are putting profits over people’s well-being, and AI is their latest weapon in 
the war against the working class. In reality, AI is just another overhyped trend that’s being pushed by people who 
have nothing better to do than watch a few YouTube videos on machine learning and pretend they know what they’re 
talking about. They act like it’s the future of everything, but the only future AI is going to have is as a tool for 
the rich to further oppress the rest of us. So yeah, let’s all get excited about AI taking over our lives. Just don’t 
be surprised when the robots don’t save us, they just leave us more confused, more divided, and more miserable than 
ever before."""
def scraper(sentence,target):
    count=0
    word=sentence.split(' ')
    for w in word:
        w.strip('.' or ',' or "'")
        if w.upper()==target.upper():
            count+=1
    return count
target="ai"
c=scraper(sentence,target)
print(f"the word {target } appears {c} times in the sentence")
