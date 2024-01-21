
# VideoStage

VideoStage is an application that allows you to display multimedia on the virtual backgrounds, or any other displays you would like. It is currently configured to send out data on `/dev/fb0`, though this can be modified to suit any needs, and we will be working more on this as use cases present themselves.

## Setup
- Clone the repository.
- Install FBI `sudo apt-get update` and `sudo apt-get install fbi -y`
- Install Flask and Python3 `sudo apt-get install python3` and `sudo apt-get install python3-flask`
-
## Setting up with multimedia
Currently the system only supports jpg and png files, which will be converted into the .fb format.

1. Use the `Upload files` function to upload your images, please give them names based on which cue you would like them to be a part of. e.x `1.jpg` `2.jpg` `3.jpg`
2. Use the terminal command `fbi --autozoom --fitwidth -T 1 --noverbose --device /dev/fb0 /home/pi/{your_image_file_name}.jpg` replacing {your_image_file_name}.jpg with the uploaded name. Leave the displayed image on the screen. More switches in this are available at the end of this document.
3. Decide which cue this image will be a part of. Then send the command `cat /dev/fb0 > /home/pi/{cue_number}.fb` once again replacing `{cue_number}` with the actual cue you would like to assign.
4. Repeat this as many times as needed. 
5. Figure out the hostname of the device, and edit the templates/index.html to have the correct IP address, or... just set the router to assign the IP address of 10.0.0.181.
6. Finally send`sudo reboot` for the changes to take effect.

## Running it live in a show
Not much setup is required, beyond pressing the `setup` button, which is available on the webpage at `10.0.0.181:105` or `127.0.0.1:105` or `{ip_address}:105`

## FBI Switches
```
**-h,** **--help**
              Print usage info.

       **-V,** **--version**
              Print **fbi** version number.

       **--store**
              Write command line arguments to config file [~/.fbirc](file://~/.fbirc).

       **-l** file**,** **--list** file
              Read image filelist from file.

       **-P,** **--text**
              Enable  textreading  mode.  In  this  mode  **fbi**  will  display large images without
              vertical offset (default is to center the images). The **SPACE** command will first try
              to  scroll down and go to the next image only if it is already on the bottom of the
              page. Useful if the images you are watching are text pages, all you have to  do  to
              get the next piece of text is to press space...

       **-a,** **--autozoom**
              Enable autozoom.  **Fbi** will automagically pick a reasonable zoom factor when loading
              a new image.

       **--(no)autoup**
              Like autozoom, but scale up only.

       **--(no)autodown**
              Like autozoom, but scale down only.

       **--(no)fitwidth**
              Use width only for autoscaling.

       **-v,** **--(no)verbose**
              Be verbose: enable status line on the bottom of the screen (enabled by default).

       **-u,** **--(no)random**
              Randomize the order of the filenames.

       **--(no)comments**
              Display comment tags (if present) instead of the filename. Probably only useful  if
              you  added  reasonable comments yourself (using **[wrjpgcom](https://manpages.ubuntu.com/manpages/xenial/man1/wrjpgcom.1.html)**(1) for example), otherwise
              you likely just find texts pointing to the software which created the image.

       **-e,** **--(no)edit**
              Enable editing commands.

       **--(no)backup**
              Create backup files (when editing images).

       **-p,** **--(no)preserve**
              Preserve timestamps (when editing images).

       **--(no)readahead**
              Read ahead images into cache.

       **--cachemem** size
              Image cache size in megabytes (default is 256).

       **--blend** time
              Image blend time in miliseconds.

       **-T** n**,** **--vt** n
              Start on virtual console n.

       **-s** steps**,** **--scroll** steps
              Set scroll steps in pixels (default is 50).

       **-t** sec**,** **--timeout** sec
              Start a continuous slideshow where each image is loaded  at  sec  second  intervals
              without any keypress.

       **-1,** **--(no)once**
              Don't loop (only use with **-t**).

       **-r** n**,** **--resolution** n
              Select resolution, n = 1..5 (default is 3, only PhotoCD).

       **-g** n**,** **--gamma** n
              Gamma  correction.  Requires  Pseudocolor  or  Directcolor visual, doesn't work for
              Truecolor (default is 1).

       **-f** <arg>**,** **--font** <arg>
              Set font. This <arg> can be anything fontconfig accepts (see  **[fonts-conf](https://manpages.ubuntu.com/manpages/xenial/man5/fonts-conf.5.html)**(5)).   Try
              **[fc-list](https://manpages.ubuntu.com/manpages/xenial/man1/fc-list.1.html)**(1)  for a list of known fonts on your system. The fontconfig config file is
              evaluated as well, so any generic stuff defined there (such  as  mono,  sans)  will
              work  as well. It is recommended to use monospaced fonts, the textboxes (help text,
              exif info) look better then.

       **-d** /dev/fbN**,** **--device** /dev/fbN
              Use /dev/fbN device framebuffer. Default is the one your virtual console is  mapped
              to.

       **-m** videomode**,** **--mode** videomode
              Name of the video mode to use (video mode must be listed in /etc/fb.modes). Default
              is not to change the video mode.```
