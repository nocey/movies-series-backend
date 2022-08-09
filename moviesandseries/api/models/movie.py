from django.db import models


class Movie(models.Model):
    # class Meta:
    #     verbose_name = ("Movie")
    #     verbose_name_plural = _("Movies")

    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publicaton_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Movie_detail", kwargs={"pk": self.pk})
