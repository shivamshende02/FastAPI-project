from fastapi import FastAPI , HTTPException

app = FastAPI()

text_posts = {1: {"title":"New Post","content":"this is a cool test post"},
2: {"title":"Morning Motivation","content":"Start your day with purpose. Small consistent efforts create big results over time."},

3: {"title":"Tech Trends","content":"Artificial intelligence and quantum computing are shaping the future of technology."},

4: {"title":"Weekend Plans","content":"Thinking about spending the weekend learning a new skill and relaxing with good music."},

5: {"title":"Coding Journey","content":"Today I solved a challenging programming problem and learned a better way to optimize code."},

6: {"title":"Study Notes","content":"Revision becomes easier when concepts are understood deeply instead of memorized."},

7: {"title":"Fitness Goals","content":"Completed a workout session today. Consistency matters more than intensity."},

8: {"title":"Travel Dreams","content":"One day I want to explore beautiful mountains and experience different cultures around the world."},

9: {"title":"Coffee Thoughts","content":"A warm cup of coffee and a good book can turn an ordinary day into a productive one."},

10: {"title":"Daily Reflection","content":"Every challenge teaches something valuable if you take time to understand the lesson."},

11: {"title":"AI Discussion","content":"Machine learning models are becoming more capable in understanding language and solving problems."},

12: {"title":"Music Vibes","content":"Listening to relaxing music while studying helps improve focus and mood."},

13: {"title":"Project Update","content":"Made progress on the web application today and fixed several bugs successfully."},

14: {"title":"Learning Python","content":"Practicing Python every day makes programming concepts easier to understand."},

15: {"title":"Nature View","content":"Watching sunsets and spending time in nature creates a peaceful state of mind."}
}

@app.get("/posts")
def get_all_posts(limit:int):
    return list(text_posts.items())[:limit]

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    else:    
        return text_posts.get(id)
