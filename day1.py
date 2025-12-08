content_view = {
    "Power of Sabr by Mufti Menk": 25000,
    "Youth and Social Media by Ali Hammuda": 30000 ,
    "Lessons from Umar ibn Khattab": 84488,
    "Tawakkul and Faith Reminder": 477738,
    "Love of Prophet Muhammad ﷺ": 47382,
    "Time Management in Islam": 333333,
    "Overthinking and Anxiety Remedy": 12332,
    "Marriage Problems in Islamic View": 332423,
    "Story of Bilal RA": 3444335,
    "Forgiveness in Islam": 334432
}

total_views=sum(content_view.values())
max_view=max(content_view.values())
top_content=max(content_view, key=content_view.get)

print("Total Views:", total_views)
print("Most Viewed:", top_content, "| Views:", max_view)

