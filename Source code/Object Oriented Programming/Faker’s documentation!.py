# Use faker.Faker() to create and initialize a faker generator, 
# which can generate data by accessing properties named after the type of data you want.

# from faker import Faker
# fake = Faker()

# fake.name()
# 'Lucy Cechtelar'

# fake.address()
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'

# fake.text()
# 'Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi
#  beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt
#  amet quidem. Iusto deleniti cum autem ad quia aperiam.
#  A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur qui
#  quaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernatur
#  voluptatem sit aliquam. Dolores voluptatum est.
#  Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.
#  Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.
#  Et sint et. Ut ducimus quod nemo ab voluptatum.'


# Each call to method fake.name() yields a different (random) result.
# This is because faker forwards faker.Generator.method_name() calls to faker.Generator.format(method_name).


# for _ in range(10):
#   print(fake.name())

# 'Adaline Reichel'
# 'Dr. Santa Prosacco DVM'
# 'Noemy Vandervort V'
# 'Lexi O'Conner'
# 'Gracie Weber'
# 'Roscoe Johns'
# 'Emmett Lebsack'
# 'Keegan Thiel'
# 'Wellington Koelpin II'
# 'Ms. Karley Kiehn V'



# Providers
# Each of the generator properties (like name, address, and lorem) are called “fake”.
# A faker generator has many of them, packaged in “providers”.

# from faker import Factory
# from faker.providers import internet

# fake = Factory.create()
# fake.add_provider(internet)

# print(fake.ipv4_private())


# Localization

# faker.Factory can take a locale as an argument, to return localized data. 
# If no localized provider is found, the factory falls back to the default en_US locale.

# from faker import Faker
# fake = Faker('it_IT')
# for _ in range(10):
#     print(fake.name())

# 'Elda Palumbo'
# 'Pacifico Giordano'
# 'Sig. Avide Guerra'
# 'Yago Amato'
# 'Eustachio Messina'
# 'Dott. Violante Lombardo'
# 'Sig. Alighieri Monti'
# 'Costanzo Costa'
# 'Nazzareno Barbieri'
# 'Max Coppola'


# Command line usage
# When installed, you can invoke faker from the command-line:

# faker [-h] [--version] [-o output]
#       [-l {bg_BG,cs_CZ,...,zh_CN,zh_TW}]
#       [-r REPEAT] [-s SEP]
#       [-i {package.containing.custom_provider otherpkg.containing.custom_provider}]
#       [fake] [fake argument [fake argument ...]]



# Where:

# faker: is the script when installed in your environment, in development you could use python -m faker instead
# -h, --help: shows a help message
# --version: shows the program’s version number
# -o FILENAME: redirects the output to the specified filename
# -l {bg_BG,cs_CZ,...,zh_CN,zh_TW}: allows use of a localized provider
# -r REPEAT: will generate a specified number of outputs
# -s SEP: will generate the specified separator after each generated output
# -i {my.custom_provider other.custom_provider} list of additional custom providers to use. Note that is the import path of the package containing your Provider class, not the custom Provider class itself.
# fake: is the name of the fake to generate an output for, such as name, address, or text
# [fake argument ...]: optional arguments to pass to the fake (e.g. the profile fake takes an optional list of comma separated field names as the first argument)
# Examples:

# $ faker address
# 968 Bahringer Garden Apt. 722
# Kristinaland, NJ 09890

# $ faker -l de_DE address
# Samira-Niemeier-Allee 56
# 94812 Biedenkopf

# $ faker profile ssn,birthdate
# {'ssn': u'628-10-1085', 'birthdate': '2008-03-29'}

# $ faker -r=3 -s=";" name
# Willam Kertzmann;
# Josiah Maggio;
# Gayla Schmitt;
# How to create a Provider
# from faker import Faker
# fake = Faker()

# first, import a similar Provider or use the default one
# from faker.providers import BaseProvider

# create new provider class. Note that the class name _must_ be ``Provider``.
# class Provider(BaseProvider):
#     def foo(self):
#         return 'bar'

# then add new provider to faker instance
# fake.add_provider(Provider)

# now you can use:
# fake.foo()
# 'bar'
# How to customize the Lorem Provider
# You can provide your own sets of words if you don’t want to use the default lorem ipsum one. The following example shows how to do it with a list of words picked from cakeipsum :

# from faker import Faker
# fake = Faker()

# my_word_list = [
# 'danish','cheesecake','sugar',
# 'Lollipop','wafer','Gummies',
# 'sesame','Jelly','beans',
# 'pie','bar','Ice','oat' ]

# fake.sentence()
# 'Expedita at beatae voluptatibus nulla omnis.'

# fake.sentence(ext_word_list=my_word_list)
# 'Oat beans oat Lollipop bar cheesecake.'
# How to use with Factory Boy
# Factory Boy already ships with integration with Faker. Simply use the factory.Faker method of factory_boy:

# import factory
# from myapp.models import Book

# class BookFactory(factory.Factory):
    # class Meta:
        # model = Book

    # title = factory.Faker('sentence', nb_words=4)
    # author_name = factory.Faker('name')
# Accessing the random instance
# The .random property on the generator returns the instance of random.Random used to generate the values:

# from faker import Faker
# fake = Faker()
# fake.random
# fake.random.getstate()
# By default all generators share the same instance of random.Random, which can be accessed with from faker.generator import random. Using this may be useful for plugins that want to affect all faker instances.

# Seeding the Generator
# When using Faker for unit testing, you will often want to generate the same data set. For convenience, the generator also provide a seed() method, which seeds the shared random number generator. Calling the same methods with the same version of faker and seed produces the same results.

# from faker import Faker
# fake = Faker()
# fake.seed(4321)

# print(fake.name())
# 'Margaret Boehm'
# Each generator can also be switched to its own instance of random.Random, separate to the shared one, by using the seed_instance() method, which acts the same way. For example:

# from faker import Faker
# fake = Faker()
# fake.seed_instance(4321)

# print(fake.name())
# 'Margaret Boehm'
# Please note that as we keep updating datasets, results are not guaranteed to be consistent across patch versions. If you hardcode results in your test, make sure you pinned the version of Faker down to the patch number.

# Tests
# Installing dependencies:

# $ pip install -e .
# Run tests:

# $ python setup.py test
# or

# $ python -m unittest -v tests
# Write documentation for providers:

# $ python -m faker > docs.txt