# -*- coding: UTF-8 -*-
# __author__ = 'liuhc'
import os
import  django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rwm.settings")
django.setup()


def main():
    from calc.models import CalcTest
    with open('data.txt') as f:
        for line in f:
            name, age = line.split("***")
            CalcTest.objects.create(name=name, age=age)

if __name__ == '__main__':
    main()
    print("Done!")