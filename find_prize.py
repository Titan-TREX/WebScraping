from bs4 import BeautifulSoup


with open("home.html", "r") as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, "lxml")


    course_cards = soup.find_all("div", class_="product-card")

    for course in course_cards:

        course_name = course.h3.text
        
     
        course_price = course.find('span', class_='price').text.split()[-1]

        print(f"Product: {course_name}")
        print(f"Price: {course_price}")
        print("-" * 20)