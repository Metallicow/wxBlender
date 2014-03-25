wxBlender
=========
[wxPython](http://wxpython.org/Phoenix/docs/html/index.html) + [Blender](http://www.blender.org/) = wxBlender

wxPython in Blender Addon for Blender.

wxPython toolkit widgets running in Blender.
Menus, Frames, Dialogs, Custom Buttons, Thumbnails, etc...

![wxBlender](https://raw.github.com/Metallicow/wxBlender/master/wxBlender_Screenshot.png)


Requirements
------------
* Blender 2.65+(built with Python33+)

  http://www.blender.org/

* wxPython Project Phoenix(works with Python3)

  http://wxpython.org/Phoenix/snapshot-builds/

* wxBlender

  https://github.com/Metallicow/wxBlender


Installation
------------
1. The phoenix download might come as a python .egg.

   Python .egg files are simply a renamed .zip file,
   so in other words you can open/extract the egg
   with an compression application
   such as 7-zip, WinRAR, etc.

   Place wx directory from the phoenix download
   in Blender's `#.##/python/lib/site-packages` directory.

2. Place the wx_blender directory in your Blender User `scripts/addons` directory.

   Depending on your type of Blender build, this location may vary.
   Ex: if Blender is portable.


Running wxBlender
-----------------
1. Start up Blender.
2. Go to File>User Preferences... in the MenuBar.
3. Under the "Addons" tab of the Blender User Preferences Dialog...
   ...Check the "3D View: wxBlender" addon checkbox.
4. Click the "Save User Settings" button in the Blender User Preferences Dialog
   so the plugin starts at startup.
5. Close the Blender User Preferences Dialog.

In the properties window of the 3D View there should now be a Panel
named "wxBlender".


[Blender logo usage guidelines](http://www.blender.org/about/logo/)
-------------------------------------------------------------------
![BlenderFavicon](https://raw.github.com/Metallicow/wxBlender/master/wx_blender/images/favicon.ico)
![BlenderLogo](https://raw.github.com/Metallicow/wxBlender/master/wx_blender/images/logo.png)

The Blender logo is a copyrighted property of NaN Holding B.V, and has been licensed in 2002 to the Blender Foundation. The logo and the brand name "Blender" are not part of the GNU GPL, and can only be used commercially by the Blender Foundation on products, websites and publications.

Under the following conditions, third parties may use the Blender logo as well:

  1. The logo can only be used to point to the product Blender. When used with a link on a web page, it should point to the url [blender.org](http://www.blender.org/).
  2. You will visualize and promote your own branding more prominent than you use the Blender logo. The Blender logo only can be used as a secondary brand, which means it has to be clear for an average viewer that this is not an official Blender or Blender Foundation website, publication or product.
  3. You can use the Blender logo on promotion products, such as T-shirts or caps or trade show booths, provided it is a secondary brand as described in point 2.
  4. The logo is used unaltered, without fancy enhancements, in original colors, original typography, and always complete (logo + text blender).
  5. In case you use the logo on products you sell commercially, you always have to [contact us](http://www.blender.org/foundation/) with a picture of how it will be used, and ask for explicit permission.

If you have further questions or doubts, do not hesitate to [contact us](http://www.blender.org/foundation/).
Usage in artwork and community websites


[Usage in artwork and community websites](http://www.blender.org/about/logo/)
-----------------------------------------------------------------------------

Blender's logo has been used in hundreds of ways. This was - and still is - considered to be an honest tribute to Blender, and the guidelines are not meant to make these uses "illegal" or "officially disapproved". This page is only meant to clarify the Blender Foundation guidelines so that people know their minimum rights and where they can use the logo.

Modifying the Blender logo is really part of your own artistic freedom, and the Blender Foundation will never act against such tributes. Just don't expect us to "officially approve" of it, that's all.

Thanks,

Ton Roosendaal, Chairman of the Blender Foundation

Amsterdam, March 2009


License
-------
Anything **NOT** involving "Blender" Logos and Graphics/Images/blender16 PyEmbeddedImage is licensed

GNU GPL v2.0

http://www.gnu.org/licenses/old-licenses/gpl-2.0.html


Tested On
---------

| Operating System          | Blender Versions            | Phoenix           |
|:-------------------------:|:---------------------------:|:-----------------:|
| Windows XP SP3 32bit      | 2.65 - 2.70                 | 3.0.1.dev76189    |
| Other OS                  | TODO                        |                   |

