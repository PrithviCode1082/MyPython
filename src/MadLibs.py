# Language
# LOC
# Problem/Goal
# Difficulty
# time_spent
# snacks_you_ate
# OS_support
# Status_of_dev
# deploy - local/github/gitlab
# review

words = [input(f"{word}: ") for word in ["language", "LOC", "goal", "difficulty", "time", "food", "OSes", "state", "deploy", "review"]]

story = """I used {0[0]} for my new app, with {0[1]} lines of code.
The App is all about {0[2]}, and it was {0[3]}. I spent {0[4]} hours 
while devouring {0[5]}. Coming back, The app supports {0[6]} and I'm quite {0[7]}.
I've deployed it {0[8]} and got {0[9]} review.
""".format(words)

print(story)