all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]


def filter_colors(colors):
	return colors["sexy"] == True

resulting_colors= list(filter(filter_colors, (all_colors)))
    
def generate_li(colors):
   	return list(map(lambda x: f"<li>{x['label']}</li>", colors))

html_colors= generate_li(resulting_colors)

print(html_colors)

