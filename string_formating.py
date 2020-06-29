from string import Template

# regular string formating
my_str = "This is a place : {0} and here is an other : {1}!".format('sth',
                                                                    '01')
print(my_str)

# string formating with tremplates
my_template = Template('This is a template for books : ${title} by ${author}')
my_str2 = my_template.substitute(title='Bible', author='God')
print(my_str2)

# using dictionary with templates
books_dict = {
    'title': 'Bible',
    'author': 'God'
    }
my_str3 = my_template.substitute(books_dict)
print(my_str3)
