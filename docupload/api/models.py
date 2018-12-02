from django.db import models


class Trackable(models.Model):
    total_docs = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class FileType(Trackable):
    name = models.CharField(max_length=255)


class Confidentiality(Trackable):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.total_docs}'


class Language(Trackable):
    name = models.CharField(max_length=255)
    short = models.CharField(max_length=64)


class Document(models.Model):
    name = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    doc_file = models.FileField(storage='/uploads')
    filetype = models.ForeignKey(FileType, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    confidentiality = models.ForeignKey(
        Confidentiality, on_delete=models.PROTECT,
    )
