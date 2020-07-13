# 1. Create a class named Course that has instance variables title, instructor, price, lectures, users(list type),
# ratings, avg_rating. Implement the methods __str__, new_user_enrolled, received_a_rating and show_details.
# From the above class, inherit two classes VideoCourse and PdfCourse. The class VideoCourse has instance variable
# length_video and PdfCourse has instance variable pages.


class Course:

    def __init__(self, title, instructor, price, lectures):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = []
        self.ratings = 0
        self.avg_rating = 0

    def __str__(self):
        print(f"Class Course {self.title} with {self.instructor} for price {self.price}")

    def new_user_enrolled(self, user):
        self.users.append(user)

    def received_a_rating(self, new_rating):
        self.avg_rating = (self.avg_rating * self.ratings + new_rating) / (self.ratings + 1)
        self.ratings += 1

    def show_details(self):
        print(f"Class Course {self.title} with {self.instructor} for price {self.price} with {self.lectures} and "
              f"the users are {self.users} with the ratings {self.ratings} and the avg rating is {self.avg_rating}")


class VideoCourse(Course):
    def __init__(self,title, instructor, price, lectures, length_video):

        super().__init__(title, instructor, price, lectures)
        self.length_video = length_video

    def show_details(self):
        super().show_details()
        print("Video length",self.length_video)


class PdfCourse(Course):
    def __init__(self, title, instructor, price, lectures, users, ratings, avg_rating, pages):
        super().__init__(title, instructor, price, lectures, users, ratings, avg_rating)
        self.pages = pages

    def show_details(self):
        super().show_details()
        print("Pages", self.pages)


v1 = VideoCourse('Dance','subash', '100', '11','100')
v1.show_details()
v1.new_user_enrolled('chan')
print(v1.users)
v1.__str__()