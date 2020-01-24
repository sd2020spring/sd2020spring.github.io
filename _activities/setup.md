---
title: Set Up Your Development Environment
date: 2019-08-30 13:30:00 -04:00
---

{% include toc %}

Before we can get down to the business, we need to make sure we have the right
tools for the job. If you follow these instructions (with help from our amazing
NINJA team), your computer will be primed and ready to do some serious
computational work.

Initially, the amount of new stuff here may seem intimidating. Please do not let
this discourage you! We (NINJAs and faculty) will provide lots of help and
guidance along the way to help you setup, and then gain comfort with your new
toolset. The process will start at the end of the first class, and will continue
with additional NINJA / faculty office hours to help you complete the process
successfully. Additionally, you will gain familiarity and comfort with this
toolset as the semester progresses. In other words, you should think of learning
the toolset as a process and not something that you need to do all at once.

## An overview of the installation process

Setting up a development environment on your machine involves (1) installing
Ubuntu on your laptop, (2) installing Python and related tools that you will
need for most of the programming in this course, and (3) getting set up with
Git and GitHub, which we will use to manage the code we write.

### A few notes about your setup and the instructions

In the instructions we provide below, we assume that you are currently on a
laptop (and likely an Olin-issued laptop) that only has Windows 10 installed on
it. We have tested these instructions on such a laptop, but we expect that these
instructions should work for the vast majority of cases.

If you have previous experience with any of the steps described below, feel free
to do things a different way. However, the more your laptop differs from our
assumed setup (e.g., is a Linux or Mac) or the more you deviate from our
standard instructions, the more difficulty we will have helping you if anything
goes wrong during the process.

## Step 1: Install Ubuntu

Our officially supported operating system (OS) is Ubuntu 18.04 (64-bit). The
steps below will cover how you can install the OS on your laptop.

### Choose your installation method

There are two primary ways you can install Ubuntu on your system.

You can *dual-boot* Windows and Ubuntu, meaning that you will install Ubuntu on
your machine in such a way that both OSes live side-by-side on your machine.
Whenever you boot you computer, you will be able to select which OS to load.

The main advantage of a dual-boot system is that each OS can easily access and
make full use the machine's hardware. This makes the setup particularly
well-suited to doing intensive computation or things like audiovisual
processing. Dual-booting does have a few disadvantages: switching between OSes
requires you to restart your machine (so you cannot use both OSes at once), and
you need to commit space on your hard drive exclusively for Ubuntu. If one of
your OSes fills its allocated disk space, it is difficult to use disk space
allocated for the other OS.

You can instead install Ubuntu as a *virtual machine (VM)*. In this setup, your
Windows machine essentially runs an application that emulates hardware (like a
CPU, RAM, graphics card, and monitor) for Ubuntu to interact with. Your computer
always boots into Windows, and when you want to use Ubuntu, you can start the VM
through the application.

Installing Ubuntu as a VM is significantly more flexible than a dual-boot setup:
you can pop into Ubuntu for a few minutes without leaving Windows, and in most
cases it is straightforward to change the hardware that Ubuntu sees (for
example, you can allocate a certain amount of computational resources to Ubuntu
and change this quite easily). However, using a VM does come with some
disadvantages. It does take a fair bit of computational overhead to run Ubuntu
in this environment, so balancing the resources you allocate to Ubuntu versus
Windows can be a bit tricky. In addition, accessing the actual hardware on your
machine for things like audiovisual processing can be very difficult.

For the purposes of this course, we recommend that you install Ubuntu as a
dual-boot system.

### Dual boot installation (recommended method)

If you opt for the dual-boot route, we have provided bootable USB drives that
contain the installer for Ubuntu 18.04.1. Follow the instructions below to
install Ubuntu on your system.

#### Making space for Ubuntu

Before starting the installer on the USB drive, you will need to make space on
your hard drive for Ubuntu. You can do this by creating a *partition* on your
drive, which reserves a portion of your hard drive space for some purpose (in
this case, Ubuntu). If you have enough unused space in Windows (we recommend
around 50 GB), you can commit this space to Ubuntu, and the installer will take
care of the rest.

To create the partition, open the Windows start menu and type "diskmgmt.msc"
into the search box, then press Enter to start the Disk Management utility.
Each line you see indicates a different partition, and you may already have a
few. We are going to shrink one of these to make space for Ubuntu.

Select the largest partition (most likely your `C:\` drive). Then use the menu
bar at the top to navigate to `Action -> All Tasks -> Shrink Volume...`, which
will bring up a window.

In this window, you can shrink your partition by some size, specified in MB. If
allocating 50 GB, enter 50000 and proceed. Once the process is done, you should
see around 50 GB of "Unallocated Space".

In most cases, your machine should detect this new partition right away, but
you may want to restart into Windows again to make sure.

#### Running the USB installer

Now you will run the USB installer for Ubuntu on your machine. The installation
process can take a while, so be sure to budget enough time.

Power off your machine and insert the USB drive into an available port.

Power on your machine, and for Olin laptops, when the Dell logo appears, press
F12 until you see an alternate menu or loading screen. For other laptops, you
should search how to access the boot menu or BIOS settings for your specific
machine. This menu will allow you to select what device to boot from; select the
USB drive, which should have a name like Cruzer or SanDisk (essentially,
whatever is not Windows or IPv4/6). Navgate to the correct entry and press
Enter.

You will then see a menu that says "GNU GRUB" at the top and a few options.
Using the arrow keys, navigate to "Install Ubuntu" and press Enter. Be aware
that when the menu first appears, there is a countdown timer of a few seconds.
If you do not press any keys before that timer runs out, your machine will
automatically select the highlighted entry (which is usually "Try Ubuntu without
installing"). Pressing an arrow key will cancel the timer.

Most of the installation process is rather straightforward. Below are a few
things to note.

If you want to connect to a wired or wireless network during the installation
process, feel free to do so. To connect to wireless, use the instructions in the
next section. (**Note**: if you have a laptop issued by Olin IT this academic
year, you will not be able to connect to a wireless network and will not even
have the option to do so. Follow the appropriate steps in the post-installation
instructions below.)

You should choose to install Ubuntu alongside Windows Boot Manager when
prompted. You should also choose to install 3rd Party Software, which includes
better drivers for the hardware on your laptop. You should get a confirmation to
format a partition like `/dev/nvme0n1` or `/dev/sda1` as ext4; confirm to
proceed with installation.

During the installation, you can enter your name, computer name, username, and
password. Feel free to set this up with whatever you want, but we recommend that
you choose to require a password to log in. You will need this password not just
to log in, but also to install software.

Once the installation process has finished, you will get a prompt to remove the
USB drive from your computer and either press Enter or shut off your machine. On
the next boot, you will be presented with a menu of choices to boot into Ubuntu
or Windows (and usually, another option such as recovery mode). Similarly to
when you started the installer, there will be a countdown timer that will select
the default option when it runs out.

### VM installation

To install Ubuntu as a VM, you will need an application to run VMs. We recommend
[VirtualBox](https://www.virtualbox.org), which is free. You may also consider
VMWare Workstation (for Windows) or VMWare Fusion (for Mac), which require
purchase but typically have better performance.

You will also need an image of the installer as a `.iso` file. We will have a
couple USB drives available for this purpose, but you can also download the
image from the [Ubuntu download page](https://ubuntu.com/download/desktop). The
latest version (18.04.3) is about 2 GB in size.

If you are using VirtualBox, open the VM Manager and select "New" to create a
new VM. You can give your VM any name you want, but make sure the Type is
"Linux" and Version is "Ubuntu (64-bit)". You may also be able to choose how
much CPU, RAM, or disk space to allocate. We recommend at least 2 CPUs
(preferably 4), 2 GB of RAM (preferably 4), and 50 GB of disk space. You can
also change these later in the Settings menu of the VM.

When you first start your VM, you will be prompted to load the `.iso` file.
Select the appropriate file and proceed to start the installer.

The installation process from this point is largely the same as for a dual-boot
setup. See above for some tips regarding the installation. In the case of a VM,
you can erase the entire disk (as it is virtual) and install Ubuntu there.

Once the installation is done, you can simply restart the machine from the
VirtualBox menu bar to boot into Ubuntu.

You should also install the VirtualBox Guest additions, which provide some
tweaks to Ubuntu to make it easier to work with and access your Windows machine.
Follow the steps in the next section to update your system, then run the
following:

```bash
$ sudo apt install gcc make perl
```

Then, insert the Guest Additions CD-ROM. You can do this virtually through the
top menu of VirtualBox, using the Devices menu. This will prompt you to run the
software on the CD, and you will need your password to complete the
installation. Once done, restart your machine.

If you are experiencing sluggish performance, [consider checking the "Use Host
I/O Cache"
box](https://www.electricmonk.nl/log/2016/03/14/terrible-virtualbox-disk-performance/)
in the settings.

### Post-installation steps

Once you have installed Ubuntu, you will need to make sure that your system is
up to date.

#### Olin 2019-2020 laptops: update the kernel

If you have a laptop issued from Olin **this year** (i.e., you are a first-year
student or otherwise received this year's laptop), **your wi-fi will probably
not work** when you first boot your machine.

To get this to work, you need to update your kernel. Open a Terminal by pressing
`Ctrl-Alt-T`. Then, type the following (leave out the initial `$`) and press
`Enter`:

```bash
$ cd /media/<your username>/Ubuntu\ 18.04.3\ LTS\ amd64
```

replacing `<your username>` with the username you set during installation. Also,
after typing the first few characters of "Ubuntu", you should be able to press
`TAB` and have it autocomplete. This will move you into the folder (also called
a *directory*) with the correct files.

Check that you are in the correct folder with the following (again leaving
out `$`):

```bash
$ ls
```

This will display a list of files in the current folder. If you see `install.sh`
and many files starting with `linux-...` then you are in the correct folder. If
not, try

```bash
$ cd /media/<your username>/Ubuntu\ 18.04.3\ LTS\ amd641
```

instead. Once in the correct folder, type

```bash
$ sudo ./install.sh
```

This might take a while. Once done, restart your computer. Wireless connections
should now work.

#### Connect to the Internet

If you are not connected to a wired or wireless network, you should do so now.
For a wired connection, just plug in the cable. If you have an Olin network
account and want to connect to the wireless network, do the steps below.
(Cross-registered students can get an account by talking to IT, which is located
in the basement of Milas Hall.)

1. Click the NetworkManager icon in the system tray, which is normally just to
   the left of the speaker icon.
1. Select the OLIN wireless network.
1. Fill in your settings as shown and click "Connect"

![]({% link images/setup/wifi_settings.png %})

#### Update your system

Once you have a network connection, click on the top left of the desktop and
type "Software Updater", then select the Software Updater application. This will
prompt you to update the system with the latest packages, for which you will
need your password. Once you do this, you will be prompted to reboot.

For most updates, we will use the Terminal. To open this application, you can
press `Ctrl-Alt-T` or click the top left of the desktop and type "terminal". You
will notice that the terminal allows you to input commands, and has a prompt
that ends with a dollar sign. When we want you to run commands in the terminal,
we will write them like this:

```bash
$ sudo apt update
$ sudo apt upgrade
```

Note that you do not have to include the dollar sign; we include it here to
indicate that these are terminal commands.

Run the two lines above (inputting your password if necessary) to update the
packages on your machine. Most software can be installed through these packages;
use `apt search <search-string>` to search for a specific package and `sudo apt
install <package-name>` to install a package.

#### Optional steps

You may also want to set up printers or access to a network share. You can do
that by following [wiki guides](http://wikis.olin.edu/linux/doku.php) written by
IT, but these may be out of date.

## Step 2: Install Python and related tools

Now, you will install Python and some related useful software tools. In
particular, you will install Jupyter, which allows you to run Python code in
computational notebooks, and Atom, a text editor that you can use to write,
modify, and run Python code.

### Installing Python

#### Choose a flavor of Python and libraries

When it comes to installing Python, you can choose to use *Anaconda*, a
prepackaged distribution that includes many libraries that you may use in this
course, or to install a set of Ubuntu packages. With Ubuntu, you can also choose
to install additional libraries as Ubuntu packages or use the software tool
`pip`. As with the decision to install Ubuntu in a dual-boot or VM setup, each
choice has its advantages and drawbacks.

In addition to shipping with many commonly used libraries, Anaconda is a bit
more intelligent in figuring out how libraries may depend on each other and how
to install and update them given those dependencies. It is also a bit easier to
maintain sets of installed packages and to switch between these sets for testing
or other purposes. Anaconda also does not require you to have administrator
permissions to install it. The biggest drawback of Anaconda is that if something
goes wrong, it can be quite difficult to diagnose or fix. Because Anaconda hides
what Python is doing under the hood, it is not a good choice if you want to
understand a better understanding of how to maintain a Python installation.
Anaconda will also likely take up more disk space because it ships with a larger
set of libraries than the alternatives do, though you can also get minimal
distributions.

If you decide to go the route of Ubuntu packages, you will likely find it easier
to fix if something goes wrong. Ubuntu packages have been extensively tested for
bugs and compatibility issues, and it is the "official" way to install Python
and its libraries. One of the drawbacks of having such extensive testing is that
package versions often lag behind the latest available versions, sometimes by a
year or more. You may also run into the case that a particular package is not
available from the official Ubuntu software repositories. In this case, you
would need to install the library from a third party and will not have the
benefit of the testing that the Ubuntu maintainers perform. Installing Ubuntu
packages also requires administrator (sudo) access.

Using `pip` is one of the more common ways to install packaged libraries, and
you can use this tool even if you have installed Python as an Ubuntu package.
Most packages can be installed with the command `pip install <packagename>` (on
Linux, you will usually need to run `sudo pip install <packagename>`), and it
comes with a search function as well. However, you should be aware that
installing packages this way *may* break your system without you realizing it,
as doing something administrator access implicitly assumes that you know the
risks of what you are doing. There may also be compatibility issues,
particularly if you forget whether you installed a library as an Ubuntu package
or as a `pip` package.

Whichever of these methods you choose, we strongly recommend that you stick with
your choice for the semester. Mixing and matching Python distributions and
library sources often ends in cryptic errors that are hard to fix.

#### Installing Python via Anaconda

You can download Anaconda directly from their
[site](https://www.anaconda.com/distribution/) ([direct link
here](https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh)). The
file will likely download to the directory `~/Downloads` (the `~` is shorthand
for your *home directory*, which is your user's main folder). You can navigate
to, and run, this setup script in Terminal like this:

```bash
$ cd ~/Downloads
$ chmod +x Anaconda3-2019.10-Linux-x86_64.sh
$ ./Anaconda3-2019.10-Linux-x86_64.sh
```

You probably do not need to fully understand the `chmod...` line for this
course, but in a nutshell, it enables the script to be executed. This is a
security feature in Linux that prevents you from accidentally downloading an
executing a malicious script before you can take a look at the code in it.

When you run the Anaconda installer, the first thing you will see is a license
agreement. You can navigate through the agreement text by pressing `f`.

When you reach the end of the agreement, you will see a prompt with some choices
that you can type in. For all of the prompts that you see in the installer,
pressing `Enter` with no other text will cause the input in square brackets to
be sent as default. (For the license agreement, this is `[no]`.)

For most of the installation process, the default answers are fine. However,
after the main part of the installation, there is a question that asks you about
running `conda init`. You should answer `yes` to this question, since it will
set up your Terminal environment to activate Anaconda by default.

Now close and reopen Terminal, and you should see that the prompt lines now
start with `(base)`. Then, if you run the following, Python should work:

```bash
$ python
```

#### Installing Python via Ubuntu

To install Python using a standard Ubuntu package, run the following in
Terminal.

```bash
$ sudo apt install python3
```

In this case, to start Python, you should use `python3` rather than `python` at
the terminal.

##### Installing Python packages

To install additional libraries or *packages*, you can use Ubuntu's package
manager or `pip`. On Ubuntu's repositories, packages are typically named
`python3-<packagename>`, like `python3-numpy`. You can install these like any
other Ubuntu package.

To install `pip`, simply run `sudo apt install python3-pip`. You can then run
`pip` using the command `pip3 <subcommand>`. Run `pip3 help` to see a list of
available commands.

### Installing Jupyter

Running `python` or `python3` will bring up an interactive prompt (similar to
Terminal) that can run Python code. The results of any code you run in the
prompt is deleted when you exit the prompt, unless you save it to a file in some
way. The interactive prompt also only understands Python, and is text only. You
cannot include additional text without causing an error, except through code
comments, and you cannot format the text.

To enable us to create documents of text and code, we use *computational
notebooks*. These are files that can be run in applications to display both
formatted text, Python code, and the results of running that code. Jupyter is
the software that allows us to write and run computational notebooks.

If you installed Anaconda, Jupyter should already be installed. Run `jupyter -h`
to ensure that it runs correctly. If not, you can run `conda install jupyter` to
install it.

If you installed Python via Ubuntu, you should run the following:

```bash
$ sudo apt install jupyter
```

Depending on what other packages you have installed up to this point, the above
command may install many other packages and take a while to run.

Once done, run `jupyter -h` to check that it runs.

### Installing Atom

Atom is an *integrated development environment (IDE)* that you can use to write
and run Python code. IDEs are far more intelligent than simple text editors,
allowing you to quickly and easily see coding errors, the overall structure of
your code, and code spread across many files. That being said, simple yet
extensible text editors such as Vim and Emacs are still quite popular, and you
may find it challenging and enjoyable to learn them. There are other popular
IDEs as well, such as PyCharm and Sublime Text.

In this course, we only support Atom, but feel free to install any coding
environment that works well for you and your project partners.

To install Atom, click in the top left corner of the desktop and search for
"Ubuntu Software". This is where you can find install software that is more in
the applications realm, such as Google Chrome. Search for and install Atom.

Atom has quite a few features. To learn how to use some of these features, you
can follow the [Atom
Basics](http://flight-manual.atom.io/getting-started/sections/atom-basics/)
guide, which covers how to create a text file and save it.

Atom is also extensible via packages, and you can explore the range of [packages
offered](http://flight-manual.atom.io/using-atom/sections/atom-packages/). In
this course, we will likely use the `script` and `Teletype` packages
extensively, so we encourage you to use those.

{::comment}
On Windows, if you see an error like this:

![](/images/setup/error_python-tools_480.jpg)

Then do the following:

1. In a terminal, enter `where atom`. This should report a *path* such as
   `C:\Users\MYNAME\AppData\Local\Continuum\Anaconda3\python.exe`, where MYNAME
   is your Windows login.
2. In Atom:
  * Use <kbd>Cmd+,</kbd> to open the Settings
  * Click on Packages in the sidebar
  * Find the "python-tools" package
  * Click Settings.
  * In the “Path to python directory” setting, paste the path from 1., *without*
    the final `python.exe`: for example,
    `C:\Users\MYNAME\AppData\Local\Continuum\Anaconda3\python.exe`
{:/comment}

## Step 3: Set up Git and GitHub.

Git is a version control system that we will use heavily in this class.

To install it, simply run the following in Terminal:

```bash
$ sudo apt install git
```

We'll talk more about git next time, but for now we'd also like you to sign up
for an account on [GitHub](https://github.com/) (if you don't have one already).
From Allen Downey's [online git
book](https://github.com/AllenDowney/amgit/blob/master/en/02-git-basics/01-chapter2.markdown#sign-up-for-github):

> GitHub is a web-based hosting service for Git users. In general a hosting
> service provides storage space on remote servers, network access, and tools
> and applications for interacting with stored data. GitHub provides storage for
> Git repositories and tools for interacting with them.
>
> There are other hosting services for Git, but GitHub is one of the most
> popular. It is so popular that people sometimes say “GitHub” when they mean
> “Git”, so just to be clear:
>
> * Git is an application that runs on your computer and helps you manage
>   repositories.
> * You can use Git to manage repos stored on your own computer or on any
>   computer configured as a Git server.
> * Anybody can set up and run a Git server. A company that runs Git servers
>   professionally is a Git hosting service.
> * GitHub is one of many Git hosting services.
>
> Ok, go to [https://github.com](https://github.com/). If you already have an
> account, log in. Otherwise, you will have to create one.
>
> You can choose any available username you like, but there are a few things you
> might want to think about:
>
> 1. Working on GitHub involves interacting with other people. They will see
>    your username, so choose wisely.
> 2. Some people, like `AllenDowney`, use their full names, but the most common
>    schema seems to be one-word lower-case usernames. For example, Scott Chacon
>    is `schacon`.
> 3. If you want to be anonymous, you can choose a username unrelated to your
>    real name; however,
> 4. Many software engineers use GitHub as part of their professional portfolio.
>    If a potential employer wants to check out your skills, they might look at
>    your GitHub repositories.
>
> It is probably a good idea to think of everything you do on GitHub as part of
> your public professional reputation.

This semester's faculty has a mix of username styles. Amon uses his full name
(`amonmillner`), Erhardt uses just his first name (`erhardt`), and Steve uses
a completely unrelated name (`syclops`).

