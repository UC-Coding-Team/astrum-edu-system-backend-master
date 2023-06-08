from django.db import models

from core.utils.time import get_now


class BaseManager(models.Manager):
    """
    Our basic manager is used to order all child models of AbstractLayer
    by created time (descending), therefore it creates a LIFO order,
    causing the recent ones appear first in results.
    """

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')


class AbstractLayer(models.Model):
    """
    All basic abstraction is done here.
    Also, we'll implement some methods which will simplify the work with models.
    """

    # All objects in our database are going to have time of creation and last updated time.
    created_at = models.DateTimeField(default=get_now)
    updated_at = models.DateTimeField(default=get_now)

    # let's configure managers
    objects = BaseManager()

    class Meta:
        abstract = True

    @classmethod
    def get(cls, *args, **kwargs):
        """
        We use our custom get method to avoid errors (like Not Found).
        This way we won't have to use try/except for the rest of our codebase (at least for non-existing objects).
        :param args:
        :param kwargs:
        :return: object of model
        """
        return cls.objects.get(*args, **kwargs)

    @classmethod
    def filter(cls, *args, **kwargs):
        """
        Just to reduce the model.objects.filter to model Filter
        :param args:
        :param kwargs:
        :return: QuerySet
        """
        return cls.objects.filter(*args, **kwargs)

    @classmethod
    def all(cls):
        """
        Shortcut for model.objects.all
        """
        return cls.objects.all()

    def save(self, *args, **kwargs):
        """
        We won't be using auto_now and auto_add_now for created_time and last_updated_time,
        since they might cause unintentional errors in the future.
        Instead, we implement custom save method to update them.
        :param args:
        :param kwargs:
        :return: None
        """
        self.updated_at = get_now()
        super().save(*args, **kwargs)

    @classmethod
    def create(cls, *args, **kwargs):
        """
        Since we are not using auto fields for created_time,
        we will be implementing our custom create method to take care of that.
        Also, we reduce model.objects.create to model.create.
        :param args:
        :param kwargs:
        :return: created object
        """
        now = get_now()
        obj = cls(
            *args,
            **kwargs,
            created_at=now,
            updated_at=now
        )
        obj.save()
        return obj
