from datetime import datetime, date

def weeks_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return round((d2 - d1).days/7)

my_projects = [
    {
        'author': 'Charles', 
        'index': 1,
        'title':'Options Pricing', 
        'alt': 'Lawliet',
        'description': 'Pricing vanilla options using analytical and numerical valuation models.', 
        'comment' : """
        For my first project here I really want to post something fundamental/boring to kickstart my quant journey. 
        Will update this with exotic options in the near future, perhaps with a GUI app as well to go along. Peace out!""",
        'language': 'C++',
        'thumbnail': 'project1.png', 
        'dated_posted': '2021-06-07',
        'day_since_posted': weeks_between('2021-06-07', str(date.today())),
        'link': 'https://github.com/charlesyew/options-pricing',
        'category': 'Quantitative Finance',
        'tags': {'Derivatives', 'Pricing', 'Options'}
    },

    {
        'author': 'Charles', 
        'index': 2,
        'title':'Portfolio Analysis', 
        'alt': 'Miyazono', 
        'description': 'Run statistical tests on my current equities portfolio to uncover rebalancing and other insights.', 
        'comment' : """
        Okay, I lied... Here's another reasonably standard quant project to showcase my fundamentals. This project also serves to 
        formalize my own investing process so that I can learn more along the way. Double win!""",
        'thumbnail': 'project2.png', 
        'language': 'Python',
        'dated_posted': '2021-07-22',
        'day_since_posted': weeks_between('2021-07-22', str(date.today())),
        'link': 'https://github.com/charlesyew/portfolio-analysis',
        'category': 'Quantitative Finance', 
        'tags': {'Valuation', 'Equities', 'Portfolio Optimization', 'Mean-Variance Analysis'}
    },

    {
        'author': 'Charles', 
        'index': 3,
        'title':'Maslow index', 
        'alt': 'Midoriya', 
        'description': "Tracking the development of megatrends across different countries using features that correlates with the Maslow's hierarchy of needs.",
        'comment': 'This project is slightly larger than the previous two so it might take awhile to be published. Hope it works!',
        'thumbnail': 'project3.jpg',  
        'language': 'Python',
        'dated_posted': '2021-09-01',
        'day_since_posted': weeks_between('2021-09-01', str(date.today())),
        'link': '#',
        'category': 'Quantitative Finance', 
        'tags': {'Natural Language Processing', 'Deep Learning', 'Factor Investing'}
    }
]
wip = [
    {
        'author': 'Charles', 
        'index': 4,
        'title':'TBD', 
        'alt': 'Tetsurō', 
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ', 
        'comment': '...',
        'thumbnail': 'project4.jpg',  
        'language': 'TBD',
        'dated_posted': '2021-06-12',
        'day_since_posted': weeks_between('2021-06-08', str(date.today())),
        'link': '#',
        'category': 'Quantitative Finance', 
        'tags': {}
    }
        

        

]