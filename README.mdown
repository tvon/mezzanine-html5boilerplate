
Overview
========

This is a mixture of a few existing themes, namely the html5boilerplate
Wordpress theme and Breakfast, a theme from http://www.opensourcedesign.com/.
The idea is not that you would use this theme as-is, but as with
html5boilerplate, as a jumping off point for your own theme.

Installation
============
(Largely a copied from Brent Hoover's [post](https://groups.google.com/group/mezzanine-users/browse_thread/thread/3345bdbef198d3c5) to GoogleGroups)

For this packages it's even easier since you actually don't need to install
anything. Just drop the contents of the directory you checked out into the
root of your project, and add the name of the directory to your
INSTALLED_APPS settings.

Clone out **mezzanine-html5boilerplate** 

    git clone git://github.com/tvon/mezzanine-html5boilerplate.git

Then just copy the directory out into your project like this:

(Notice the the dash has changed to an underscore, probably a name like
"mytheme" might work better)

    myprojectroot/
	            /mezzanine_html5boilerplate/
	                                       /templates
	                                       /templatetags
	                                       /etc...

Then in settings.py change your INSTALLED_APPS so it looks like so:

    .....<other_apps_snipped>
    "mezzanine.generic",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.pages",
    "mezzanine_html5boilerplate",

Then while you are working on modifying the theme, you will want to add:

    THEME="mezzanine_html5boilerplate"

Which allow mezzanine to use the theme without installing it. 