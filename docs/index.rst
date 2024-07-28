.. Wagtail Forms documentation master file, created by
   sphinx-quickstart on Sat Oct 14 14:40:45 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Wagtail forms
===================

Allows you to build forms in the CMS admin area and add them to any StreamField in your site.
You can add your own fields along with the vast array of default fields which include the likes
of file fields. Form submissions are controlled by hooks that you can add that process the forms cleaned data.
Templates can be created which will then appear as choices when you build your form,
allowing you to display and submit a form however you want.


What else is included?
----------------------

*  Each form is built using a StreamField.
*  Customise things like success and error messages, post submit redirects and more.
*  Forms are processed via a ``before_page_serve`` hook. Meaning there is no fuss like remembering to include a page mixin.
*  The hook can easily be disabled to provide the ability to create your own.
*  Form submissions are controlled via hooks meaning you can easily create things like emailing the submission which you can turn on and off on each form.
*  Fields can easily be added to the form from your own code such as Recaptcha or a Regex Field.
*  The default set of fields can easily be replaced to add things like widget attributes.
*  Form submissions are also listed by their form which you can filter by date and are ordered by newest first.
*  Files can also be submitted to the forms that are shown with the form submissions.
*  A form and its fields can easily be copied to a new form.
*  There is a template tag that can be used to render a form, in case you want it to appear outside a StreamField.

.. toctree::
   :maxdepth: 1
   :caption: Content

   installation
   usage
   templates
   fields
   advanced
   submission
   hooks
   permissions
   housekeeping
   settings
   contributors
   changelog
   screenshots
