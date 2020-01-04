# DjangoSnippets 
* This repository holds random snippets of code I found useful in Django projects 
* *DISCLAIMER* Code has not been thouroughly tested or debugged, use at your own risk

## Contents
- **SaveFilterMixin**
  - Can be used as a mixin for django-filters FilterView,
  - This mixin saves users filter selections and re-applys them after they have navigated away from the page. Mixix in will also apply the      filter to a django-tables2 table if you are using SingleTableMixin. 
  - You must have user sessions enabled in your project for this to work.
