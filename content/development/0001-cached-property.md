Title: django's cached_property
date: 2014-06-12 16:00
tags: python, django
slug: django-cached-property

If you find yourself using `@property` a lot in your model and the _property_ 
costs database queries, you might want to consider using [cached_property][] instead.

For example:

    :::python
    ...
    from django.utils.functional import cached_property
    ...

    class Book(models.Model):
        ...

        @cached_property
        def references(self):
            ...
            # more queries here
            return references

So instead re-query everytime you call the property, it'll use cache instead,
as long as the instance still exists.


[cached_property]: https://docs.djangoproject.com/en/1.6/ref/utils/#django.utils.functional.cached_property "cached_property"
