from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .search import LeadIndex

# Create your models here.


# Blogpost to be indexed into ElasticSearch
class LeadPost(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leadpost')
   project = models.CharField(max_length=200)
   posted_date = models.DateField(default=timezone.now)
   business_website = models.URLField(max_length=200)
   first_name = models.TextField(max_length=200)
   second_name = models.TextField(max_length=200)
   corporate_email = models.EmailField(max_length=200)
   industry = models.TextField(max_length=200)
   corporate_phone_number = models.IntegerField
   company_size = models.TextField(max_length=200)
   state = models.TextField(max_length=200)
   country = models.TextField(max_length=200)

   def indexing(self):
      obj = LeadIndex(
         meta={'id': self.id},
         author=self.author.username,
         project=self.project,
         posted_date=self.posted_date,
         business_website=self.business_website,
         first_name=self.first_name,
         second_name=self.second_name,
         corporate_email=self.corporate_email,
         industry=self.industry,
         corporate_phone_number=self.corporate_phone_number,
         company_size=self.company_size,
         state=self.state,
         country=self.country
      )
      obj.save()
      return obj.to_dict(include_meta=True)
