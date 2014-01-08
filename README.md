wxBlender
=========
wxPython in Blender

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


License
-------
GNU GPL v2.0

http://www.gnu.org/licenses/old-licenses/gpl-2.0.html


Tested On
---------

| Operating System          | Blender Versions            | Phoenix           |
|:-------------------------:|:---------------------------:|:-----------------:|
| Windows XP SP3 32bit      | 2.65 - 2.69                 | 3.0.1.dev75563    |
| Other OS                  | TODO                        |                   |
