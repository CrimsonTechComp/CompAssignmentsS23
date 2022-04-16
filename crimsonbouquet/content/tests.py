from turtle import title
from django.test import TestCase

# Create your tests here.
query {
  contributor(id: 1) {
    content {
        title
    }
  }
} 


query {
    content(slug: "why-yelan-is-gamechaning") {
        contributors {
            firstName
            lastName
        }
    }
}